class Tokenizer(object):
    """docstring for Tokenizer."""

    def __init__(self, table, finals):
        super(Tokenizer, self).__init__()
        self.table = table
        self.finals = finals

    def tokenize(self, input):
        current_state = 0
        for c in input:
            # Go to next state
            current_state = self.table[current_state][c]
            # Check if the current state is final and print its token
            if current_state in self.finals:
                yield self.finals[current_state]
                current_state = 0
