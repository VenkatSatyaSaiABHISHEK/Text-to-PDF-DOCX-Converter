from flask import Flask, render_template, request, send_file
from utils import create_docx, create_pdf
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    format_type = request.form['format']
    if format_type == 'pdf':
        file_path = create_pdf(text)
    else:
        file_path = create_docx(text)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
