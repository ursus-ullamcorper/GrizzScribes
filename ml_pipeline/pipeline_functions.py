from openai import OpenAI
from tika import parser
from moviepy.editor import *

client = OpenAI()

def speech_to_text(file_path):
    audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",  
        file=audio_file
    )
    return transcription.text


def extract_text_from_file(file_path):
    # Parse the PDF and extract the raw text content
    raw_text = parser.from_file(file_path) 

    # Print the extracted text 
    return raw_text['content']

def mp4_to_mp3(file_path):
    # Specify the filename of the resulting MP3 file
    mp3_file_path = f'#{file_path[:-4]}.mp3'

    # Load the video file
    video_clip = VideoFileClip(file_path)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio data to the MP3 file
    audio_clip.write_audiofile(mp3_file_path)

    # Close the clips
    audio_clip.close()
    video_clip.close()

    return mp3_file_path

def generate_summary(text, type):
    if type == 'md':
        prompt = "Convert this text into a summary as class notes in markdown code: "
    elif type == 'qa':
        prompt = """
        Given these class notes, I want you to generate a JSON output for students to use as flashcards. They should be a list of items of
        the form {"question" : <QUESTION>,  "answer" : <ANSWER>}: 
        """

    prompt += text

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt} 
        ]
    )
    return completion.choices[0].message.content