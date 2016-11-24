import os
import json
from runserver import app
from flask import request, redirect, url_for, render_template, flash, make_response
import logging
import logging.handlers
from datetime import date
import sys
import traceback
import urllib
from urlparse import urlparse
import time
import requests

log_format = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
logging.basicConfig(format=log_format, level=logging.DEBUG)
my_logger = logging.getLogger('views')
my_logger.setLevel(logging.DEBUG)

base_url = app.config['BASE_URL']

@app.route('/',methods = ['GET'])
def home():
    try:
        if request.method == 'GET':
            data = [{'age':26,'course':'CS','name':'vicky'},{'age':25,'course':'IS','name':'raj'},{'age':24,'course':'CS','name':'Jason'}]
            filepath = os.path.dirname(os.path.abspath(__file__))
            fname = os.path.join(filepath, "testData.txt")
            json.dump(data,open(fname,'w'))
            xml_template = json.load(open(fname))
            return render_template("student_xml_content.html",data=xml_template)

    except Exception :
        my_logger.debug("Error In home()")
        msg = "Error: %s %s" % (sys.exc_info()[0], traceback.format_exc())
        my_logger.debug(msg)
