from .__init__ import WIDTH, HEIGHT


class Image:

    def __init__(self, content=None):

        self.__content__ = []

        for y in range(HEIGHT):
            for x in range(WIDTH):
                self.__content__.append(list("0") * WIDTH)

        if content:
            split = content.split(":")
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    self.__content__[y][x] = split[y][x]

    def __returncontent__(self):
        return self.__content__
