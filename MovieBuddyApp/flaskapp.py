from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://search.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///https://github.com/himanshu20792/moviebuddy/blob/master/MovieBuddyApp/search.db'
# Initialize the database
db = SQLAlchemy(app)

# Create db model
class search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(200), nullable=False)
    wc_drop_down_name = db.Column(db.String(200), nullable=False)
    wc_picture_type = db.Column(db.String(200), nullable=False)

    # Create a funtion to return a string when we add something
    def __repr__(self):
        return '<wc_picture_type %r>' % self.search_term 
    
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/findsimilar")
def findsimilar():
    return render_template('findsimilar.html')

@app.route("/wordcloud")
def wordcloud():
    return render_template('wordcloud.html')

if __name__ == '__main__':
    app.run(debug=True)