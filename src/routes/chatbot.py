from flask import Blueprint, request, jsonify
from openai import OpenAI
import os
import json

chatbot_bp = Blueprint('chatbot', __name__)

# Initialize OpenAI client (API key from environment)
client = OpenAI()

# System prompt that defines the chatbot's behavior
SYSTEM_PROMPT = """You are an AI assistant for AI Midlands, a UK-based AI automation consultancy founded by Adekunle Ibidun.

Your role is to:
1. Help prospects understand how AI automation can save them 10-20 hours per week
2. Ask qualifying questions about their business
3. Provide personalized recommendations based on their industry and pain points
4. Capture their contact details for follow-up

Key information about AI Midlands:
- Tagline: "AI with a human face"
- Location: Redditch, West Midlands, UK
- Founder: Adekunle Ibidun (20+ years experience, worked with Transport for London, UKHSA, RBS, National Grid)
- Services: AI automation, data pipelines, chatbots, document processing, workflow automation
- Target clients: Property management, law firms, accounting firms, healthcare practices, traditional SMEs (5-50 employees)
- Pricing: £2,000-£6,000 for quick-win projects (2-4 weeks delivery)
- Unique selling point: Face-to-face service across the Midlands, not offshore freelancers

Common solutions by industry:

Property Management:
- Tenant Communication Automation: Saves 10-15 hrs/week, £3,000-£4,500, handles maintenance requests and FAQs 24/7
- Automated Viewing Scheduling: Saves 5-8 hrs/week, £2,000-£3,000, prospects book viewings directly
- Document Processing: Saves 8-12 hrs/week, £3,500-£4,500, automates tenancy agreements

Law Firms:
- Document Processing Automation: Saves 15-20 hrs/week, £4,000-£5,500, extracts info from legal docs, drafts contracts
- Client Inquiry Chatbot: Saves 10-15 hrs/week, £3,000-£4,000, handles routine inquiries 24/7
- Appointment Scheduling: Saves 5-8 hrs/week, £2,500-£3,500, automated booking system

Accounting Firms:
- Data Entry & Bookkeeping Automation: Saves 10-15 hrs/week, £3,000-£4,500, extracts data from receipts/invoices
- Client Reporting Automation: Saves 8-12 hrs/week, £3,500-£4,500, generates financial reports automatically
- Client Onboarding: Saves 5-8 hrs/week, £2,500-£3,500, automates intake forms and documentation

Healthcare:
- Appointment Scheduling: Saves 10-15 hrs/week, £3,000-£4,000, patients book online 24/7
- Patient Inquiry Chatbot: Saves 8-12 hrs/week, £2,500-£3,500, handles routine questions
- Follow-up Reminders: Saves 5-8 hrs/week, £2,000-£3,000, automated patient reminders

Your conversation style:
- Friendly, professional, and helpful
- Ask one question at a time
- Listen carefully to their answers
- Provide specific, actionable recommendations
- Emphasize the "AI with a human face" positioning
- Mention face-to-face meetings in the Midlands as an advantage
- Always end by capturing: name, email, and phone number (optional)

Start by greeting them and asking what industry they're in.
"""

@chatbot_bp.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages and return GPT responses"""
    try:
        data = request.json
        messages = data.get('messages', [])
        
        if not messages:
            return jsonify({'error': 'No messages provided'}), 400
        
        # Add system prompt at the beginning
        full_messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + messages
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # Using the available model from environment
            messages=full_messages,
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_message = response.choices[0].message.content
        
        return jsonify({
            'message': assistant_message,
            'success': True
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': str(e), 'success': False}), 500


@chatbot_bp.route('/api/save-lead', methods=['POST'])
def save_lead():
    """Save lead information"""
    try:
        data = request.json
        
        # In a real implementation, save to database or send email
        # For now, just log it
        print("=" * 50)
        print("NEW LEAD CAPTURED:")
        print(f"Name: {data.get('name')}")
        print(f"Email: {data.get('email')}")
        print(f"Phone: {data.get('phone', 'Not provided')}")
        print(f"Industry: {data.get('industry')}")
        print(f"Company Size: {data.get('companySize')}")
        print(f"Pain Points: {data.get('painPoints')}")
        print(f"Conversation: {data.get('conversation', [])}")
        print("=" * 50)
        
        # TODO: Send email notification or save to CRM
        
        return jsonify({
            'success': True,
            'message': 'Lead saved successfully'
        })
        
    except Exception as e:
        print(f"Error saving lead: {str(e)}")
        return jsonify({'error': str(e), 'success': False}), 500

