class Language:
    sos_token = 0
    eos_token = 1
    pad_token = 2
    unk_token = 3

    def __init__(self, name):
        self.name = name
        self.word2index = {'<SOS>': 0, '<EOS>': 1, '<PAD>': 2, '<UNK>': 3}
        self.word2count = {}
        self.index2word = {0: '<SOS>', 1: '<EOS>', 2: '<PAD>', 3: '<UNK>'}
        self.n_words = len(self.index2word)

    def index_words(self, sentence):
        for word in sentence.split(' '):
            self.index_word(word)

    def index_word(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1
