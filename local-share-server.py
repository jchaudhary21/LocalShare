from flask import Flask, request, redirect, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static')
UPLOAD_FOLDER = '/home/jc/Desktop/advanceCopyPaste/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CONTENT_FILE = 'content.txt'

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    content_path = os.path.join(app.config['UPLOAD_FOLDER'], CONTENT_FILE)
    if os.path.exists(content_path):
        with open(content_path, 'r') as file:
            content = file.read()
    else:
        content = ''
    return render_template('index.html', files=files, content=content)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect('/')

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect('/')

@app.route('/clear')
def clear_files():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return redirect('/')

@app.route('/save', methods=['POST'])
def save_file():
    content = request.form['content']
    content_path = os.path.join(app.config['UPLOAD_FOLDER'], CONTENT_FILE)
    with open(content_path, 'w') as file:
        file.write(content)
    return redirect('/')

if __name__ == '__main__':
    print("Flask app is running on http://{}:{}".format('192.168.1.6', 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)
