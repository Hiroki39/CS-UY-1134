import string
import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from LinkedHashTableMap import LinkedHashTableMap


class InvertedFile:
    def __init__(self, file_name):
        self.IndMap = LinkedHashTableMap()
        f = open(file_name, "r")
        index = 0
        for line in f:
            for word in line.split():
                word = word.lower().translate(str.maketrans('', '', string.punctuation))
                if word is not None:
                    try:
                        self.IndMap[word].append(index)
                    except KeyError:
                        self.IndMap[word] = [index]
                    index += 1

    def indices(self, word):
        try:
            return self.IndMap[word]
        except KeyError:
            return []

    def generate_report(self):
        f = open("out.txt", "w")
        f.write("report:\n")
        f.writelines(str(key) + ':' +
                     str(self.IndMap[key]) + "\n" for key in self.IndMap)
