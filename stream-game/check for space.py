
import requests
import json

# Enter your YouTube API key here
API_KEY = "YOUR_YOUTUBE_API_KEY"

# Enter your YouTube channel ID here
CHANNEL_ID = "YOUR_YOUTUBE_CHANNEL_ID"

# Enter your YouTube live chat ID here
LIVE_CHAT_ID = "YOUR_YOUTUBE_LIVE_CHAT_ID"

def get_live_chat_messages():
    url = f"https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId={LIVE_CHAT_ID}&part=snippet&key={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def check_for_space(messages):
    for message in messages:
        if 'space' in message['snippet']['displayMessage']:
            return True
    return False

def play_game():
    while True:
        messages = get_live_chat_messages()['items']
        if check_for_space(messages):
            print("Space mentioned in chat!")
            # Add your game logic here
            break

if __name__ == '__main__':
    play_game()