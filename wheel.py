import random
import slice as s

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
        # dictionary to keep track of which color is at which slice
        self.pairings = {}
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
        print(self.colors)
        print(self.characters)
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
            self.slices[i].setStartingPosition(start)
            self.slices[i].draw(canvas, rand_color, extent)
            # add pairing to dictionary (color: Slice)
            self.pairings[rand_color] = self.slices[i]

            # testing
            print("slice " + str(i))
            print(self.slices[i].getChars())
            print(rand_color)

            # set start for next slice
            start += extent
            
        return

    # function to change pairings of colors and slices when user rotates wheel
    # also need to redraw!!
    def updateColorsSlices(self, canvas):
        return



    