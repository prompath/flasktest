from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'What\'s up fucker!'

if __name__ == '__main__':
    app.run()