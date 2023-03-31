from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required

from db import get_thresholds, get_current_air_data, get_single_threshold, set_threshold

home = Blueprint('home', __name__)


@home.route('/')
@login_required
def homepage():
    return render_template('pages/index.html',
                           air_data=get_current_air_data(),
                           thresholds=get_thresholds())


@home.route('/edit/<type>', methods=['GET'])
@login_required
def edit_threshold(type):
    thres_data = get_single_threshold(type)
    if thres_data is None:
        abort(404)
    value, max_value, step_value = thres_data
    return render_template('pages/set_threshold.html',
                           type=type,
                           current_value=value,
                           max_value=max_value,
                           step_value=step_value)


@home.route('/edit/<type>', methods=['POST'])
@login_required
def edit_threshold_post(type):
    value = request.form.get('new-threshold')
    if not set_threshold(type, float(value)):
        abort(400)
    return redirect(url_for('home.homepage'))
