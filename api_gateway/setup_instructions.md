### API Gateway Setup Instructions

1. **Create a New API**:
   - Navigate to the [API Gateway Console](https://console.aws.amazon.com/apigateway).
   - Click on "Create API" and choose "HTTP API" or "REST API" based on your preference.
   - Follow the prompts to create a new API.

2. **Create Resource and Method for Fetching Random Employee**:
   - In the API Gateway console, select your API and go to the "Resources" section.
   - Click on "Create Resource" and enter a name for the resource (e.g., `/fetch-employee`).
   - Select the newly created resource and click on "Create Method".
   - Choose "POST" as the method type and click on the checkmark to confirm.
   - In the "Integration type" section, select "Lambda Function".
   - Enter the name of the Lambda function you created for fetching a random employee (`get_random_employee`).
   - Save and deploy the API to a new or existing stage.

3. **Create Resource and Method for Initiating a Call**:
   - Repeat the above steps to create another resource (e.g., `/initiate-call`).
   - Add a "POST" method to this resource.
   - Set up the integration to invoke the Lambda function responsible for initiating the call (`initiate_call`).
   - Save and deploy the API to the same or a new stage.

4. **Deploy the API and Note Down Endpoint URLs**:
   - Go to the "Stages" section in the API Gateway console.
   - Select the stage you deployed the API to (e.g., `prod`).
   - Note down the Invoke URL provided for the deployed API. You will use this URL to make requests to your API.

You can now use the endpoint URLs to trigger the Lambda functions via the API Gateway.
