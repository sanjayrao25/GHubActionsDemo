from src.num_ops import add, subtract, multiply, divide
def test_add():
  assert add(4, 5) == 9

def test_subtract():
  assert subtract(5, 4) == 1

def test_multiply():
  assert multiply(3, 4) == 12

def test_divide():
  assert divide(4, 2) == 2
   
