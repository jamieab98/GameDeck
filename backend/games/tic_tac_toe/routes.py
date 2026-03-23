from logic import *
from flask import Blueprint, request, jsonify
from . import tic_tac_toe_bp

@tic_tac_toe_bp.POST('/move')
def move():
    data = request.get_json()

    board = data['board']
    player = data['player']
    location = data['location']

    apply_move(board, player, location)