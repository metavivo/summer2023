# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys

import os
from dotenv import load_dotenv

# add your project directory to the sys.path
#project_home = '/home/valitutti/examples/9_Flask_example1'
#project_home = '/home/valitutti/examples/10_Flask_example2_venv'
project_home = '/home/valitutti/examples/8_OpenAI_example1'

load_dotenv(os.path.join(project_home, '.env'))



if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from flask_app import app as application  # noqa
#from app import app as application  # noqa
