print("------------")
print("Tic Tae Toe")
print("------------")

print(""" 
    ----------------------
      |    |     |    |
    ---------------------- 
      |    |     |    |
    ----------------------
      |    |     |    |
    ----------------------
      """)

def display():
  print("-----------------------")
  print("  ","|" ,store[0], "|" ,store[1] ,"|", store[2] ,"|")
  print("-----------------------")
  print("  ","|" ,store[3], "|", store[4] ,"|", store[5], "|")
  print("-----------------------")
  print("  ","|" ,store[6], "|" ,store[7] ,"|" ,store[8] ,"|")
  print("-----------------------")
#array creation
store = [""]*9
#displaying  the initalization as 1st 
for i in  range(0,9):
    print("print ", i ,"and" , store[i])
#simple condition
for i in range(0,5):

    insertIndex = int(input("Enter the number from (0-8) to put O : "))
    store[insertIndex]= "O"
    display()
    if((store[0]==store[1]==store[2]=="O")or(store[0]==store[3]==store[6]=="O")or(store[6]==store[7]==store[8]=="O")or(store[2]==store[5]==store[8]=="O")or(store[0]==store[4]==store[8]=="O")or(store[2]==store[4]==store[6]=="O")or(store[1]==store[4]==store[7]=="O")or(store[3]==store[4]==store[5]=="O")):
      print("O won")
      break
    # only 4 turn for x
    if(i !=4):
        insertIndex = int(input("Enter the number from (0-8) to put X : "))
        store[insertIndex]= "X"
        display()
        if((store[0]==store[1]==store[2]=="X")or(store[0]==store[3]==store[6]=="X")or(store[6]==store[7]==store[8]=="X")or(store[2]==store[5]==store[8]=="X")or(store[0]==store[4]==store[8]=="X")or(store[2]==store[4]==store[6]=="X")or(store[1]==store[4]==store[7]=="X")or(store[3]==store[4]==store[5]=="X")):
          print("X won")
          break
    
#displaying the array
for i in  range(0,9):
    print(store[i],end= "")









