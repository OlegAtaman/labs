class FileManager:
    def __init__(self, filename):
        try:
            file = open(filename)
            self.text = file.readlines()
        except:
            self.text = ''

        self.wordnum = self.count_words()
        self.charnum = self.count_chars()
        self.sentencenum = self.count_sentences()

    def count_chars(self):
        charnum = 0
        for lane in self.text:
            for i in range(len(lane)):
                charnum += 1
            charnum -= 1
        if self.text:
            charnum += 1
        return charnum

    def count_words(self):
        spoted = False
        wordnum = 0
        for lane in self.text:
            for i in range(len(lane)):
                if lane[i] == ' ' and spoted:
                    wordnum += 1
                    spoted = False
                elif lane[i] == ' ':
                    pass
                else:
                    spoted = True
            if spoted:
                wordnum += 1
        return wordnum

    def count_sentences(self):
        spoted = False
        sentencenum = 0
        for lane in self.text:
            for i in range(len(lane)):
                if lane[i] == '.' and spoted:
                    sentencenum += 1
                    spoted = False
                elif lane[i] == '.':
                    pass
                else:
                    spoted = True
        return sentencenum

    def printfile(self):
        for line in self.text:
            print(line, end='')


manager1 = FileManager('text.txt')

print('Your file contains:')
manager1.printfile()
print('\n')
print(f'Number of chars is {manager1.charnum}')
print(f'Number of words is {manager1.wordnum}')
print(f'Number of sentences is {manager1.sentencenum}')

