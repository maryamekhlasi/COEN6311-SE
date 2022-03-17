from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
#@login_required
def home():
     seat_type = ['Business', 'Economy', 'Permium']
     return render_template("home.html",seat_type=seat_type, user=current_user)
