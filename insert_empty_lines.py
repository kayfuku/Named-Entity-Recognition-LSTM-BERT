
input_file = 'data/test_empty_line.tsv'

with open(input_file, encoding='utf_8') as f:
    data = []
    for line in f:
        # line = line.rstrip() # Get rid of '\n'. This line is not necessary.
        # print(line)
        data.append(line)
        word, tag = line.split()
        # print(word)
        if word == '.':
            # Insert empty line.
            data.append('\n')

print(data)

# for line in data:
#     print(line)

output_file = 'data/test_empty_line_inserted.tsv'

with open(output_file, mode='w') as f:
    for line in data:
        f.write(line)
        # f.write('\n') This is not necessary.



























