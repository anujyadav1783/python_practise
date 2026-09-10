from calculator import calculatora

def test_calculator():

    try:
        assert calculatora(2) == 8
    except AssertionError:
        print("Test failed: calculatora(2) should return 4")

    try:
        assert calculatora(3) == 6
    except AssertionError:
        print("Test failed: calculatora(3) should return 6")

    try:
        assert calculatora(0) == 0
    except AssertionError:
        print("Test failed: calculatora(0) should return 0")


def main():
    test_calculator()


main()