from flask import Flask

app = Flask(__name__)
env = "prod"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    if env is "dev":
        app.run()
    else:
        app.run(debug=False, host="0.0.0.0")
