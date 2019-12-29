from DoublyLinkedList import DoublyLinkedList
from ChainingHashTableMap import ChainingHashTableMap


class ExtendedPartiesQueue:
    def __init__(self):
        self.PartyMap = ChainingHashTableMap()
        self.KeyList = DoublyLinkedList()

    def __len__(self):
        return len(self.KeyList)

    def is_empty(self):
        return len(self) == 0

    def enq_party(self, party_name, party_size):
        self.PartyMap[party_name] = party_size
        self.KeyList.add_last(party_name)

    def add_to_party(self, party_name, size_to_add):
        try:
            self.PartyMap[party_name] += size_to_add
        except KeyError:
            raise Exception("party not in queue")

    def first_party(self):
        if self.is_empty():
            raise Exception("ExtendedPartiesQueue is empty")
        key = self.KeyList.header.next.data
        return self.PartyMap[key]

    def deq_first_party(self):
        if self.is_empty():
            raise Exception("ExtendedPartiesQueue is empty")
        key = self.KeyList.delete_first()
        size = self.PartyMap[key]
        del self.PartyMap[key]
        return size
