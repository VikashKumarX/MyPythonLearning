# pip install flask python-docx pdf2docx 
from flask import Flask, request, render_template
from docx import Document
from pdf2docx import Converter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        # Save the uploaded Word document
        doc_filename = secure_filename(file.filename)
        doc_path = os.path.join(app.config['UPLOAD_FOLDER'], doc_filename)
        file.save(doc_path)

        # Convert Word to PDF
        pdf_filename = f"{os.path.splitext(doc_filename)[0]}.pdf"
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
        
        try:
            # Open the Word document
            doc = Document(doc_path)

            # Save as PDF using pdf2docx library
            cv = Converter(doc_path)
            cv.convert(pdf_path, start=0, end=None)
            cv.close()

            return send_from_directory(app.config['UPLOAD_FOLDER'], pdf_filename, as_attachment=True)

        except Exception as e:
            return str(e)

    else:
        return 'Invalid file format'

if __name__ == '__main__':
    app.run(debug=True)
