from flask import Flask
app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1 style = "text-align: center"> Hello This is Flask Starting Project</h1>'\
            '<p>This is a paragraph.</p>'\
            '<img src = "https://media.tenor.com/UXYgWuJjM4wAAAAM/i-spotted-a-dinosaur-on-the-loose-kohli.gif" width = 600, height = 600>' 



if __name__ == "__main__":
    app.run(debug=True)