inventory = [
    {
        "name": "Vintage T-Shirt",
        "price": 29.99,
        "stock": 42,
    },
    {
        "name": "Coffee Mug",
        "price": 12.50,
        "stock": 100,
    },
    {
        "name": "Laptop Sticker Pack",
        "price": 5.00,
        "stock": 250,
    },
]

cart = {}


def display_products(inventory):
    for index, item in enumerate(inventory):
        print(
            f"Id: {index + 1}, Name: {item["name"]} - Price: {item["price"]} - Stock: {item["stock"]}"
        )


def add_to_cart(inventory, cart):
    product_id = int(input("Product Number: "))
    quantity = int(input("Quantity: "))
    if product_id > 0 and product_id <= len(inventory):
        if quantity <= inventory[product_id - 1]["stock"]:
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity
        else:
            print(
                f"Sorry, only {inventory[product_id - 1]["stock"]} items are left in stock."
            )
    else:
        print("Invalid Id")


display_products(inventory)
