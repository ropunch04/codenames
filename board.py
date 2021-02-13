class Board():
    def __init__(self, size):
        self.size = size
        self.setBoard()
    
    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for _ in range(self.size[1]):
                word = ["Test", "hello", "hola", "afdf"]
                row.append(x for x in word)
            self.board.append(row)
        print(self.board)
