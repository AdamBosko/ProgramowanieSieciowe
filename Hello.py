from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/test")
def test():
    return "Test/Hello_World/Test"

@app.route("/suma")
def suma():
    a = 5
    b = 7
    return str(a + b)
	
@app.route("/iloczyn")
def iloczyn():
    a = 10
    b = 2
    return str(a * b)
	
if __name__ == '__main__':
    app.run()