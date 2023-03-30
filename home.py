from flask import Blueprint, render_template
from flask_login import login_required

from db import get_thresholds, get_current_air_data

home = Blueprint('home', __name__)


@home.route('/')
@login_required
def homepage():
    return render_template('pages/index.html',
                           air_data=get_current_air_data(),
                           thresholds=get_thresholds())
