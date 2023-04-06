from flask import request, render_template, url_for
from flask_login import login_user, login_required, logout_user

def index():
    return 'Index'
