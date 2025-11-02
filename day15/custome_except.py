def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"Brewing {flavor} chai...")


brew_chai("ginger")

try:
    brew_chai("mint")
except ValueError as e:
    print(f"Handled Error: {e}")


class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("Chai is ready...")

try:
    make_chai(0, 1)
except OutOfIngredientsError as e:
    print(f"Error caught: {e}")
make_chai(1, 2)
