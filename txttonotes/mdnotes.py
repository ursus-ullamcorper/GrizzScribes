import os
from dotenv import load_dotenv
import openai
from openai import OpenAI
load_dotenv()
convertType = "qa"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
client = OpenAI()

def get_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt} 
        ]
    )
    return completion.choices[0].message.content

# Get the prompt from the user
user_prompt = input("Enter your prompt: ")

# Get the response using the prompt
if convertType == "md":
  response = get_response("Convert this text into a summary as class notes in markdown code: " + user_prompt)
elif convertType == "qa":
   response = get_response("Given these class notes, I want you to generate a JSON file to help the user study for an exam based off these notes: " + user_prompt)
else:
   print("error")

# Print the response
print(response)