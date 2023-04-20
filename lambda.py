import json
import re

def lambda_handler(event, context):
    username = event['username']
    password = event['password']
    
   
    username_pat = r'^\w{1,8}$'
    password_pat = r'^(?=.*[A-Za-z0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{1,8}$'
    
    if re.match(username_pat, username) and re.match(password_pat, password):
        return {'message': 'SUCCESS'}
    else:
        return {'message': 'FAILED'}
    