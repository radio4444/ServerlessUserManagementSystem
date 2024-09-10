# Serverless User Management System

This project is a serverless user management system built with AWS SAM CLI, Python, and MongoDB. It includes Lambda functions for CRUD operations and user authentication, with API Gateway integration and testing setup.

## Project Overview

This application provides a set of Lambda functions for managing user data and authentication. The project utilizes AWS SAM for deployment, MongoDB for data storage, and includes test cases for validating the functionality of the APIs.

## Features

- **User Registration**: Lambda function to register users with validation and storage in MongoDB.
- **User Management**: CRUD operations to create, read, update, and delete user data.
- **Authentication**: Custom JWT authorizer for securing API endpoints and managing user login sessions.
- **Token Management**: Lambda functions for creating and refreshing JWT tokens.

## Project Structure

- `organizations/user/`
  - `create/`
    - `app.py`: Handles user registration.
  - `read/`
    - `app.py`: Retrieves user information.
  - `update/`
    - `app.py`: Updates user information.
  - `delete/`
    - `app.py`: Deletes user information.
  - `login/`
    - `app.py`: Manages user login and token creation.
    - `token.py`: Functions for creating and refreshing JWT tokens.
    - `validator.py`: User login and token validation schemas.
  - `authorizer/`
    - `app.py`: Custom JWT authorizer for API Gateway.

- `tests/unit/`
  - `test_handler.py`: Contains pytest-based tests for the registration API.

- `template.yaml`: AWS SAM template defining the serverless application resources.

## Deployment

1. **Deploy the Application**:
   - Right-click on the `template.yaml` and select "Sync Serverless Application".
   - Follow the prompts to create the stack and S3 bucket, and deploy the application.

2. **Test the Functions**:
   - Use AWS Lambda test events to validate individual functions.
   - Test API endpoints using Postman by retrieving the invoke URL from API Gateway and adding necessary information.

## Setup

1. **MongoDB**:
   - Ensure MongoDB is set up and connected to your development environment.

2. **Dependencies**:
   - Ensure you have the required Python packages installed. Refer to `requirements.txt` for a list of dependencies.

## Testing

- **Unit Tests**:
  - Run tests using pytest to ensure functionality is as expected.

## Notes

- **Security**: Ensure the `SECRET_KEY` environment variable is configured properly for JWT encryption and decryption.
- **Cleanup**: The `teardown` method in the tests removes the last inserted user from the MongoDB collection after tests.

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

