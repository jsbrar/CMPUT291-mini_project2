import sys
import fileinput
import re
import pdb
import os

class Hash:
    def __init__(self):
        self.adfile = open("ads.txt", "r+")
        self.table = {}

    def insert(self, key, data):
        if key in self.table:
            self.table[key].append(data)
        else:
            self.table[key] = data

    def delete(self, key):
        del self.table[key]

    def search(self, key):
        return self.table[key]
