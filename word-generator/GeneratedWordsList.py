import word_generator

class GeneratedWordsList():
    """List with saved randomly generated words"""

    def __init__(self, no_of_words, min_word_length, max_word_length):
        self.words_list = word_generator.generate_word_list(no_of_words, min_word_length, max_word_length)

    def print_words(self):
        for word in self.words_list:
            print(word)
    
    def save_to_file(self, path):
        with open(path, 'w') as words_file:
            for word in self.words_list:
                words_file.write(word+'\n')