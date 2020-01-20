from DoublyLinkedList import DoublyLinkedList
from ChainingHashTableMap import ChainingHashTableMap
import sys
sys.path.append(sys.path[0] + '/../DataStructure')


def most_frequent(lst):
    fMap = ChainingHashTableMap()
    for num in lst:
        if num not in fMap:
            fMap[num] = 0
        fMap[num] += 1
    most_frequent = None
    for key in fMap:
        if most_frequent is None or fMap[key] > fMap[most_frequent]:
            most_frequent = key
    return most_frequent


def two_sum(lst, target):
    indMap = ChainingHashTableMap()
    for i in range(len(lst)):
        if lst[i] in indMap:
            return(indMap[lst[i]], i)
        indMap[target - lst[i]] = i
    return (None, None)


class PlayList:
    def __init__(self):
        self.RefMap = ChainingHashTableMap()
        self.DataList = DoublyLinkedList()

    def add_song(self, new_song):
        self.RefMap[new_song] = self.DataList.add_last(new_song)

    def add_song_after(self, song, new_song):
        song_ref = self.RefMap[song]
        self.RefMap[new_song] = self.DataList.add_after(song_ref, new_song)

    def play_song(self, song):
        print("Playing " + self.RefMap[song].data)

    def play_list(self):
        for song in self.DataList:
            print("Playing " + song)
