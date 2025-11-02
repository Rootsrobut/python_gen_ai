class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"'{flavor}' chai is not available")
        if not isinstance(cups, int) or cups <= 0:
            raise TypeError("Number of cups must be a positive integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai is {total} rupees")
    except InvalidChaiError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


bill("masala", 2)
bill("elaichi", 1)
bill("ginger", "three")
bill("ginger", 0)