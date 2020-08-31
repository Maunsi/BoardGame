from flask import Flask, request, render_template
from os import path
from os import getenv

import logging
import socket
from logging.handlers import SysLogHandler
import sys
import json


# environmentName = getenv('ENVIRONMENT_NAME')
# if environmentName == None:
#     environmentName = 'LocalEnvironment'
#
# syslogAddressEnvVar = getenv('SYSLOG_ADDRESS')
# syslogAddress = None
# logHandler = None
# if syslogAddressEnvVar:
#     syslogAddress = json.loads(syslogAddressEnvVar)
#
# if syslogAddress and ('address' in syslogAddress and 'port' in syslogAddress and syslogAddress['port']):
#     syslogAddressPort = int(syslogAddress['port'])
#     logHandler = SysLogHandler(address=(syslogAddress['address'], syslogAddressPort))
# else:
#     logHandler = logging.StreamHandler(sys.stdout)
#
# format = '%(asctime)s {0} boardgame: %(levelname)s %(message)s'.format(environmentName)
# formatter = logging.Formatter(fmt=format, datefmt='%b %d %H:%M:%S')
#
# logHandler.setFormatter(formatter)
#
# logger = logging.getLogger()
# logger.addHandler(logHandler)
# logger.setLevel(logging.INFO)


# def my_handler(type, value, tb):
#     logger.exception('Uncaught exception: {0}'.format(str(value)))


# Install exception handler
# sys.excepthook = my_handler

app = Flask(__name__)


# TEST ME: curl -d '{"fileName": "generic.xlsx"}' -H "Content-Type: application/json" -X POST 'http://localhost:8080/validate'
# @app.route('/validate', methods=['POST'])
# def validate():
#     file_name = request.get_json()["fileName"]
#     obj = s3.get_object(Bucket=bucket_name, Key=path.join(s3_file_path, file_name))
#     xl_body = obj['Body'].read()
#     result = validator.validate_from_memory(file_binary=xl_body, file_name=file_name)
#     return result
#

@app.route('/version', methods=['GET'])
def version():
    v = getenv('VERSION')
    if v == None:
        return "No version set"
    return v


# TEST ME: curl -d '{"fileName": "generic.xlsx"}' -H "Content-Type: application/json" -X GET 'http://localhost:8080/summary'
# @app.route('/summary', methods=['GET'])
# def summary():
#     file_name = request.get_json()["fileName"]
#     obj = s3.get_object(Bucket=bucket_name, Key=path.join(s3_file_path, file_name))
#
#     xl_body = obj['Body'].read()
#     result = TemplateSummary.summary_from_memory(file_binary=xl_body, file_name=file_name)
#     return result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def react_example():
    return render_template("react-example.html")

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


if __name__ == "__main__":
    app.run(debug=True)
