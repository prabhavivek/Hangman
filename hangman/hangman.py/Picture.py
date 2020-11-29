'''
Created on 08-Feb-2020

@author: ibright
'''
from Constants import *
from IO import *
from Constants import *
LOST = 6
LOGO = 6
WON = 7

def print_hangman(picNum):
    empty = "\n"
    left = "|\n"
    top = "------------    \n"
    top1 = "-------+----    \n"
    head = "|     ( )       \n"
    body = "|      |      \n"
    leftHand = "|     /|      \n"
    rightHand = "|     /|\\      \n"
    rightHand1 = "|     \\O/      \n" +   "|      |\n"
    leftLeg = "|     /      \n"
    rightLeg = "|     / \\      \n"
    bench = "|  |-------|    \n"
    footer = "---|-------|----\n"
    footer1 = " Y O U  W O N !! \n"
    
    pictures = [
                # 0
                top + 
                left + 
                left + 
                left + 
                left + 
                left + 
                bench + 
                footer,
                
                # 1
                top1 + 
                head + 
                left + 
                left + 
                left + 
                left + 
                bench + 
                footer,
                
                # 2
                top1 + 
                head + 
                body + 
                left + 
                left + 
                left + 
                bench + 
                footer,
                
                # 3
                top1 + 
                head +
                leftHand + 
                left + 
                left +
                left +
                bench + 
                footer,
                
                 # 4
                top1 + 
                head + 
                rightHand + 
                left + 
                left +
                left +
                bench + 
                footer,
                
                # 5
                top1 + 
                head + 
                rightHand + 
                leftLeg + 
                left +
                left +
                bench + 
                footer,
                
                # LOGO: 6
                top1 + 
                head + 
                rightHand + 
                rightLeg + 
                left + 
                left + 
                bench + 
                footer,
                
                # WON: 7
                top + 
                left + 
                left + 
                left +
                left +
                rightHand1 + 
                rightLeg + 
                footer1,
            
        
        ]

    if(picNum < 0 or picNum >= len(pictures)):
        print_error(INCORRECT_NUM_ERRORS)
        return

    clear_screen()

    if picNum == WON:
        print_title(f"{3*' '}{APP_NAME}")
        print_blue(empty + pictures[picNum] + empty)
    else:
        print_title(f"{3*' '}{APP_NAME}")
        print_red(empty + pictures[picNum] + empty)
