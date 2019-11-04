class Tokenizer(object):
    """docstring for Tokenizer."""

    def __init__(self, alpha, table, finals):
        super(Tokenizer, self).__init__()
        self.alpha = alpha
        self.table = table
        self.finals = finals

    def tokenize(self, input):
        current_state = 0
        for c in input:
            if not c in self.alpha:
                raise Exception(f'Character {c} does not belong to the alphabet')
            # Go to next state
            current_state = self.table[current_state][c]
            # Check if the current state is final and print its token
            if current_state in self.finals:
                yield self.finals[current_state]
