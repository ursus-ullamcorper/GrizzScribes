# GrizzScribes
Turns your notes and class recordings into a summarized version of notes and study flashcards
![](https://media.discordapp.net/attachments/1215079325464789083/1216242535006212216/blob.jpg?ex=65ffad21&is=65ed3821&hm=be1d782ae805f82484edaf7d42ed3b8db1597b6221f44cec35c28e8f72de8d9b&=&format=webp)
## Quickstart
Make sure to run the command in the root directory: pip install -r requirements.txt 
Run the appy.py in the flask_app folder.
Then run the Grammorly.html in the root folder

*P.S. We too lazy to chage the original name*

## Inspiration
As University Students, we really wanted to make something dedicated to helping Oakland University Students to be able to do better and be more efficient in their education. From this, we decided to build a study tool to help convert our notes & class material to an easily readable/studyable format.
## What it does
Our web app is like a converter - we take in all types of files ranging from recorded videos to PDF documents to Powerpoint presentations and convert it into a downloadable markdown document & study flash cards that students can use to help them study.
## How we built it
![](https://cdn.discordapp.com/attachments/1215079325464789083/1216399312934932622/image.png?ex=66003f23&is=65edca23&hm=700709305e852e12d2856666b30ada654adf7dd229390f8e2749fdf3eb2a1cfc&)
OCR = Optical Character Recognition
Acceptable file types: mp3,mp4,pdf,docx,doc,pptx,txt files.
## Development Process
We took in the common file types and used a library called Apache Tika and Open AI's Whisper model to convert all these file types into a text file. From here, we used the ChatGPT api to convert it into MD notes and a JSON file for questions and answers. Then, going in on to our front-end, we dynamically create a new MD file with the MD notes, link it to the downloadable link, and dynamically use the JSON file to make the flash cards.
## What's next for Grizzscribes?
I've got to say, overall grinding out this hackathon overnight, we made a great effort building and debugging everything, there were a few features that we wanted to implement that we were not able to get to. Some of these features are:
- Voice generated notes
- Login Feature to store past notes
- Different note-taking models (hugging face's library took too long to convert)
- Turning the web into an executable application