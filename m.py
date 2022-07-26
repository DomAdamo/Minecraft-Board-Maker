from random import randint

with open("bingoList.txt","r") as list:
    things = str(list.read())
print(things)
numboards = 5

board = [["" for c in range(5)] for r in range(5)]


def remove(h):
    x = randint(0, len(h) - 1)
    m = h[x]
    things[x]
    try:
        return str(m)[0] + str(m)[1]
    except:
        return str(m)[0]+" "


def p(g):
    print(" " + str(g)[1:][:-1].replace("],", "],\n"))


for i in range(numboards):
    T = things
    board = [[remove(T) for c in range(5)] for r in range(5)]
    p(board)
    print("")
