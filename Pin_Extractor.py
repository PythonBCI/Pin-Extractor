def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(str(len(words[line_index])))
        secret_code += str(len(words[line_index]))
    
