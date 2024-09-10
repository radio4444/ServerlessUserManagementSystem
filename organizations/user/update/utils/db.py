from pymongo import MongoClient


class MongoDBConnection:
	def __init__(self):
		self.connection = None

	def __enter__(self):
		self.connection = MongoClient(
			"mongodb+srv://Radio4444:ma0bx3HMnp4xcicE@mydb.qblqq.mongodb.net/?retryWrites=true&w=majority&appName=myDB")
		# Have the client URL in different file. And add it in .gitignore file

		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.connection.close()
