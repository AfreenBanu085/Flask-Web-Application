from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h1>Welcome to Home Page</h1>'

@app.route('/regex', methods=['GET','POST'])
def add_fun():
    if request.method == 'POST':
        text = str(request.form.get('text'))
        pattern = str(request.form.get('pattern'))
        c = []
        c.extend(re.findall(pattern,text))
        d = int(len(c))
        if text == '' or pattern == '': 
            return render_template('about.html')   
            
        else:
            return render_template('result.html', c = c, d = d)

    return render_template('about.html')

@app.route('/about')
def hello():
     return 'about page'


if __name__ == '__main__':
    app.run(debug=True)
