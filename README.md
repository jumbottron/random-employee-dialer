# Random Employee Dialer

This repository contains the code and setup instructions for a random employee dialer system using AWS services.

## Services Used

- AWS Lambda
- Amazon DynamoDB
- Amazon Connect
- Amazon API Gateway
- Amazon CloudWatch Events

## Setup Instructions

1. Create the DynamoDB table:
   - Table Name: Employees
   - Primary Key: EmployeeID (String)

2. Set up Amazon Connect:
   - Create an instance and configure an IVR.

3. Deploy Lambda functions:
   - `get_random_employee.py`: Fetches a random employee from DynamoDB.
   - `initiate_call.py`: Initiates a call using Amazon Connect.

4. Set up API Gateway:
   - Create resources and methods to trigger Lambda functions.

5. Schedule random calls using CloudWatch Events:
   - Use the provided event_rule.json to schedule Lambda triggers.

6. Configure IAM roles and permissions:
   - Ensure Lambda functions have necessary permissions.

## Deployment

1. Clone the repository.
2. Follow the setup instructions for each service.
3. Deploy the Lambda functions and API Gateway setup.
4. Schedule the CloudWatch Events rule.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.

