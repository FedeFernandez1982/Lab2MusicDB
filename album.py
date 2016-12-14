
class Album:

    def __init__(self, artist, title, genre):
        self.artist = artist
        self.title = title
        self.genre = genre

    def getartist (self):
        return self.artist

    def setartist (self, artist):
        self.artist = artist

    def gettitle (self):
        return self.title

    def settitle (self, title):
        self.title = title

    def getgenre(self):
        return self.genre

    def setgenre(self, genre):
        self.genre = genre

    def __repr__(self):
        self.str_repr = self.artist + '\t' + self.title + '\t' + self.genre
        return self.str_repr
