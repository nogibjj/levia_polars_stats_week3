from main import add, subtract


def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(1, 2) == -1

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("Success")
