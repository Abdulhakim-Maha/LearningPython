from flask import Flask,template_rendered
from flask_restful import Api,Resource,abort,reqparse
import Dummy_list
import Q
app = Flask(__name__)
api = Api(app)

#Request Parser
list_post_args = reqparse.RequestParser()
list_post_args.add_argument('id', type=int, help='Id of music')
list_post_args.add_argument('title',type=str, help='Name of music')
list_post_args.add_argument('artist',type=str, help='Artist of this music')

# get API
class HelloWorld(Resource):
	def get(self):
		if q.isEmpty(): abort(404,message='No List') 
		return q.dequeue() 
	def post(self):
		args = list_post_args.parse_args()
		q.enqueue(args)	
		print(q)	
		return {'message': 'added'},201
		
api.add_resource(HelloWorld,'/getMusic')

@app.route('/')
def hello():
	return template_rendered('about.html')

if __name__ == '__main__':
	q = Q.Queue()
	inp = Dummy_list.music_list
	for i in inp:
		q.enqueue(i)
	# print(q)
	app.run(debug=True)
