'''
Created on 20-Feb-2020

@author: ibright
'''
import Category
import Menu
from Picture import *
from table import *
import random
from IO import *
class Game():

    def __init__(self):
        self.catMenuTitle = "Play again in the '{}' category"
        self.MAX_TRIES=6
        self.debug = False
        self.numGames = 0
        self.gamesWon = 0

    def start_game(self):
        self.run()

    def run(self):
        self.cat = Category.Category()
        self.cat_name = self.cat.get_category()
        if self.cat_name == None: return
        self.run_game()

        def go_back():
            return Menu.MenuStatus.DONE

        def new_category():
            try:
                self.cat_name = self.cat.get_category()
                if self.cat_name == None: return Menu.MenuStatus.OK
                self.run_game()
                self.cat_menu_item.set_title(self.catMenuTitle.format(self.cat_name))

            except Exception as e:
                print_error(e)
            return Menu.MenuStatus.OK

        def same_category():
            self.run_game()
            return Menu.MenuStatus.OK

        men = Menu.MenuX("Hangman:Menu")
        self.cat_menu_item = Menu.MenuItem(self.catMenuTitle.format(self.cat.get_name()), same_category)
        men.add(self.cat_menu_item)
        men.add(Menu.MenuItem("Change category", new_category))
        men.add(Menu.MenuItem("Go Back", go_back))
        while men.run() == Menu.MenuStatus.OK : pass

    def run_game(self):
        self.game()
        self.report_game_stats()
        pause()

    def game(self):
        self.word = self.cat.get_random_word()
        if self.word == None: return
        self.word = self.word.upper()
        self.numGames += 1
        self.tries = ""
        self.lines = self.get_guess_line()
        self.letter = " "
        self.lines = self.replace_letter()
        self.numTries = 0
        self.catName = self.cat.get_name()

        while self.numTries < self.MAX_TRIES:
            print_hangman(self.numTries)
            self.show_game_board()
            if self.debug:
                print_info(self.word)
            answer = read_string("\nEnter a letter or word")
            answer = answer.upper()

            if len(self.word)<len(answer):
                print_error("You have entered more then answer please take serious.If you not play well hangman will kill you")
                pause()
                continue

            if answer == "?":
                answer = self.get_clue()
                self.numTries += 2
            chars = ""

            for a in answer:
                chars += a
            reportDup = len(chars) == 1

            for self.letter in chars:
                if self.letter.isalpha() == False:
                    pause("Enter Letters only please")
                    continue

                if self.letter in self.tries:
                    if reportDup : pause(f'You entered {self.letter} already')
                    continue

                self.tries += self.letter + " "

                if self.letter not in self.word:
                    self.numTries += 1
                else:
                    self.lines = self.replace_letter()
                    if self.lines == self.word:
                        print_hangman(WON)
                        self.show_game_board()
                        print_info('Congratulations! You won!')
                        self.gamesWon += 1
                        return

        print_hangman(LOST)
        self.show_game_board()
        print_red("Well, Try next time.The word was:"+self.word)

    def replace_letter(self):
        temp = []
        for l in self.lines:
            temp += l
        i=0
        while i < len(self.word):
            if self.word[i] == self.letter:
                temp[i] = self.letter
            i += 1
        # traverse in the string
        new = ""
        for x in temp:
            new += x
        return new

    def get_guess_line(self):
        self.lines = ''
        i = 0
        while i < len(self.word):
            ch = self.word[i]
            if (ch.isalpha()):
                self.lines = self.lines + '*'
            else:
                self.lines = self.lines + ch
            i += 1
        return self.lines

    def show_game_board(self):
        t=Table ('Category:20',f'{self.catName}:30')
        t.print('Your Guess',str(self.lines))
        t.print('Letters guessed',self.tries)
        t.end()

    def get_clue(self):
        empty = []
        i = 0
        while i < len(self.lines):
            if self.lines[i] == '*':
                empty.append(i)
            i += 1
        if len(empty) == 0: return None
        rnd=random.choice(empty)
        return self.word[rnd]

    def report_game_stats(self):
        t=Table('Number of game played:35',f'{self.numGames}:10')
        t.print("Number of games you won",self.gamesWon)
        if self.numGames > 0:
            self.win = (self.gamesWon / self.numGames) * 100
            t.print('Win %',f"{self.win:,.2f}")
        t.end()

