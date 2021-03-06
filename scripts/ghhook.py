#!/usr/bin/env python

"""
  Listens to github hooks at /poetroid and runs literatti and sends results to s3

"""

from flask import Flask, request
import json
from s3 import build
import os

app = Flask(__name__)

@app.route('/poetroid',methods=['POST'])
def gh_hook():
    # check request uri from github
    os.system('echo "%s"' % (deploy_time))
    payload = request.form.get('payload')
    data = json.loads(payload)
    deploy_time = build()
    os.system('echo "%s"' % (deploy_time))

    return "Done"

if __name__ == '__main__':
    app.run()
