from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def add():
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)
    if x is None or y is None:
        return "Please provide both x and y parameters", 400
    c = x + y
    return str(c)

if __name__ == '__main__':
    app.run()

