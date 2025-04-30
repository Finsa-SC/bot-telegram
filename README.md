# Telegram Bot

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> *Telegram bot with Telegram*

---

## 📜 About This Bot

This bot is a smart AI assistant that is implemented as a Telegram bot. It uses a model from Ollama to provide a natural and useful response. 

## ✨ Features

- 💬 **Natural Interaction** - Communicates with users using natural language and understands conversation context
- 🏠 **Locally Hosted** - Uses Ollama to run the OpenChat model locally, enhancing privacy and security
- 🤖 **Different Personality** - You can replace personality change by using a prompt
- ⚡ **Quick Responses** - Optimized to provide responses in minimal time

## 🔧 Technologies Used

- **Python** - Primary programming language
- **python-telegram-bot** - Library for integrating with the Telegram API
- **Ollama** - Framework for running AI models locally
- **OpenChat** - Large language model used as Fairy's brain

## 🚀 Getting Started

### Prerequisites

1. Python 3.8 or newer
2. Ollama installed and running on the local machine
3. telegram token

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/username/fairy-bot.git
   cd fairy-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Ollama is installed and running on the default port (11434):
   ```bash
   ollama serve
   ```

4. Pull the OpenChat model:
   ```bash
   ollama pull openchat:latest
   ```
   I recommend it because I use it too

### Configuration

If you want to customize the bot, edit the following variables in the `main.py` file:
- `TELEGRAM_TOKEN` - Your Telegram bot token (from BotFather)
- `OLLAMA_URL` - The Ollama API endpoint URL
- `MODEL` - The model you want to use
- `SYSTEM_PROMPT` - System instructions to define the bot's persona

### Running the Bot

```bash
python main.py
```

The bot will be active and ready to receive messages! Open Telegram and start chatting with Fairy.

## 🛠️ Code Structure

```
fairy_bot.py             # Main application file
├── TELEGRAM_TOKEN       # API token for Telegram bot
├── OLLAMA_URL           # URL for communicating with Ollama API
├── MODEL                # AI model used (openchat:latest)
├── SYSTEM_PROMPT        # Definition of bot's personality and role
├── chat_with_ollama()   # Function for communicating with Ollama model
└── handle_message()     # Handler for incoming user messages
```

## 💡 Customization

You can customize Fairy's personality by changing the `SYSTEM_PROMPT`. For example:

```python
SYSTEM_PROMPT = "Your name is Fairy. You are a cheerful and enthusiastic assistant who enjoys helping users with information and support. You were created by Master Finsa and serve as his replacement when he's not available."
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" alt="Python Logo" width="100"/>
  <img src="https://ollama.com/public/ollama.png" alt="Ollama Logo" width="70"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram Logo" width="70"/>
</p>

- Thanks to [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the amazing bot framework
- Thanks to [Ollama](https://github.com/ollama/ollama) for enabling local AI model hosting
- Thanks to [OpenChat](https://github.com/openchat-ai/openchat) for the powerful language model

---

<p align="center">
  Made with ❤️ by Master Finsa
</p>