from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Saurabh Powar',
        'title' : 'asjd',
        'content' : 'asdcsvc',
        'lov' : 'sp'
    },
    {
        'author': 'Sauraxd scbh Powar',
        'title' : 'sjddcdsac',
        'content' : 'scxsaxa',
        'lov' : 'psdsc'
    }
]

@app.route('/')
def root():
    return '<h1> Heyy! </h1>'

@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)