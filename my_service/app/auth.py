from functools import wraps
from flask import request, jsonify
from authlib.integrations.flask_client import OAuth
from app import create_app

app = create_app()
oauth = OAuth(app)

oauth.register(
    name='example',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    server_metadata_url='https://example.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            user_info = oauth.example.parse_id_token(token)
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(user_info, *args, **kwargs)
    return decorated
