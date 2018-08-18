import zipfile
import io
import os
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/downloadfiles')
def download():
    os.chdir(r"Files")

    data = io.BytesIO()
    with zipfile.ZipFile(data, mode='w') as z:
        for file_name in os.listdir('.'):
            z.write(file_name)
    data.seek(0)

    os.chdir(r"..")
    
    return send_file(data, mimetype="application/zip", attachment_filename = "website_blocker.zip", as_attachment = True)

@app.route('/data', methods=['POST'])
def savedata():
    if request.method == 'POST':
        initial_hour = request.form.get("first_hour")
        final_hour = request.form.get("last_hour")
        url = request.form.getlist("url")
        list_arguments = [initial_hour, final_hour, url]

    os.chdir(r"Files")

    with open("data.txt", "r+") as file:
        file.truncate()
        for argument in list_arguments:
            file.write("%s\n" % argument)

    os.chdir(r"..")

    return download()

if __name__ == '__main__':
    app.run(debug=True)