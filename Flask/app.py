from flask import Flask,render_template
from flask_restful import Api,Resource 
app = Flask(__name__)
api = Api(app)

# get API
class HelloWorld(Resource):
	def get(self, name):
		return {"Hello": name }
	def post(self):
		return {'Post' : 'Posted'}

api.add_resource(HelloWorld,'/helloWorld/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)