import datetime
import os
import jwt

from marshmallow import ValidationError


# Function one: Creating new JWT token
# Function two: Refresh the token, which we used to generate a new token
#   based on previous token validity until it hasn't expired

def create_access_token(result):
	# Returns new JWT token
	jwt_info = jwt.encode({
		"id": str(result["_id"]),
		"first_name": str(result["first_name"]),
		"last_name": str(result["last_name"]),
		"exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=300),
	}, os.environ['SECRET_KEY'])
	# Token is valid for 5 minutes
	return jwt_info


def refresh_token(token):
	# Refresh Token if the token has expired
	try:
		result = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=["HS256"])
		jwt_info = jwt.encode(
			{**result, "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=300)},
			os.environ['SECRET_KEY'])
		# Token is valid for 5 minutes
		return {
			"status": True,
			"data": jwt_info,
			"message": None
		}
	except jwt.exceptions.DecodeError:
		return {
			"status": False,
			"data": None,
			"message": "Unable to decode data!"
		}
	except jwt.ExpiredSignatureError:
		return {
			"status": False,
			"data": None,
			"message": "Token has expired !"
		}
