import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [[_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _]]

board2 =   [[_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, R, R, _],
            [_, R, _, _, _],
            [_, _, _, M, _]]

board3 =   [[_, _, _, M, _],
            [_, _, R, _, M],
            [_, R, R, R, _],
            [_, R, _, _, _],
            [_, _, _, M, _]]

board4 =   [[_, _, _, _, _],
            [_, _, R, _, _],
            [_, R, R, R, _],
            [M, R, M, M, _],
            [_, _, _, _, _]]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((1,2)) == R
    assert at ((4,0)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    set_board(board2)
    assert at((1,3)) == M
    assert at((2,2)) == R
    assert at((4,4)) == _
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert get_board() == [[_, _, _, M, _],
                          [_, _, R, M, _],
                          [_, R, M, R, _],
                          [_, R, _, _, _],
                          [_, _, _, R, _]]
    set_board(board2)
    assert get_board() ==   [[_, _, _, M, _],
                            [_, _, R, M, _],
                            [_, R, R, R, _],
                            [_, R, _, _, _],
                            [_, _, _, M, _]]

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    with pytest.raises(ValueError):
        string_to_location('H4')
    assert string_to_location('C4') == (2,3)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    # replace with tests
    assert location_to_string((1,1))=="B2"
    with pytest.raises(ValueError):
        location_to_string((5,5))
    assert location_to_string((3,4))=="D5"
    with pytest.raises(ValueError):
        location_to_string((-1,5))

def test_at():
    set_board(board1)
    assert at((2,2)) == M
    assert at((1,2)) == R
    assert at((0,0)) == _
    set_board(board2)
    assert at((2,2)) == R
    assert at((0,3)) == M
    assert at((0,0)) == _

def test_all_locations():
    assert all_locations()==[[(0,0),(0,1),(0,2),(0,3),(0,4)],[(1,0),(1,1),(1,2),(1,3),(1,4)],
    [(2,0),(2,1),(2,2),(2,3),(2,4)],[(3,0),(3,1),(3,2),(3,3),(3,4)],[(4,0),(4,1),(4,2),(4,3),(4,4)]]

def test_adjacent_location():
    assert adjacent_location((2,0), "right") == (2,1)
    assert adjacent_location((4,4), "down") == (5,4)
    assert adjacent_location((0,1), "up") == (-1,1)
    assert adjacent_location((3,1), "right") == (3,2)
    assert adjacent_location((3,4), "right") == (3,5)

def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((2,2), "up") == True
    assert is_legal_move_by_musketeer((0,4),"up") == False
    with pytest.raises(ValueError):
        assert is_legal_move_by_musketeer((3,1),"up")


def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((1,2),"up") == True
    assert is_legal_move_by_enemy((4,3),"down") == False
    with pytest.raises(ValueError):
            assert is_legal_move_by_enemy((2,2),"up")


def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((1,2),"down") == False
    assert is_legal_move((2,2), "up") == True
    assert is_legal_move((0,4),"up") == False
    assert is_legal_move((1,2),"up") == True
    assert is_legal_move((4,3),"down") == False

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((3,2)) == False
    assert can_move_piece_at((0,4)) == False

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board3)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    create_board()
    assert has_some_legal_move_somewhere('R') == False
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,1)) == ["up","left"]
    assert possible_moves_from((3,1)) == ["down","left","right"]
    assert possible_moves_from((0,4)) == []
    assert possible_moves_from((3,2)) == []
    create_board()
    assert possible_moves_from((0,0)) == []
    assert possible_moves_from((2,2)) == ["up","down","left","right"]

def test_is_legal_location():
    assert is_legal_location((2,2)) == True
    assert is_legal_location((0,0)) == True
    assert is_legal_location((4,4)) == True
    assert is_legal_location((5,5)) == False
    assert is_legal_location((6,3)) == False
    assert is_legal_location((-1,8)) == False

def test_is_within_board():
    assert is_within_board((2,2), right) == True
    assert is_within_board((4,4), right) == False
    assert is_within_board((4,4), down) == False
    assert is_within_board((4,4), up) == True
    assert is_within_board((4,4), left) == True

