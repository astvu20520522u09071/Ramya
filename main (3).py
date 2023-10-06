def linear_search_product(products, target):
    indices = []
    for i in range(len(products)):
        if products[i] == target:
            indices.append(i)
    return indices


#Example usage:
products = ["apple", "banana", "orange", "banana", "grape"]
target = "banana"
print(linear_search_product(products, target))
