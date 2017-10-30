from flask_restful import Resource
from manage import User

class sample(Resource):

	def get(self):
		return 'Test good'