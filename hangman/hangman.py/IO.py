'''
Created on 10-Feb-2020

@author: ibright
'''
from color import *

richText = False

def print_title(msg):
    print(get(green, msg))

def print_error(errmsg):
    print(get(red, errmsg))
    
def print_blue(msg):
    print(get(blue, msg))
    
def print_red(msg):
    print(get(red, msg))
    
def print_info(info):
    print(get(blue, info))

def print_under(info):
    print(get(underlne, info))

def get_inp(prompt, mn='', mx=''):
    if mn != '' and  mx != '':
        while True:
            try:
                ret = int(input(prompt + ' >'))
                if mn > ret or mx < ret:
                    print_error('\n   Enter a number between %d and %d' %(mn, mx))
                else:
                    return ret
            except:
                print_error(f"\n{' '*3}Not a valid input. Try again")
    else:return int(input(prompt + ">"))

def read_boolean(prompt):

    return read_string(prompt) in ['y','yes','sure','yeah','yup','si','oui']

def read_string(prompt):
    return input(prompt + '>')

def pause(msg=''):
    if msg!='':
        print(msg)
    input('\nEnter to continue >')

    
def get_i(prompt, d = ''):
    p = prompt
    if d != '':
        p += ' [' + str(d) + ']'
    p += '> '
    s = input(p)
    if not s:
        return d
    return s.strip()

def set_rich_text(rt):
    global richText
    richText = rt


def clear_screen():
    if not richText: return
    print("\033\143")

