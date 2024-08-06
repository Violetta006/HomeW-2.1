def split_list(input_list):
    middle_index = (len(input_list) + 1) // 2
    return [input_list[:middle_index], input_list[middle_index:]]

examples = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
]

for example in examples:
    result = split_list(example)
    print(f"{example} => {result}")
