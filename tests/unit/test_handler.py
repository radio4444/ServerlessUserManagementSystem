import json
import time
import pytest

from organizations.user.create import app
from .testing_db import db


@pytest.fixture()
def fixture_event():
	return {
		"body": "{\"first_name\": \"John\", \"last_name\": \"Samson\", \"email\": \"johnsamson" + str(
			time.time_ns()) + "@gmail.com\", \"password\": \"johnSamson1234\"}"
	}


class TestRegistrationAPI:
	def test_lambda_handler(self, fixture_event):
		ret = app.lambda_handler(fixture_event, "")
		data = json.loads(ret["body"])
		assert ret["statusCode"] == 201
		assert "message" in ret["body"]
		assert data["message"] == "Registered Successfully", "Registered failed"

	def teardown(self):
		mongo = db.MongoDBConnection()
		with mongo:
			database = mongo.connection['myDB']
			collection = database['registration']

		# Get last inserted id
		queryset = collection.find().sort([("_id", -1)]).limit(1)
		for result in queryset:
			result_id = result["_id"]

		# drop last inserted id
			collection.delete_one({"_id": result_id})
