
COORDINATES = (30, 30, 250, 250)

# a slice has 2 characters in list form and it's start position
class Slice:
    def __init__(self):
        # characters is list where index 0 represents the inner letter and 
        # index 1 represents the outer letter
        self.characters = []
        self.start_angle = None
        self.position = None
    
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
        canvas.create_text(COORDINATES[0], COORDINATES[1], text=self.characters[0])
        return

    # function to retrieve characters list
    def getChars(self):
        return self.characters
