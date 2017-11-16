import os
import time
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from styling import *

UPLOAD_FOLDER = 'images'
BASE_TEMPLATE_NAME = 'index.html'

app = Flask(
    __name__, 
    template_folder = 'templates', 
    static_folder = 'images'
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template(BASE_TEMPLATE_NAME)
    if request.method == 'POST':
        image = request.files['img']
        if image.filename == '':
            return redirect('/')
        if image and allowed_file(image.filename):
            timestamp = int(time.time())
            name = os.path.splitext(image.filename)[0]
            ext = os.path.splitext(image.filename)[1]
            filename = UPLOAD_FOLDER + '/' + secure_filename(name + '_' + str(timestamp)  + ext)
        else:
            return str(ALLOWED_EXTENSIONS) + ' are only allowed'
        image.save(filename)  
        link = process_image(filename)
        return render_template(BASE_TEMPLATE_NAME, link = link) 
    
@app.route('/')
def render_images():
    return '<img src=' + url_for(RESULT_FOLDER) + '>' 

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0', port = 8080 
    )