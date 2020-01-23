import random
from collections import OrderedDict
import slice as s
import time

COORDINATES = (30, 30, 250, 250)

# a class that contains a list of colors, password characters, and Slice classes
# manages all the slices and takes care of wheel big picture stuff
class Wheel:
    def __init__(self):
        self.colors = ["red2", "DarkOrange1", "blue", "forest green", "purple1", "white", "saddle brown"
                      , "dark turquoise", "yellow", "dim gray"]
        self.slices = []
        self.characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
                          , "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        # ordered dictionary to keep track of which color is at which slice
        self.pairings = OrderedDict()
        # could possibly change number of slices
        # used to calculate the extent to draw the arcs
        self.number_of_slices = 10

        # populate slices list
        self.makeSlices()

    # function to create Slice instances for self.slices
    def makeSlices(self):
        for i in range(self.number_of_slices):
            slice = s.Slice()
            self.slices.append(slice)

    # function that creates the wheel by looping through slices,
    # assigning colors and characters, and calling their draw function
    def create(self, canvas):
        # make copy of colors and characters list
        # for randomly choosing and removing (don't want to modify original)
        colors_copy = self.colors.copy()
        chars_copy = self.characters.copy()

        # calculate the "extent" for drawing arc
        extent = 360 / self.number_of_slices
        start = 0

        for i in range(self.number_of_slices):
            # randomly choose a color and two characters to give to each slice
            rand_color = random.choice(colors_copy)
            colors_copy.remove(rand_color)
            rand_char1 = random.choice(chars_copy)
            chars_copy.remove(rand_char1)
            rand_char2 = random.choice(chars_copy)
            chars_copy.remove(rand_char2)

            # assign to slice and draw slice
            self.slices[i].setCharacters([rand_char1, rand_char2])
            self.slices[i].setStartingAngle(start)
            self.slices[i].draw(canvas, rand_color, extent)
            self.slices[i].drawCharacters(canvas)

            # add pairing to dictionary (color: Slice)
            self.pairings[rand_color] = self.slices[i]
            s.SLICE_NUM += 1

            # set start for next slice
            start += extent
            #s.SLICE_NUM += 1

        # debug
        for color, slice in self.pairings.items():
            print(color + " " + slice.getChars()[0] + " " + slice.getChars()[1] + '\n')

        return

    # function to change pairings of colors and slices when user rotates wheel
    # also redraws the wheel to seem like it is rotating
    def updateColorsSlices(self, canvas, direction):
        # get self.pairings keys list and values list
        colors = list(self.pairings.keys())
        slices = list(self.pairings.values())

        # rotate colors array
        if direction == 1:
            # right rotate
            rotated = colors[1:] + [colors[0]]

        if direction == -1:
            # left rotate
            rotated = colors[-1:] + colors[:-1]

        # reset pairings of colors and slices
        self.pairings = OrderedDict(zip(rotated, slices))

        # redraw rotated wheel on screen
        # calculate the "extent" for drawing arc
        extent = 360 / self.number_of_slices
        start = 0

        s.SLICE_NUM = 0
        for color, slice in self.pairings.items():
            slice.setStartingAngle(start)
            slice.draw(canvas, color, extent)
            slice.drawCharacters(canvas)
            s.SLICE_NUM += 1

            start += extent

            # debug
            # print(color + " " + slice.getChars()[0] + " " + slice.getChars()[1] + '\n')



        return



    # function to retrieve a character from a slice given a color and index
    def getCharacter(self, color, index):
        slice = self.pairings[color]
        return slice.getCharacter(index)


    # function that returns the slice that has the given color
    def getSlice(self, color):
        # print(self.pairings)
        return self.pairings[color]
