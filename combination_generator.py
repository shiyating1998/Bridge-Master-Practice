import itertools

def generate_combinations(values):
    # Initialize table header with an index column
    table = "|  | W  | E  | 分析 |\n|-------|------------|------------|------|\n"

    index = 1  # Initialize index for each row

    # Generate all possible combinations of splitting the list into two piles
    for i in range(len(values) + 1):
        for pile1 in itertools.combinations(values, i):
            pile2 = [item for item in values if item not in pile1]
            # Format piles and add to table, leaving the 分析 column blank
            table += f"| {index}     | {''.join(pile1) if pile1 else '—'} | {''.join(pile2) if pile2 else '—'} |      |\n"
            index += 1
    
    return table

values = ['A', 'Q', '6']
markdown_table = generate_combinations(values)
print(markdown_table)
