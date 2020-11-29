'''
Created on Jan 30, 2019

@author: Logu

General purpose table display module

'''

import color
from IO import *

class Table():
    
    printFunc = print
    
    def __init__(self, *columns):
        '''
        Constructor
        '''
        self.getSize()
        self.count = 0
        cols = []
        self.lengths = []
        self.totalLength = 0
        for col in columns:
            tmp = col.split(':')
            cols.append(tmp[0])
            l = int(tmp[1]);
            self.totalLength += abs(l) + 2
            self.lengths.append(l)
        
        self.totalLength += 1
        self.printHeader(cols)
        
    def empty(self, *args):
        self.printLine('|')

    def printc(self, col, *args):
        self.printLine('|')
        row = '|'
            
        for i in range(len(self.lengths)) :
            if(self.lengths[i] < 0):
                fmt = ' {:<' + str(abs(self.lengths[i])) + '}|'
            else:
                fmt = ' {:' + str(abs(self.lengths[i])) + '}|'
            row += fmt.format(args[i])
        self.printFunc(color.get(col, row))
        self.pause()

    def print(self, *args):
        self.printLine('|')
        row = '|'
            
        for i in range(len(self.lengths)) :
            if(self.lengths[i] < 0):
                fmt = ' {:<' + str(abs(self.lengths[i])) + '}|'
            else:
                fmt = ' {:<' + str(abs(self.lengths[i])) + '}|'
            row += fmt.format(args[i])
        self.printFunc(row)
        self.pause()
        
    def end(self):
        self.printHeaderLine()

    def printLine(self, sep):
        row = '|'
        cnt = len(self.lengths)
        for i in range(cnt - 1) :
            l = self.lengths[i]
            row += '-' * (abs(l)+1) + sep

        l = self.lengths[cnt - 1]
        row += '-' * (abs(l)+1) + '|'
        self.printFunc(row)
        self.pause()

        
    def printHeader(self, cols):

        self.printHeaderLine()
        row = '|'
        i = 0
        for col in cols:
            fmt = ' {:<' + str(abs(self.lengths[i])) + '}|'
            i += 1
            row += fmt.format(col)
        self.printFunc(row)
        self.pause()
    
    def printHeaderLine(self):
        line ='+' + '-' * (self.totalLength - 2) + '+'
        self.printFunc(line)
        self.pause()

    def pause(self):
        self.count += 1
        if self.count >= (self.lines-1):
            self.count = 0
            get_i('<-more-')
             

    def getSize(self):
        import os
        #rows, columns = os.popen('stty size', 'r').read().split()
        rows=20
        self.lines = int(rows)

class LazyTable(Table):
    t = None
    def __init__(self, *columns):
        self.columns = columns

    def printc(self, col, *args):
        if self.t == None: self.t = Table(*self.columns)
        self.t.printc(col, *args)

    def print(self, *args):
        if self.t == None: self.t = Table(*self.columns)
        self.t.print(*args)

    def end(self):
        if self.t != None: self.t.end()

