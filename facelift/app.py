from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Setup the Flask app
app = Flask(__name__)
app.debug = True

# Configure file upload path
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ROUTING AND APP METHODS -----------------------------------------------------

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route('/images/<path:path>')
@app.route('/assets/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

def adversarifier(path_base, path_attack):
    '''
    Returns a path to an image with the the adverserial NN applied to it
    :param path_one: A path to the base image
    :param path_two: A path to the attack image
    '''
    
    pass
    
# UPLOAD AND TASK METHODS -----------------------------------------------------

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/postImage', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submits a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'a').close()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run()
