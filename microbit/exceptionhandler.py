import sys

def handler(type, value, traceback):
    if type == KeyboardInterrupt:
        print() # print newline to satisfy zsh
    else:
        sys.__excepthook__(type, value, traceback)
        
    return

sys.excepthook = handler