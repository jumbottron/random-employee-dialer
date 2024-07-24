# Amazon Connect Setup for Employee Dialer

Amazon Connect is a cloud-based contact center service that allows you to set up and manage customer interactions. In this case, we will use Amazon Connect to handle the outbound calls to your employees. Here's how you can set it up:

## Step 1: Create an Amazon Connect Instance

1. **Log in to the AWS Management Console**.
2. **Navigate to Amazon Connect**:
   - Search for "Amazon Connect" in the AWS services search bar.
   - Click on "Amazon Connect" to open the service dashboard.
3. **Create a new Amazon Connect instance**:
   - Click "Get started" if it's your first time, or "Add an instance" if you already have instances.
   - Follow the prompts to set up your instance. You'll need to provide:
     - **Instance alias**: A unique name for your instance.
     - **Administrator**: Provide admin details.
     - **Access URL**: This will be your instance URL.
   - Click "Create instance".

## Step 2: Set Up an IVR (Interactive Voice Response)

1. **Access the Amazon Connect instance**:
   - Navigate to the URL provided for your instance.
   - Log in with the admin account you set up.
2. **Set up a contact flow**:
   - Go to the "Contact flows" section.
   - Click "Create contact flow".
   - Use the drag-and-drop editor to design your IVR. A simple example might include:
     - **Play prompt**: A greeting message.
     - **Get customer input**: Ask the employee to press a number to confirm they are available.
     - **Branch based on input**: Direct the call based on the input received.
   - Save the contact flow and note the Contact Flow ID.
3. **Set up phone numbers**:
   - Go to the "Phone numbers" section.
   - Claim a new phone number or use an existing one.
   - Assign the contact flow you created to this phone number.

## Step 3: Configure IAM Roles

1. **Create an IAM role for Lambda with Connect permissions**:
   - Navigate to the IAM service in the AWS Management Console.
   - Create a new role for Lambda.
   - Attach the `AmazonConnect_FullAccess` policy to this role.
   - Note the role ARN for use in your Lambda functions.

## Step 4: Update Lambda Function to Initiate Call

Update the Lambda function to initiate a call using the Amazon Connect instance and the contact flow you created:

```python
import boto3

def lambda_handler(event, context):
    connect_client = boto3.client('connect')
    
    employee_number = event['body']['PhoneNumber']
    
    response = connect_client.start_outbound_voice_contact(
        DestinationPhoneNumber=employee_number,
        ContactFlowId='YOUR_CONTACT_FLOW_ID',
        InstanceId='YOUR_INSTANCE_ID',
        SourcePhoneNumber='YOUR_SOURCE_PHONE_NUMBER'
    )
    
    return {
        'statusCode': 200,
        'body': 'Call initiated'
    }
