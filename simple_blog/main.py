from flask import Flask, render_template
import requests

def retrieve_blogs():
    blog_response = requests.get(url="https://api.npoint.io/b52f715e3c34aca88574")
    blog_posts = blog_response.json()
    return blog_posts

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = retrieve_blogs()
    return render_template("index.html", blog_posts=blog_posts)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    blog_posts = retrieve_blogs()
    for blog_post in blog_posts:
        if blog_post['id'] == blog_id:
            requested_post = blog_post 
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)