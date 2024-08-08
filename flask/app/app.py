from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file:
            # Save the uploaded file to the filesystem
            filename = secure_filename(file.filename)
            if not filename.endswith('.cc'):  # Ensure it's a .cc file
                return "Only .cc files are allowed"
            filepath = os.path.join('uploads', filename)
            file.save(filepath)

            # Compile the uploaded C++ program
            compile_command = ['g++', '-o', filepath + '.out', filepath]
            compile_result = subprocess.run(compile_command, capture_output=True, text=True)
            if compile_result.returncode != 0:  # Compilation error
                return render_template('result.html', compile_errors=compile_result.stderr)

            # Execute the test script and capture the output
            os.chmod('test.sh', 0o755)  # Make sure the test script is executable
            test_result = subprocess.run(['./test.sh'], capture_output=True, text=True)
            score = int(test_result.stdout.strip()) if test_result.stdout.strip().isdigit() else 0

            # Read the source code from the uploaded file for display
            with open(filepath, 'r') as file:
                source_code = file.read()

            # Render the results template
            return render_template('result.html', score=score, source_code=source_code, compile_errors=None)

    # If not a POST request, or no file was uploaded, show the upload form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

