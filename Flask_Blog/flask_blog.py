from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return '<h1> Heyy! </h1>'

@app.route('/home')
def home():
    return '<h1> Hello, SP! </h1>'


@app.route('/about')
def about():
    return '<h1> About page! </h1>'

if __name__ == '__main__':
    app.run(debug=True)