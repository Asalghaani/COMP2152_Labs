cart = ["apple","banana","milk","bread","apple","egg"]
apple_count = cart.count("apple")
print(f"Number of apples : {apple_count}")
print(f"Position of milk : {cart.index("milk")}")
cart.remove("apple")
print(f"removed item using pop:{cart.pop()}")
print("Is banana in the cart?","banana"in cart)
print(f"Final cart: {cart}")