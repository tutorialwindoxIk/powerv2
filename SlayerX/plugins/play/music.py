import logging
from pyrogram import Client, filters
import requests

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your actual credentials
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'


# Initialize the Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function to connect to the 9xm API and retrieve song data
def get_song_data():
    # Replace 'YOUR_9XM_API_ENDPOINT' with the actual 9xm API endpoint
    url = "https://d75dqofg5kmfk.cloudfront.net/bpk-tv/9XM/default/9XM-audio_208482_und=208000-video=2137600.m3u8"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        # This URL returns an m3u8 file, not JSON
        return response.text
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None

# Define a function to play the song on the Telegram bot
def play_song(client, message):
    song_data = get_song_data()
    if song_data:
        # Replace 'YOUR_SONG_AUDIO_URL' with the actual URL of the song audio
        song_audio_url = "https://d75dqofg5kmfk.cloudfront.net/bpk-tv/9XM/default/9XM-audio_208482_und=208000-video=2137600.m3u8"
        
        try:
            # Send the audio file
            client.send_voice(chat_id=message.chat.id, voice=song_audio_url)
        except Exception as e:
            logging.error(f"Audio file sending failed: {e}")
            message.reply_text("Failed to send audio file.")
    else:
        message.reply_text("Failed to retrieve song data.")


# Define a command handler to play the song
@app.on_message(filters.command("song"))
def play(client, message):
    play_song(client, message)

# Run the bot
if __name__ == "__main__":
    app.run()
