from .__init__ import WIDTH, HEIGHT

CHARACTERS = [
    " ",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",

    "?",
    "\n"
]


class Display:

    def __init__(self):

        self.__content__ = [["0"] * WIDTH] * HEIGHT

    def __printcontent__(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                try:
                    value = int(self.__content__[y][x])
                except ValueError:
                    value = -2

                print(CHARACTERS[value], end="")

            print(CHARACTERS[-1], end="")

    def show(self, image):
        self.__content__ = image.__returncontent__().copy()
        self.__printcontent__()

display = Display()
