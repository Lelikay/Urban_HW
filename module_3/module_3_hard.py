def calculate_structure_sum(args):
    total = 0

    def recursive_sum(args):
        nonlocal total

        for item in args:
            if isinstance(item, int):
                total += item
            elif isinstance(item, str):
                total += len(item)
            elif isinstance(item, list):
                recursive_sum(item)
            elif isinstance(item, tuple):
                recursive_sum(item)
            elif isinstance(item, dict):
                for key, value in item.items():
                    recursive_sum([key, value])

    recursive_sum(args)

    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)