import boto3
import random

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Employees')
    response = table.scan()
    employees = response['Items']
    
    if not employees:
        return {
            'statusCode': 404,
            'body': 'No employees found'
        }
    
    random_employee = random.choice(employees)
    
    return {
        'statusCode': 200,
        'body': random_employee
    }
