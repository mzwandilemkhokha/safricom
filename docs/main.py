from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/link1')
def link1():
    return redirect('http://localhost:8501/')

@app.route('/link2')
def link2():
    return redirect('http://localhost:8501/')

@app.route('/link3')
def link3():
    return redirect('https://www.example.com/link3')

@app.route('/link4')
def link4():
    return redirect('https://www.example.com/link4')

@app.route('/link5')
def link5():
    return redirect('https://www.example.com/link5')

if __name__ == '__main__':
    app.run(debug=True)
