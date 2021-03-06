import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['mp3'])
music_files = []
music_files_number = 0

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation


@app.route('/')
def index():
    global music_files, music_files_number
  #  music_files= [f for f in os.listdir('uploads/') if f.endswith('mp3')]
   # music_files_number = len(music_files)

    return render_template('index.html',
                           title='Home',
                           music_files_number=music_files_number,
                           music_files=music_files,
                           ip_addr=request.remote_addr)






@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    global music_files,music_files_number
#    music_files=[f for f in os.listdir('uploads/') if f.endswith('mp3')]
 #   music_files_number = len(music_files)

    file = request.files['file']
    print(type(file))
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        music_files.append(filename)
        music_files_number += 1

        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return render_template('index.html',
                               title='Home',
                               music_files_number=music_files_number,
                               music_files=music_files,
                               ip_addr=request.remote_addr)
        # return redirect('index.html')#url_for('uploaded_file',
        #filename=filename))


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/musicfile/', methods=['GET'])
def musicfile():
    global music_files_number,music_files
    ret_data = {"music_files_number": music_files_number, "hell": "ji"}
    x=""
    for i in range(music_files_number):
        x+=music_files[i]+"$$##"

    ret_data["music_files"]=x

    return jsonify(ret_data)



if __name__ == '__main__':
    app.run(

        host="0.0.0.0",
        port=int("8080"),
        debug=True
    )

