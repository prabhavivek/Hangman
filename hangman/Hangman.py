'''
Created on 05-Feb-2020

@author: ibright
'''
from IO import *
from Picture import *
from Constants import *
from Menu import *
from Game import *
import sys

g = Game()
def main():
    try:
        # Process on commend line argument
        if len(sys.argv) > 1:
            if sys.argv[1] == '-rt':
                set_rich_text(True)

        # Print hangman logo
        print_hangman(LOGO)

        # Ask to the player want to play
        if not read_boolean(WANT_TO_PLAY):
            print(BYE)
            return
        main_menu()
        end()

    except Exception as e:
        print_error(SOMETHING_WRONG + e)

def main_menu():
    def new_game():
        try:
            g.start_game()
        except Exception as e:
            print(e)
        return MenuStatus.OK

    def show_game_stats():
        g.report_game_stats()
        return MenuStatus.OK

    def print_help():
        help()
        return MenuStatus.OK

    def done():
        print_info(HOPE_YOU_ENJOYED)
        return MenuStatus.DONE

    menu = MenuX('Hangman: Main Menu')
    menu.add(MenuItem(NEW_GAME, new_game))
    menu.add(MenuItem(GAME_STATS, show_game_stats))
    menu.add(MenuItem(HELP, print_help))
    menu.add(MenuItem(DONE_PLAYING, done))

    while menu.run() == MenuStatus.OK: pause()

def end():
    g.report_game_stats()

def help():
    print_under('\nHelp:')
    print(' '*4,'You can enter one or more letters')
    print(' '*4,'Enter ? to get a clue. This will take 2 points')

if __name__ == '__main__':
    main()

