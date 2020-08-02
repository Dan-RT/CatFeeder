from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/feed')
def hello_world():
    return { "message:" : "Cat fed!" }


if __name__ == '__main__':
    app.run()
