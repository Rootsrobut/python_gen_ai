users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"}, 
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = { 
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10), 
}

for user in users:
    percent_off, fixed_off = discounts.get(user["coupon"], (0.0, 0))
    discount_amount = (user["total"] * percent_off) + fixed_off
    amount_paid = user["total"] - discount_amount
    print(f"User {user['id']} (Coupon: {user['coupon']}):")
    print(f"  - Original Total: {user['total']:.2f}, Discount: {discount_amount:.2f}, Final Paid: {amount_paid:.2f}")