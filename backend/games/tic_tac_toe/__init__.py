from flask import Blueprint

tic_tac_toe_bp = Blueprint("tic_tac_toe", __name__)

from . import routes