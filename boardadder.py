
i = input("Type:  ")
while not i == "q" :
    with open("bingoList.txt","a") as f:
        with open("bingoList.txt","r") as m:
            if not i in str(m.read()):
                f.write(i+"\n")
    i = input("Type:  ")