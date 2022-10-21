"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    def __init__(self, path):
        self.path = path
        self.words_read = []
        self.line_count = sum(1 for line in open(self.path))
        self.read_file()
        print(f"{self.line_count} words read")
    
    def read_file(self):
        new_file = open(self.path, "r")
        for line in new_file:
            lines = line.rstrip('\n')
            self.words_read.append(lines)
        new_file.close()


    def random_word(self):
        return choice(self.words_read)

class SpecialWordFinder(WordFinder):
    def find_special(self):
        for line in self.words_read:
           if line.startswith('#') or line.startswith(' '):
                self.words_read.remove(line)
        