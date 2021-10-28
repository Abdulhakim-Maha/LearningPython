from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/user/<name>')
def home(name):
	return '<h1>Hello {}'.format(name)

@app.route('/hello')
def hello():
	return '<div>Welcome to my website</div>'
	

if __name__ == '__main__':
	app.run(debug=True)