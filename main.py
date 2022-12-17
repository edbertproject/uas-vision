import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

from Comparation import compare_percentage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/upload'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            file_name = secure_filename(file.filename)
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], file_name))
            file_url = url_for('static', filename='upload/' + file_name)
            max_number, max_percentage, percentages = compare_percentage("static/upload/" + file_name)
            return render_template('index.html', rendered_image=file_url, max_number=max_number, max_percentage=max_percentage, percentages=percentages)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
