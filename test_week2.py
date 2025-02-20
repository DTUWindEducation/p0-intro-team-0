"""Test your functions from Week 2 assignment.
"""
import pytest
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect


@pytest.mark.parametrize("inp, out", [(130, 'Too small!\n'), (140, 'Just right. :)\n'), (160, 'Too large!\n')])
def test_goldilocks(inp, out, capsys):
    """Check goldilocks returns expected output"""
    # given
    # when
    fxn.goldilocks(inp)
    captured = capsys.readouterr()
    # then
    assert captured.out == out  # TODO! Update the contents of this function so it correctly tests goldilocks


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match

@pytest.mark.parametrize("inp, out", [(10, [1,1,2,3,5,8]), (22,[1,1,2,3,5,8,13,21]), (2,[1,1,2])])
def test_fibonacci_stop(inp,out):
    """Check fibonacci functions works as expected."""
    # given
    #inp = 10
    #exp_out = [1,1,2,3,5,8]
    # when
    #out = fxn.fibonacci_stop(inp)
    # then
    assert fxn.fibonacci_stop(inp) == out  


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp1 = [-1, 2, 6, 95]
    inp2 = [1, 0, 0, 0]
    exp_out = [-999, 2, 6, 95]
    
    # when
    out = fxn.clean_pitch(inp1,inp2)
    
    # then
    assert exp_out == out  # TODO! Update the contents of this function so it correctly tests clean_pitch
