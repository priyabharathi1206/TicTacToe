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
# displaying the board
def display():
  print("-----------------------")
  print("  ","|" ,store[0], "|" ,store[1] ,"|", store[2] ,"|")
  print("-----------------------")
  print("  ","|" ,store[3], "|", store[4] ,"|", store[5], "|")
  print("-----------------------")
  print("  ","|" ,store[6], "|" ,store[7] ,"|" ,store[8] ,"|")
  print("-----------------------")
#array declaration 
store = [""]*9
#Assigning the value from 1-9
for i in  range(0,9):
  store[i]=i+1
  #print("print ", i ,"and" , store[i])
display()
result=1 # if 0, then won 
i=0
j=0
# for m in range(0,5):

while(result==1):
    if(i<=4 and j<=4):

      while(i<=4):
        # print(i,"When o")
        
        insertIndex = int(input("Enter the number from (1-9) to put O : "))
        if store[insertIndex-1] != "O" and store[insertIndex-1] != "X": 
          store[insertIndex-1]= "O"
          display()
          i+=1
          if((store[0]==store[1]==store[2]=="O")or(store[0]==store[3]==store[6]=="O")or(store[6]==store[7]==store[8]=="O")or(store[2]==store[5]==store[8]=="O")or(store[0]==store[4]==store[8]=="O")or(store[2]==store[4]==store[6]=="O")or(store[1]==store[4]==store[7]=="O")or(store[3]==store[4]==store[5]=="O")):
            print("O player showed the stuff to win")
            print("O won")
            result=0
            break
          else:
            break

          
        else:
          print("It is already filled")
      
      while(j < 4) : 
          # if(j==4):
          #   break
          # print(j ,"when x")
          if (result!=0):
          
            insertIndex = int(input("Enter the number from (1-9) to put X : "))
            if store[insertIndex-1] != "O" and store[insertIndex-1] != "X": 
              
              store[insertIndex-1]= "X"
              display()
              j+=1
              if((store[0]==store[1]==store[2]=="X")or(store[0]==store[3]==store[6]=="X")or(store[6]==store[7]==store[8]=="X")or(store[2]==store[5]==store[8]=="X")or(store[0]==store[4]==store[8]=="X")or(store[2]==store[4]==store[6]=="X")or(store[1]==store[4]==store[7]=="X")or(store[3]==store[4]==store[5]=="X")):
                print("X player showed the stuff to win")
                print("x won")
                result=0
                break
              else:
                break
              
            else:
              print("It is already filled")
          else:
            break
    else:
      
      print("you players showed you have to be in safe zone ")
      print("*******draw******")
      break

# for i in  range(0,9):
#     print(store[i],end= "")









