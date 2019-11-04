from tokenizer import Tokenizer
from utils import formatOutput, ignoreComments
from const import table, finals
import fileinput

tokenizer = Tokenizer(table, finals)
stdin = ''
for line in fileinput.input():
    stdin = stdin + line

stdin = ignoreComments(stdin)

tokens = tokenizer.tokenize(stdin);
result = list(tokens)
print(formatOutput(result))
