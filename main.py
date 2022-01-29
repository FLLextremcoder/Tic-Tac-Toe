#1d array
something = [1, 2]
print (something)

#2d array
Arrow = [['-', '-','-'], ['-', '-', '-'], ['-', '-' , '-']]
print (Arrow)


def printBoard(Arrow):

    for i in range(3):
        print("")
        for j in range(3):
            print(Arrow[i][j], end="", flush=True)
            

print ("")
player = "X"
for i in range (9):
    print("")
    print("please enter the X coordinate, ", player, " Turn")
    Xcoordinate = input()
    print("please enter the Y coordinate, ", player, " Turn")
    Ycoordinate = input()
    Arrow[int(Xcoordinate)][int(Ycoordinate)] = player
    if(player =="X"):
        player = 'O' #next turn
    elif(player == 'O'):
        player = 'X' #next turn
        
    printBoard(Arrow)
    counter =0
    for i in range(3):
        print("")
        for j in range(3):
            if(Arrow[i][j] =='X'):  
                counter = counter + 1
            if(counter == 3):
                print("X wins")  
                break  


    counter =0
    for i in range(3):
        print("")
        for j in range(3):
            if(Arrow[i][j] =='Y'):  
                counter = counter + 1
            if(counter == 3):
                print("Y wins")  
                break              