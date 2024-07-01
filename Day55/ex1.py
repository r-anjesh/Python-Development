from flask import Flask
app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Write your name in url "/anjesh"'

@app.route('/<path:username>/')
def greet(username):
    return f'Hello {username}'


if __name__ == "__main__":
    app.run(debug=False)