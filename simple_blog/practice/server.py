from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    blog_response = requests.get(url="https://api.npoint.io/b52f715e3c34aca88574")
    blog_posts = blog_response.json()
    return render_template('blog.html', blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)