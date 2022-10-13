class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.charnum = self.count_chars()
        self.wordnum = self.count_words()
        self.sentencenum = self.count_sentences()

    def count_chars(self):
        try:
            file = open(self.filename)
            text = file.read().replace('\n', ' ')
            file.close()
        except:
            text = ''

        splited = list(text)
        for char in splited:
            if not char:
                splited.remove(char)
        return len(splited)

    def count_words(self):
        try:
            file = open(self.filename)
            text = file.read().replace('\n', ' ')
            file.close()
        except:
            text = ''

        splited = text.split(' ')
        for word in splited:
            if not word:
                splited.remove(word)
        return len(splited)

    def count_sentences(self):
        try:
            file = open(self.filename)
            text = file.read().replace('\n', ' ')
            file.close()
        except:
            text = ''

        splited = text.split('.')
        for sent in splited:
            if not sent:
                splited.remove(sent)
        return len(splited)

    def printfile(self):
        try:
            file = open(self.filename)
            text = file.read()
            file.close()
        except:
            text = ''
        for line in text:
            print(line, end='')


manager1 = FileManager('text.txt')

print('Your file contains:')
manager1.printfile()
print('\n')
print(f'Number of chars is {manager1.charnum}')
print(f'Number of words is {manager1.wordnum}')
print(f'Number of sentences is {manager1.sentencenum}')
