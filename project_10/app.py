
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

notes = []
@app.route('/About')
def about_me():
    import webbrowser
    webbrowser.open('https://www.linkedin.com/in/Afreen-Banu/')
    return 'https://www.linkedin.com/in/Afreen-Banu/'

@app.route('/projects')
def about_project():
    import webbrowser
    webbrowser.open('https://github.com/AfreenBanu085')
    return 'https://github.com/AfreenBanu085'
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'GET':
        notes.clear()

    elif request.method == 'POST':
        note = request.form.get("note")
        if note != '':
            notes.append(note)
        return render_template("notes.html", notes=notes)
        
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)