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

import dvc.api

with dvc.api.open(
    's3_data_1.txt',  ## 데이터 경로
    repo='https://github.com/GomDue/flask-docker.git'  ## github repo 경로
) as fd:
	data = fd.read()
	print(data)

# from dvc.api import DVCFileSystem

# fs = DVCFileSystem(config='Test/flask-docker/.dvc/config')

# text = fs.read_text("s3_data_1.txt", encoding="utf-8")

# print(text)