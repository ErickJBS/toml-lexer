def formatOutput(result):
    return str(result).replace('[', '') \
    .replace(']', '').replace('\'', '') \
    .replace(' ', '').replace(',', '\n')
