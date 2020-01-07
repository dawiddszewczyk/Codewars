def binary_array_to_number(arr):
    new_str = ""
    for i in range(len(arr)):
        new_str+=str(arr[i])
    return int(new_str, 2)

print(binary_array_to_number([0,0,0,1]))
print(binary_array_to_number([0,0,1,1]))
print(binary_array_to_number([1,1,1,1]))
print(binary_array_to_number([0,1,0,1]))