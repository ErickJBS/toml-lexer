from tokenizer import Tokenizer

alpha = ['a', 'b']
table = {
    0: {'a': 1, 'b': 1},
    1: {'a': 1, 'b': 2},
    2: {'a': 0, 'b': 0},
}
finals = {
    2: 'TOKEN'
}


tokenizer = Tokenizer(alpha, table, finals)
stdin = input()

tokens = tokenizer.tokenize(stdin);
result = list(tokens)
print(result)
