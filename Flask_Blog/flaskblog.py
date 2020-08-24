from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Himanshu Agarwal',
        'title': 'How to rule the world',
        'content': 'Ya .. really !!',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ty Schnettler',
        'title': 'Boring post',
        'content': 'Watching plants grow',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)