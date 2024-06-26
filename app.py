from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return f'IP Address: {request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)}, Port: {request.environ["SERVER_PORT"]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
