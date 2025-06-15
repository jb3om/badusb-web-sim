import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from badusb_emulator import run_emulator, TARGET_FILE

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'ino'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    file_content = None
    log_output = None

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            success, log_output = run_emulator(filepath)
            result = "✅ 공격 성공 (파일 변경됨)" if success else "❌ 공격 실패 (파일 미변경)"

            if os.path.exists(TARGET_FILE):
                with open(TARGET_FILE, 'r') as f:
                    file_content = f.read()

    return render_template('index.html', result=result, file_content=file_content, log_output=log_output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')