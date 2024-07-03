import time

from flask import Flask
app = Flask(__name__)
def sleep_decorator(function):
    def wrapper_funtion():
        time.sleep(2s)
        function()
        return wrapper_funtion

@app.route('/')
def home_page():
    return 'Write your name in url "/anjesh"'

@app.route('/<path:username>/')
def greet(username):
    return f'Hello {username}'

@sleep_decorator
def demo():
    print("this function implemented after 2 seconds")

if __name__ == "__main__":
    app.run(debug=False)