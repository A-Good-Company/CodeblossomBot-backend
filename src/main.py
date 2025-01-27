from flask import jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
import functions_framework

load_dotenv()

# Initialize OpenAI client with environment variable
client = OpenAI(
    api_key=""  # Get from .env or environment variables
)

@functions_framework.http
def munkchat(request):
    """HTTP Cloud Function handling chat requests with OpenAI."""
    # CORS headers configuration
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    # Get message from request
    message = None
    
    if request.method == 'GET':
        message = request.args.get('message')
    else:
        request_json = request.get_json(silent=True)
        if request_json and 'message' in request_json:
            message = request_json['message']

    if not message:
        return jsonify({'error': 'No message provided'}), 400, headers

    try:
        # Create chat completion with updated SDK syntax
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            model="gpt-4-turbo"  # Updated model name (verify current model name)
        )
        
        return jsonify({
            "response": chat_completion.choices[0].message.content
        }), 200, headers
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers