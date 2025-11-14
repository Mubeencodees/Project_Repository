from src.mathoperations import add,subtract 

def test_add():
    assert add(5,3)==8
    assert add(-5,3)== -2
    assert add(-5,-3)==-8
    assert add(5,-3)== 2

def test_sub():
    assert(5,3)==2
    assert add(-5,3)== -8
    assert add(-5,-3)==-2
    assert add(5,-3)== 8


