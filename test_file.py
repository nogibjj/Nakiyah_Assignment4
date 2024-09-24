from main_file import function1


def test_function1():
    assert function1(1, 2, 3) == 27
    assert function1(2, 2, 2) == 16
    assert function1(3, 2, 4) == 625


if __name__ == "__main_file__":
    test_function1()
