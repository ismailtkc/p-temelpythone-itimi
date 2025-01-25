def flatten(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):  
            flattened.extend(flatten(item))  
        else:
            flattened.append(item)  
    return flattened

# Örnek kullanım
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten(input_list)
print(output_list)  