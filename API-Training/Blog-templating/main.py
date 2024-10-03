from flask import Flask, render_template
import requests

app = Flask(__name__)

response  = requests.get(" https://api.npoint.io/99b573803f564b593d1d")
data = response.json()

@app.route('/')
def home(dat = data):
    return render_template("index.html",data = data)

@app.route('/post/<int:id>')
def posts(id):
    # Find the post with the matching id
    for post in data:
        if post['id'] == id:
            return render_template("post.html", post=post)
    # If post not found, return an error message
    return "Post not found"

    

if __name__ == "__main__":
    app.run(debug=True)
