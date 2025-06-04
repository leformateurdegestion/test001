import sys

BOARD_SIZE = 3

# Initialize empty board
board = [[[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Precompute all winning lines
lines = []
# Lines along axes
for x in range(BOARD_SIZE):
    for y in range(BOARD_SIZE):
        lines.append([(x, y, z) for z in range(BOARD_SIZE)])
for x in range(BOARD_SIZE):
    for z in range(BOARD_SIZE):
        lines.append([(x, y, z) for y in range(BOARD_SIZE)])
for y in range(BOARD_SIZE):
    for z in range(BOARD_SIZE):
        lines.append([(x, y, z) for x in range(BOARD_SIZE)])
# Diagonals in planes
for z in range(BOARD_SIZE):
    lines.append([(i, i, z) for i in range(BOARD_SIZE)])
    lines.append([(i, BOARD_SIZE-1-i, z) for i in range(BOARD_SIZE)])
for x in range(BOARD_SIZE):
    lines.append([(x, i, i) for i in range(BOARD_SIZE)])
    lines.append([(x, i, BOARD_SIZE-1-i) for i in range(BOARD_SIZE)])
for y in range(BOARD_SIZE):
    lines.append([(i, y, i) for i in range(BOARD_SIZE)])
    lines.append([(i, y, BOARD_SIZE-1-i) for i in range(BOARD_SIZE)])
# Space diagonals
lines.append([(i, i, i) for i in range(BOARD_SIZE)])
lines.append([(i, i, BOARD_SIZE-1-i) for i in range(BOARD_SIZE)])
lines.append([(i, BOARD_SIZE-1-i, i) for i in range(BOARD_SIZE)])
lines.append([(BOARD_SIZE-1-i, i, i) for i in range(BOARD_SIZE)])


def print_board():
    for z in range(BOARD_SIZE):
        print(f"Couche {z+1}")
        for y in range(BOARD_SIZE):
            row = []
            for x in range(BOARD_SIZE):
                row.append(board[x][y][z])
            print(' | '.join(row))
            if y < BOARD_SIZE - 1:
                print('-' * (BOARD_SIZE * 4 - 3))
        print()


def check_win(player):
    for line in lines:
        if all(board[x][y][z] == player for x, y, z in line):
            return True
    return False


def board_full():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            for z in range(BOARD_SIZE):
                if board[x][y][z] == ' ':
                    return False
    return True


def main():
    players = ['X', 'O']
    current = 0

    while True:
        print_board()
        player = players[current]
        try:
            coords = input(f"Joueur {player}, entrez les coordonnées x y z (1-3) séparées par des espaces: ")
        except EOFError:
            print()
            return
        parts = coords.strip().split()
        if len(parts) != 3:
            print("Entrée invalide. Veuillez fournir trois nombres.")
            continue
        try:
            x, y, z = (int(p)-1 for p in parts)
        except ValueError:
            print("Entrée invalide. Veuillez fournir des nombres.")
            continue
        if not all(0 <= v < BOARD_SIZE for v in (x, y, z)):
            print("Coordonnées hors limites. Utilisez des valeurs entre 1 et 3.")
            continue
        if board[x][y][z] != ' ':
            print("Case déjà prise. Choisissez-en une autre.")
            continue
        board[x][y][z] = player
        if check_win(player):
            print_board()
            print(f"Le joueur {player} a gagné!")
            return
        if board_full():
            print_board()
            print("Match nul!")
            return
        current = 1 - current


if __name__ == "__main__":
    main()
