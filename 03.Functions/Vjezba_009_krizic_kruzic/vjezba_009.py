"""
Napraviti ploču
Svako polje označiti brojem
Kada se odabere polje zamijeniti ga odgovarajućim znakom
Definirati koji igrač je koji znak
Postaviti uvjete za pobjedu koji se provjeravaju
"""

"""
PSEUDO KOD:
Ispis ploče:
    Definirati listu s brojevima od 1 do 9
    Ispisati sve brojeve iz liste tako da su po tri u redu
    Dodati crte između brojeva da izgleda kao matrica 

"""


def tic_tac_toe_board(board):
    """
    Funkcija koja iscrtava ploču
    """
    print("Dobrodošli u igru križić kružić.")
    print()
    print("\t\t|\t\t|\t\t")
    print(f"\t{board[1]}\t|\t{board[2]}\t|\t{board[3]}\t")
    print("\t\t|\t\t|\t\t")
    print("-" * 51)
    print("\t\t|\t\t|\t\t")
    print(f"\t{board[4]}\t|\t{board[5]}\t|\t{board[6]}\t")
    print("\t\t|\t\t|\t\t")
    print("-" * 51)
    print("\t\t|\t\t|\t\t")
    print(f"\t{board[7]}\t|\t{board[8]}\t|\t{board[9]}\t")
    print("\t\t|\t\t|\t\t")

def tic_tac_toe_game(board):
    """
    Funkcija koja izvršava igru
    """
    game_status = ""
    user_number = 1
    while game_status != "stop":
        tic_tac_toe_board(board)
        # if user_number % 2 == 1:
        #     print("Na redu je Igrač 1")
        # else:
        #     print("Na redu je Igrač 2")
        field = int(input("Upiši broj polja na koji želiš postaviti znak: "))
        if user_number % 2 == 1:
            user_sign = "X"
        else:
            user_sign = "O"
        
        if field == 1 and board[1] == 1:
            board[1] = user_sign
        elif field == 2 and board[2] == 2:
            board[2] = user_sign
        elif field == 3 and board[3] == 3:
            board[3] = user_sign
        elif field == 4 and board[4] == 4:
            board[4] = user_sign
        elif field == 5 and board[5] == 5:
            board[5] = user_sign
        elif field == 6 and board[6] == 6:
            board[6] = user_sign
        elif field == 7 and board[7] == 7:
            board[7] = user_sign
        elif field == 8 and board[8] == 8:
            board[8] = user_sign
        elif field == 9 and board[9] == 9:
            board[9] = user_sign
        else:
            print("Polje je već odabrano. Probajte ponovo.")
        user_number += 1
        game_status = game_result(board)
        if game_status == "Pobjeda" or game_status == "Nerješeno":
            tic_tac_toe_board(board)
            pick = ""
            while pick != "da" and pick != "ne":
                pick = input("Želite li igrati ponovo (Da/Ne)? ").lower()
                if pick == "da":
                    game_status = ""
                    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                elif pick == "ne":
                    game_status = "stop"
                else:
                    print("Pogrešan unos. Probajte ponovo!")

def game_result(board):
    """
    Funkcija za provjeru rezultata igre
    """
    if board[1] == board[2] and board[2] == board[3]:
        return "Pobjeda"
    elif board[4] == board[5] and board[5] == board[6]:
        return "Pobjeda"
    elif board[7] == board[8] and board[8] == board[9]:
        return "Pobjeda"
    elif board[1] == board[4] and board[4] == board[7]:
        return "Pobjeda"
    elif board[2] == board[5] and board[5] == board[8]:
        return "Pobjeda"
    elif board[3] == board[6] and board[6] == board[9]:
        return "Pobjeda"
    elif board[1] == board[5] and board[5] == board[9]:
        return "Pobjeda"
    elif board[3] == board[5] and board[5] == board[7]:
        return "Pobjeda"
    elif board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8 and board[9] != 9:
        return "Nerješeno"
    else:
        return ""
    
board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

tic_tac_toe_game(board)