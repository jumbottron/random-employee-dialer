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
