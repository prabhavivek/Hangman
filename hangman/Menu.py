'''
Created on 10-Feb-2020

@author: ibright
'''
from IO import *
from enum import Enum

class MenuX():
    def __init__(self, title):
        self.title = title
        self.menu_items = []

    def add(self, item):
        self.menu_items.append(item)

    def run(self):
        clear_screen()
        print_title(self.title + '\n')
        idx = 1
        for menu in self.menu_items:
            print('%4d. %s' % (idx, menu.help))
            idx += 1
        opt = get_inp('\nEnter option', 1, len(self.menu_items))

        return self.menu_items[opt-1].action()

class MenuStatus(Enum):
    OK = 0
    DONE = 1
    ERROR = -1

class MenuItem():
    def __init__(self, help_line, action):
        self.help = help_line
        self.action = action

    def set_title(self, title):
        self.help = title



