from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
	return "Hello world\n"

if __name__ == '__main__':
	app.run(port=8080)


