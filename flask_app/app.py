from flask import Flask, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
import sys
import json

from celery import Celery

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ml_pipeline')))
from pipeline_functions import *

app = Flask(__name__)
app.secret_key = 'secret_key'  # Needed for flash messages

# Directory where uploaded files will be stored
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Celery for processing jobs
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

app.config.update(
    CELERY_BROKER_URL='url_to_your_broker',
    CELERY_RESULT_BACKEND='url_to_your_backend'
)
celery = make_celery(app)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'mp3', 'pdf', 'doc', 'docx', 'txt', 'pptx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # return redirect(url_for('upload_file', filename=filename))
            return pipeline_process(file_path)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def pipeline_process(file_path):
    extension = file_path.split('.')[-1]
    if extension == 'mp4':
        file_path = mp4_to_mp3(file_path)
        extension = 'mp3'
    
    if extension == 'mp3':
        transcription = speech_to_text(file_path)
    else:
        transcription = extract_text_from_file(file_path)

    summary = generate_summary(transcription, 'md')
    flashcards = json.loads(generate_summary(transcription, 'qa'))
    
    summary_file_path = file_path[: - len(extension)] + 'md'
    with open(summary_file_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(summary)

    filename = summary_file_path.split('/')[-1]
    summary_download_url = url_for('download_file', filename=filename, _external=True)

    return {
        'markdown_download_url': summary_download_url,
        'flashcards': flashcards
    }
 
@app.route('/download/<filename>')
def download_file(filename):
    directory = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create directory if it doesn't exist
    app.run(debug=True)
