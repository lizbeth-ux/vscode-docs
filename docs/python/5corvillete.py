class Board:
    def __init__(self, size, colors):
        self.size = size
        self.colors = colors

    def move(self, player, color):
        # Find the index of the first square with the given color
        index = self.colors.find(color)
        # If the color is not found, move to the last square
        if index == -1:
            index = self.size - 1
        # If the player is already on the last square, do not move
        if index == self.size - 1:
            return
        # Move the player to the next square with the given color
        while self.colors[index] != color:
            index = (index + 1) % self.size
        player.position = index

class Game:
    def __init__(self, num_players, board_size, deck):
        self.num_players = num_players
        self.board = Board(board_size, "RGBYP" * (board_size // 5))
        self.deck = [card.upper() for card in deck]
        self.players = [Player(i) for i in range(num_players)]

    def play(self):
        num_cards_used = 0
        while self.deck or any(player.position != self.board.size - 1 for player in self.players):
            for player in self.players:
                if not self.deck:
                    break
                color = self.deck.pop(0)
                self.board.move(player, color)
                num_cards_used += 1
        if any(player.position != self.board.size - 1 for player in self.players):
            print(f"Ningun jugador gano despues de {num_cards_used} paquetes de cartas")
        else:
            winner = next(player for player in self.players if player.position == self.board.size - 1)
            print(f"Jugador {winner.number} gano despues de {num_cards_used} paquetes de cartas")

class Player:
    def __init__(self, number):
        self.number = number
        self.position = 0

# Read the input
num_games = 1
while True:
    line = input().split()
    if line[0] == "0":
        break
    num_players, board_size, num_cards = int(line[0]), int(line[1]), int(line[2])
    if num_games > 1:
        print()
    board_colors = input()
    deck = input().split()
    game = Game(num_players, board_size, deck)
    game.play()
    num_games += 1