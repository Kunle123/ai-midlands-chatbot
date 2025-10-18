# AI Midlands Chatbot

GPT-powered chatbot for lead qualification and demonstration of AI automation capabilities.

## Features

- 🤖 GPT-4 powered conversational AI
- 💼 Industry-specific recommendations (Property Management, Law Firms, Accounting, Healthcare)
- 📊 ROI calculations and time savings estimates
- 📝 Lead capture functionality
- 🎨 Professional, mobile-responsive interface

## Tech Stack

- **Backend:** Flask (Python)
- **AI:** OpenAI GPT-4
- **Frontend:** HTML, CSS, JavaScript
- **Hosting:** Render

## Deployment

This chatbot is deployed on Render. See deployment documentation for details.

### Environment Variables Required

- `OPENAI_API_KEY` - Your OpenAI API key

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export OPENAI_API_KEY="your-api-key-here"

# Run the app
python -m src.main
```

Visit `http://localhost:5000` to test locally.

## Usage

### Standalone Link
Share the chatbot URL directly: `https://your-chatbot-url.onrender.com`

### Embed on Website
```html
<iframe 
  src="https://your-chatbot-url.onrender.com" 
  width="100%" 
  height="700px" 
  style="border: none; border-radius: 20px;"
></iframe>
```

## License

Private - AI Midlands © 2025

