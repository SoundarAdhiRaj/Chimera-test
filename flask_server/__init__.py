from flask import Flask, request, session, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

import config
import views

app.debug = app.config['DEBUG']

