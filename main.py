from notebook import Notebook
import sys

DIVIDER = 80*'='
NOTEBOOK = Notebook()
ACTIONS = [
    ("Show all notes", 'show_notes'), 
    ("Search notes", 'search_notes'), 
    ("Add note", 'create_note'), 
    ("Modify note", 'modify_note'), 
    ("Quit", 'quit')
    ]

class Display:
    def __init__(self, actions=None):
        if __name__ == '__main__':
            if (not actions):
                actions = ACTIONS
            while True:
                print(DIVIDER)
                self.menu(actions)
                command = int(input("Enter an option: "))-1
                if command < len(actions):
                    print()
                    print(DIVIDER)
                    print()
                    function = getattr(self, actions[command][1])
                    function()
                else:
                    print(f"{command+1} is not a valid choice")

    def menu(self, actions):
        print("\nNotebook Menu:")
        num = 0
        for i in actions:
            num += 1
            print(str(num)+'. '+i[0])
        print()

    def show_notes(self):
        NOTEBOOK.show_notes()

    def create_note(self):
        memo = input("Enter a memo: ")
        tag = input("Enter tag: ")
        NOTEBOOK.create_note(memo, tag)
        print("Your note has been added.\n")

    def search_notes(self):
        filter = input("Search for: ")
        find = NOTEBOOK.search(filter)
        NOTEBOOK.show_notes(find)

    def modify_note(self):
        id = int(input("Enter a note id: "))
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        print()
        NOTEBOOK.modify(id, memo, tags)

    def quit(self):
        print("Thank you for using your Notebook today.\n")
        sys.exit(0)

if __name__ == '__main__':
    Display()

