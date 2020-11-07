import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('webpage', __name__, url_prefix='/webpage')

@bp.route('/render', methods=('GET', 'POST'))
def render():
    return render_template('main.html')