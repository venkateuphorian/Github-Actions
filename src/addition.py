# app.py
# This is a simple addition program
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 4
    assert add(1, -1) == 0