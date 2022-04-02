products = [1, 45, 87, 2, 5, 23, 9, 4]
seen_prods = [87, 1, 5]
d = []
def filter_products(products, seen_prods):
    for item in products:
        if item not in d:
            d.append(item)
            print(d)



d=(filter_products(
        [1, 45, 87, 2, 5, 23, 9],
        [87, 1, 5]
))
