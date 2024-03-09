from openai import OpenAI
from tika import parser


def speech_to_text(file_path):
    client = OpenAI()
    audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",  
        file=audio_file
    )
    print(transcription.text)



def extract_text_from_file(file_path):
    # Parse the PDF and extract the raw text content
    raw_text = parser.from_file(file_path) 

    # Print the extracted text 
    print(raw_text['content']) 