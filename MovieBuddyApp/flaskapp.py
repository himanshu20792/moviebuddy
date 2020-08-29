from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/findsimilar")
def findsimilar():
    return render_template('findsimilar.html')

@app.route("/wordcloud")
def findsimilar():
    return render_template('wordcloud.html')

if __name__ == '__main__':
    app.run(debug=True)