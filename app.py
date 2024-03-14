import os
import telebot
import cohere
from textblob import TextBlob
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
API_KEY_COHERE = os.getenv("COHERE_API_KEY")
API_KEY_TELEGRAM = os.getenv("TELEGRAM_BOT_API_KEY")

# Create a Cohere client instance
co = cohere.Client(API_KEY_COHERE)

# Create a Telegram bot instance
bot = telebot.TeleBot(API_KEY_TELEGRAM)

# Introduction message for the bot
intro_message = """
🤖 Welcome to the Text Summarizer Bot with Sentiment Analysis! 📝

I'm here to help you summarize long texts into concise and easy-to-read summaries, and I can also analyze the sentiment of your text.

Here's how to use me:
1️⃣ Simply send me any text you want to summarize.
2️⃣ I'll analyze it and generate a summary for you.
3️⃣ You'll receive the summary along with the sentiment analysis.

Don't hesitate to try me out! Start summarizing your texts now by sending them over. If you have any questions or need assistance, feel free to ask. Happy summarizing! 🚀
"""

# Define a handler for the "/start" command
@bot.message_handler(commands=['start'])
def send_intro_message(message):
    bot.send_message(message.chat.id, intro_message)

# Define a handler for incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Get the text from the incoming message
    text = message.text

    try:
        # Use Cohere to summarize the text
        response = co.summarize(
            text=text,
            length='auto',
            format='auto',
            model='summarize-xlarge',
            additional_command='',
            temperature=0.3,
        )

        # Get the summary from the response
        summary = response.summary

        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment

        # Interpret sentiment
        if sentiment.polarity > 0:
            sentiment_label = "Positive"
        elif sentiment.polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        # Send the summary and sentiment analysis as a reply
        bot.reply_to(message, f"Summary: {summary}\n\nSentiment: {sentiment_label}")

    except Exception as e:
        # Log the error message
        print("Error:", str(e))

        # Handle any errors that occur during summarization
        bot.reply_to(message, "Oops! Something went wrong.")

# Start the Telegram bot
bot.polling()
