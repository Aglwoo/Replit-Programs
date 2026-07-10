# author: Giorgio
# date: 19.03.2024
# topic: TikTok-Voice-TTS
# version: 1.1

import argparse

# the script in the directory
import tiktokvoice
from gtts import gTTS
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.editor import VideoFileClip, vfx, afx, AudioFileClip, concatenate_videoclips
import random
from pydub import AudioSegment
language = "en"
def vid():

    t1 = 1
    t2 = 20
    vid = random.randint(1,4)
    
    clip = VideoFileClip(str(vid)+".mp4").subclip(t1,t2).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    clip  = clip.rotate(90)
    audio = AudioFileClip("output.mp3").fx(afx.audio_fadein, 0.5)
    audio = audio.volumex(0.1)
    combined = concatenate_videoclips([clip])
    combined.audio = CompositeAudioClip([audio])
    combined.write_videofile("output.mp4")

def main():
#opening txt
    file = open("hi.txt", "r")
    text = file.read()
    print(text)
    print("Running")
    tiktokvoice.tts(text, "en_male_narration", "output.mp3", play_sound=False)
    vid()


if __name__ == "__main__":
    main()
