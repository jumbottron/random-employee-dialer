### Explanation

- **Import Libraries**:
  - `boto3`: AWS SDK for Python, used to interact with AWS services.
  - `random`: Python standard library for generating random numbers and making random selections.

- **Define `lambda_handler` Function**:
  - The entry point for the Lambda function, which AWS Lambda invokes with the `event` and `context` parameters.

- **Create DynamoDB Resource**:
  - `dynamodb = boto3.resource('dynamodb')`: Creates a DynamoDB resource object to interact with DynamoDB tables.

- **Access DynamoDB Table**:
  - `table = dynamodb.Table('Employees')`: Accesses the `Employees` table in DynamoDB.

- **Scan Table**:
  - `response = table.scan()`: Retrieves all items from the `Employees` table.

- **Extract Items**:
  - `employees = response['Items']`: Extracts the list of employee items from the scan response.

- **Handle No Employees**:
  - If no employees are found, the function returns a `404` status code with a message indicating that no employees were found.

- **Select Random Employee**:
  - `random_employee = random.choice(employees)`: Selects a random employee from the list.

- **Return Response**:
  - Returns a `200` status code and the randomly selected employee.
