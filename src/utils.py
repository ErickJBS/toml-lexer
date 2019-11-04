def formatOutput(result):
    return str(result).replace('[', '') \
    .replace(']', '').replace('\'', '') \
    .replace(' ', '').replace(',', '\n')

def ignoreComments(input):
    delete_mode = True
    result = []
    for c in input:
        if c == '#':
            delete_mode = True
        if c == '\n':
            delete_mode = False
        if c != '#' and not delete_mode:
            result.append(c)

    return ''.join(result)
