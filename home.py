from flask import Blueprint, render_template, abort
from flask_login import login_required

from db import get_thresholds, get_current_air_data, get_single_threshold

home = Blueprint('home', __name__)


@home.route('/')
@login_required
def homepage():
    return render_template('pages/index.html',
                           air_data=get_current_air_data(),
                           thresholds=get_thresholds())


@home.route('/edit/<type>')
@login_required
def edit_threshold(type):
    thres_data = get_single_threshold(type)
    if thres_data is None:
        abort(404)
    print(thres_data)
    value, max_value, step_value = thres_data
    return render_template('pages/set_threshold.html',
                           type=type,
                           current_value=value,
                           max_value=max_value,
                           step_value=step_value)
