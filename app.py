from flask import Flask

app = Flask(__name__)
host_addr = "0.0.0.0"
host_port = 5000

@app.route('/')
def hello():
    return "hello world"

@app.route('/test')
def ping():
    return {'response': 'test'}


if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)