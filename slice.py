
COORDINATES = (30, 30, 250, 250)
slice_num = 0
SLICE_COORD = 0

# a slice has 2 characters in list form and it's start position
class Slice:
    def __init__(self):
        # characters is list where index 0 represents the inner letter and
        # index 1 represents the outer letter
        self.characters = []
        self.start_angle = None
        self.position = None
        #self.slice_num = 0


    # function to actually draw the slice on the screen
    def draw(self, canvas, color, extent):
        canvas.create_arc(COORDINATES, start=self.start_angle, extent=extent, fill=color)
        return

    # function that sets a slice's starting angle (for draw)
    def setStartingAngle(self, start):
        self.start_angle = start
        return

    # function to set the characters inside this slice
    def setCharacters(self, char):
        self.characters = char

    # function to return an inner or outer character based on user input
    def getCharacter(self, number):
        return self.characters[number]

    # function to display the characters on the screen inside the slice
    def drawCharacters(self, canvas):
        #if SLICE_NUM == 0:
        # Upper half
        # INNER
        if slice_num == 5:
            canvas.create_text(90, 125, text=self.characters[0])
        elif slice_num == 6:
            canvas.create_text(110, 100, text=self.characters[0])
        elif slice_num == 7:
            canvas.create_text(143, 90, text=self.characters[0])
        elif slice_num == 8:
            canvas.create_text(167, 100, text=self.characters[0])
        elif slice_num == 9:
            canvas.create_text(190, 125, text=self.characters[0])
        elif slice_num == 0:
            canvas.create_text(90, 140, text=self.characters[0])

        # OUTER
        if slice_num == 5:
            canvas.create_text(70, 120, text=self.characters[1])
        elif slice_num == 6:
            canvas.create_text(95, 85, text=self.characters[1])
        elif slice_num == 7:
            canvas.create_text(143, 70, text=self.characters[1])
        elif slice_num == 8:
            canvas.create_text(178, 80, text=self.characters[1])
        elif slice_num == 9:
            canvas.create_text(210, 120, text=self.characters[1])
        elif slice_num == 0:
            canvas.create_text(110, 130, text=self.characters[1])


        # canvas.create_text(200, 100, text=self.characters[1])
        return

    # function to retrieve characters list
    def getChars(self):
        return self.characters
