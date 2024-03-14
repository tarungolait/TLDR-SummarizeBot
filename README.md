# Text Summarizer Bot with Sentiment Analysis

This repository contains a Telegram bot that utilizes the Cohere API for text summarization and TextBlob library for sentiment analysis. The bot is designed to receive text inputs, summarize them, and provide sentiment analysis of the input text. Below are the steps to set up and use the bot:

## How to Use

1. **Obtain API Keys**: 
   - Sign up for an account on [Cohere's website](https://cohere.ai/).
   - Navigate to the API Key section in your account settings.
   - Generate an API key if you don’t have one already.
   - Copy the generated Cohere API key.

2. **Create a Telegram Bot Using BotFather**:
   - Open the Telegram app and search for BotFather.
   - Start a chat with BotFather and follow the instructions.
   - Use the `/newbot` command to create a new bot.
   - Provide a name and username for your bot.
   - Copy the generated Telegram bot token.

3. **Environment Setup**:
   - Make sure you have Python installed on your machine.
   - Create a new Python project and install the required dependencies: `cohere`, `telebot`, `textblob`, and `python-dotenv`.

4. **Initialize the Cohere Client and Telegram Bot**:
   - Replace `"COHERE-API-KEY"` with your actual Cohere API key.
   - Replace `"TELEGRAM-BOT-TOKEN"` with your Telegram bot token.

5. **Handle Incoming Messages**:
   - Define a message handler function to extract text from incoming messages.

6. **Use Cohere for Text Summarization**:
   - Inside the message handler, utilize the Cohere API to summarize the text.
   - Wrap the summarization code in a try-except block to handle errors.

7. **Start the Telegram Bot**:
   - Add the code to start the Telegram bot and begin polling for incoming messages.

## Repository Contents

- `app.py`: Python script containing the implementation of the Telegram bot.
- `.env.example`: Example environment file template.
- `README.md`: Instructions on how to set up and use the bot.

## Usage

1. Clone this repository to your local machine.
2. Rename `.env.example` to `.env` and fill in your API keys.
3. Install the required Python dependencies using `pip install -r requirements.txt`.
4. Run the bot script using `python app.py`.
5. Interact with the bot by sending text messages to the Telegram bot.

## Contributors

- [Tarun Golait](https://github.com/tarungolait) - Creator and maintainer.

