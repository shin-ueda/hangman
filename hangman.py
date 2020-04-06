import random

word = ["cat", "bat", "bed", "but", "cut"]

def hangman(word):
    wrong = 0
    stages = ["",
                "__________          ",
                "|                   ",
                "|         |         ",
                "|         0         ",
                "|        /|\        ",
                "|        / \        ",
                "|                   ",
                ]
    rltters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rltters:
            cind = rltters.index(char)
            board[cind] = char
            rltters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

num = random.randint(0, len(word) - 1)
hangman(word[num])