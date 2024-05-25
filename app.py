# from flask import Flask

# app = Flask(__name__)
# host_addr = "0.0.0.0"
# host_port = 5000

# @app.route('/')
# def hello():
#     return "hello world"

# @app.route('/test')
# def ping():
#     return {'response': 'test'}


# if __name__ == "__main__":
#     app.run(debug=True,
#             host=host_addr,
#             port=host_port)

from dotenv import load_dotenv
import os
import dvc.api
import pickle

load_dotenv()

remote_config = {
	'access_key_id' : os.environ.get('access_key_id'),
	'secret_access_key' : os.environ.get('secret_access_key')
}

print(os.environ.get('access_key_id'))

with dvc.api.open(
    'kcbert_hatespeech_classifier.pth',
    repo='https://github.com/GomDue/flask-docker.git',
	remote_config=remote_config
) as f:
	model = pickle.load(f)

print(model)