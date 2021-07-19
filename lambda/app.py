import sys

def handler(event, context):

    # get request body from 'event'
    # something = event.get('something', None)

    return 'Hello from AWS Lambda using Python' + sys.version + '!'        
