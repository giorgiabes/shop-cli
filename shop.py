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


def display_products(inventory):
    for index, item in enumerate(inventory):
        print(
            f"Id: {index + 1}, Name: {item["name"]} - Price: {item["price"]} - Stock: {item["stock"]}"
        )


display_products(inventory)
