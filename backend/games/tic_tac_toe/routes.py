from logic import *
from flask import Blueprint, request, jsonify
from . import tic_tac_toe_bp

@tic_tac_toe_bp.post('/move')
def move():
    data = request.get_json()

    board = data['board']
    player = data['player']
    location = data['location']

    new_board = apply_move(board, player, location)
    
    if check_winner(new_board):
        return jsonify({
            'board': new_board,
            'player': player,
            'winner': 'winner'
        })

    if check_tie(new_board):
        return jsonify({
            'board': new_board,
            'winner': None
        })
    
    upcoming_player = next_player(player)
    return jsonify({
        'board': new_board,
        'player': upcoming_player,
        'winner': None
    })