def test_all_possible_moves_for():
    set_board(board1)
    assert all_possible_moves_for("M")==[((1, 3), 'down'), ((1, 3), 'left'), ((2, 2), 'up'), ((2, 2), 'left'), ((2, 2), 'right')]
    assert all_possible_moves_for("R")==[((1, 2), 'up'), ((1, 2), 'left'), ((2, 1), 'up'), ((2, 1), 'left'),((2, 3), 'down'),
    ((2, 3), 'right'), ((3,1), 'down'), ((3,1), 'left'), ((3,1), 'right'), ((4,3), 'up'), ((4,3), 'left'), ((4,3), 'right')]
    set_board(board2)
    assert all_possible_moves_for("M")==[((1, 3), 'down'), ((1, 3), 'left')]
    assert all_possible_moves_for("R")==[((1, 2), 'up'), ((1, 2), 'left'), ((2, 1), 'up'), ((2, 1), 'left'),((2, 2), 'down'),((2, 3), 'down'),
    ((2, 3), 'right'), ((3,1), 'down'), ((3,1), 'left'), ((3,1), 'right')]
    set_board(board3)
    assert all_possible_moves_for("R")==[((1, 2), 'up'), ((1, 2), 'left'), ((1, 2), 'right'), ((2, 1), 'up'), ((2, 1), 'left'),((2, 2), 'down'), ((2, 3), 'up'), ((2, 3), 'down'),
    ((2, 3), 'right'), ((3,1), 'down'), ((3,1), 'left'), ((3,1), 'right')]
    assert all_possible_moves_for("M")==[]

def test_make_move():
    set_board(board1)
    assert make_move((2,2),"left") ==   [[_, _, _, M, _],
                                        [_, _, R, M, _],
                                        [_, M, _, R, _],
                                        [_, R, _, _, _],
                                        [_, _, _, R, _]]

    set_board(board1)
    assert make_move((1,2),"left") ==   [[_, _, _, M, _],
                                        [_, R, _, M, _],
                                        [_, M, _, R, _],
                                        [_, R, _, _, _],
                                        [_, _, _, R, _]]

def test_choose_computer_move():
    board1 =  [[_, _, _, M, _],
                [_, _, R, M, _],
                [_, R, M, R, _],
                [_, R, _, _, _],
                [_, _, _, R, _]]
    set_board(board1)
    assert choose_computer_move(R) == ((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right') or ((4,3), 'up') or ((4,3), 'left') or ((4,3), 'right')
    assert choose_computer_move(R) == ((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right') or ((4,3), 'up') or ((4,3), 'left') or ((4,3), 'right')
    assert choose_computer_move(R) == ((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right') or ((4,3), 'up') or ((4,3), 'left') or ((4,3), 'right')
    assert choose_computer_move(R) == ((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right') or ((4,3), 'up') or ((4,3), 'left') or ((4,3), 'right')
    assert choose_computer_move(R) == ((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right') or ((4,3), 'up') or ((4,3), 'left') or ((4,3), 'right')
    assert choose_computer_move(R) == ((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right') or ((4,3), 'up') or ((4,3), 'left') or ((4,3), 'right')
    assert all_possible_moves_for(M) == ((1, 3), 'down') or ((1, 3), 'left') or ((2, 2), 'up') or ((2, 2), 'left') or ((2, 2), 'right')
    assert all_possible_moves_for(M) == ((1, 3), 'down') or ((1, 3), 'left') or ((2, 2), 'up') or ((2, 2), 'left') or ((2, 2), 'right')
    assert all_possible_moves_for(M) == ((1, 3), 'down') or ((1, 3), 'left') or ((2, 2), 'up') or ((2, 2), 'left') or ((2, 2), 'right')
    assert all_possible_moves_for(M) == ((1, 3), 'down') or ((1, 3), 'left') or ((2, 2), 'up') or ((2, 2), 'left') or ((2, 2), 'right')
    assert all_possible_moves_for(M) == ((1, 3), 'down') or ((1, 3), 'left') or ((2, 2), 'up') or ((2, 2), 'left') or ((2, 2), 'right')
    set_board(board2)
    assert all_possible_moves_for("M")==((1, 3), 'down') or  ((1, 3), 'left')
    assert all_possible_moves_for("M")==((1, 3), 'down') or  ((1, 3), 'left')
    assert all_possible_moves_for("R")==((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")==((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")==((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")==((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")==((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")==((1, 2), 'up') or ((1, 2), 'left') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    set_board(board3)
    assert all_possible_moves_for("R")== ((1, 2), 'up') or ((1, 2), 'left') or ((1, 2), 'right') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'up') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")== ((1, 2), 'up') or ((1, 2), 'left') or ((1, 2), 'right') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'up') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")== ((1, 2), 'up') or ((1, 2), 'left') or ((1, 2), 'right') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'up') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")== ((1, 2), 'up') or ((1, 2), 'left') or ((1, 2), 'right') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'up') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    assert all_possible_moves_for("R")== ((1, 2), 'up') or ((1, 2), 'left') or ((1, 2), 'right') or ((2, 1), 'up') or ((2, 1), 'left') or ((2, 2), 'down') or ((2, 3), 'up') or ((2, 3), 'down') or ((2, 3), 'right') or ((3,1), 'down') or ((3,1), 'left') or ((3,1), 'right')
    
def test_is_enemy_win():
    set_board(board1)
    assert is_enemy_win() == False
    set_board(board2)
    assert is_enemy_win() == True
    set_board(board4)
    assert is_enemy_win() == True
