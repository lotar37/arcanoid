def get_sdnf(table):
    result = []
    for inputs, row_result in table.items():

        if row_result:
            row = []
            for value, letter in zip(inputs, 'XYZIJK'):
                row.append(('' if value else 'not ') + letter)
            result.append('({})'.format(' and '.join(row)))
    return ' or '.join(result)
# Ключи словаря - входы, значения - выходы
table = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 1
}
# table = {
# (0,0,0):0,
# (0,0,1):1,
# (0,1,0):1,
# (0,1,1):0,
# (1,0,0):1,
# (1,0,1):1,
# (1,1,0):0,
# (1,1,1):1
# }
print(get_sdnf(table))