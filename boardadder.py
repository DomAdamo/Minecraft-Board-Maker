def boardAdd():
    i = input("Type:  ")
    while not i == "q" :
        with open("bingoList.txt","a") as f:
            with open("bingoList.txt","r") as m:
                x = int(m.read().replace("\n",",").split(",")[-1])
                if not i in str(m.read()):
                    f.write("\n"+i.lower()+","+str(x+1))
        i = input("Type:  ")