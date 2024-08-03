from pytube import YouTube
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'defaultsecretkey')
# app.config['UPLOAD_FOLDER'] = 'downloads'
DOWNLOAD_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')
app.config['UPLOAD_FOLDER'] = DOWNLOAD_FOLDER


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def videodownload(url, save_path):
    try:
        yt = YouTube(url)
        streams =  yt.streams.filter(file_extension='mp4', progressive=True)
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def mp3download(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True).first()
        streams.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods =['POST'])
def download():
    url = request.form['url']
    file_type = request.form['file_type']
    if not url:
        flash('URL is required!')
        return redirect(url_for('index'))
    
    save_path = app.config['UPLOAD_FOLDER']
    
    if file_type == 'mp4':
        message = videodownload(url, save_path)
    else:
        message = mp3download(url, save_path)
    
    flash(message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)