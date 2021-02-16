def view(lis):
    print("---------")
    print(f"| {lis[0]} {lis[1]} {lis[2]} |")
    print(f"| {lis[3]} {lis[4]} {lis[5]} |")
    print(f"| {lis[6]} {lis[7]} {lis[8]} |")
    print("---------")

def not_finished(lis_check):
    """when neither side has three in a row but the grid still has empty cells."""
    if "_" in lis_check:
        return True
    else:
        return False

def winning(lis_check, checker):
    """when the grid has three X or O"""
    for n in range(0, 9, 3):
        if lis_check[n] == checker and lis_check[n] == lis_check[n+1] and lis_check[n] == lis_check[n+2]:
            return True
    for n in range(3):
        if lis_check[n] == checker and lis_check[n] == lis_check[n+3] and lis_check[n] == lis_check[n+6]:
            return True
    if lis_check[0] == checker and lis_check[0] == lis_check[4] and lis_check[0] == lis_check[8]:
        return True
    if lis_check[2] == checker and lis_check[2] == lis_check[4] and lis_check[2] == lis_check[6]:
        return True
    return False

def impossible(lis_check):
    """Returns True when the grid has three X’s in a row as well as three O’s in a row, 
    or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; 
    if the difference is 2 or more, then the game state is impossible)."""
    #check if there are 2 winners
    if winning(lis_check, 'O') and winning(lis_check, 'X'):
        return True
    #check if totals are too far.
    totalO = 0
    totalX = 0
    for k in lis_check:
        if k == 'O':
            totalO += 1
        if k == 'X':
            totalX += 1
    if totalO > totalX + 1:
        return True
    if totalX > totalO + 1:
        return True
    return False

def check_results(lis_check):
    """Final checker returns string"""
    if impossible(lis_check):
        return True, ('Impossible')
    if winning(lis_check, 'O'):
        return True, ('O wins')
    if winning(lis_check, 'X'):
        return True, ('X wins')
    if not_finished(lis_check):
        return False, ("Game not finished yet!")
    else:
        return True, ("Draw")

def return_index(double):
    """Converts [1, 3] to  index"""
    if double[0] == 1:
        return double[1] - 1
    elif double[0] == 2:
        return double[1] + 2
    elif double[0] == 3:
        return double[1] + 5
    else:
        print("number is too big")
        
def check_if_empty(lis, double):
    num_index = return_index(double)
    if lis[num_index] not in "XO":
        return True
    else:
        return False
    
def make_move(lis, player):
    """Player move phase"""
    print("Player \"" + player + "\" makes a move")
    #inputing and checking
    while True:
        coordinates = input('Enter the coordinates:').split()
        try:
            #check if coordinates are numbers
            coordinates = ([int(num) for num in coordinates])
            #check if only 2 coordinates
            if len(coordinates) > 2:
                print("You should enter 2 numbers only!")
                continue
            #check if coordinates are not to big
            if coordinates[0] > 3 or coordinates[0] < 1 or  coordinates[1] > 3 or coordinates[1] < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            if not check_if_empty(lis, coordinates):
                print("This cell is occupied! Choose another one!")
                continue
            break
        except: 
            print("You should enter numbers!")
            continue
    index = return_index(coordinates)
    new_string = lis[:index] + player + lis[index + 1:]
    return new_string

def swap_player():
    if player == 'X':
        return 'O'
    else:
        return 'X'

#starting point
lis = "_________"
view(lis)
player = 'X'


while True:
    lis = make_move(lis, player) 
    view(lis)
    
    end, printout = check_results(lis)
    print(printout)
    if end:
        break
    player = swap_player()

