'''
Created on 11-Feb-2020

@author: ibright
'''
import yaml
from Constants import *
from IO import *
import random

class Category():
    def __init__(self):
        self.CAT_FILE = CAT_FILE
        self.data = self.yaml_loader()
        self.files = []
        self.cats = []
        for key, value in self.data.items():
            self.files.append(key)
            self.cats.append(value)

    def get_category(self):
        """Load a yaml file"""
        clear_screen()
        print_title('Categories\n')
        idx = 0
        print('%4d. %s'% (idx,'Go Back'))
        idx = 1
        for key in self.cats:
            print('%4d. %s'% (idx, key))
            idx += 1
        idx = get_inp('\nSelect a category',0,len(self.cats))
        if idx == 0:return None
        self.cat = self.cats[idx-1]
        self.file = self.files[idx-1]
        self.load_category()
        return self.cat
    
    def yaml_loader(self):
        with open(self.CAT_FILE,'r') as file_descripter:
            return yaml.load(file_descripter) 

    def load_category(self):
        self.name=self.cat
        self.load_dictionary()
    
    def load_dictionary(self):
        try:
            self.lines=[]
            with open(self.file+'.txt') as f:
                for self.line in f:
                    self.lines.append(self.line)
            if len(self.lines)==0:
                print_error('Empty words file:' + self.file)
        except FileNotFoundError:
            print_error('Dictionary not found :'+self.file)
        
    def get_random_word(self):
        if len(self.lines) <=0:
            return None
        else:
            words=self.lines
            rnd = random.choice(words)
            words.remove(rnd)
            return  rnd.strip()

    def get_name(self):
        return self.name


        
