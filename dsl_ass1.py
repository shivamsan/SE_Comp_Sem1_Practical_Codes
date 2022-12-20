def TakeInput(Sport):
 players = int(input(f'Enter how many players playing {Sport}:'))
 array = ['name'] * players
 for i in range(0,players):
    array[i]=input("Enter the name of players:")
 return array
Cricket=TakeInput("Cricket")
Football=TakeInput("Football")
Badminton=TakeInput("Badminton")
#print the name of the players
print("Cricket players are:",Cricket)
print("Football players are:",Football)
print("Badminton players are:",Badminton)

#1.Players playing both cricket and badminton
CAB = []
for player in Cricket:
 if player in Badminton:
     CAB.append(player)
print("Players playing both cricket and badminton",CAB)

#2.Players playing Cricket or Badminton but not both 
COBNB= []
for player in Cricket:
 if player not in Badminton:
     COBNB.append(player)
for player in Badminton:
 if player not in Cricket:
     COBNB.append(player)
print("Players playing Cricket or Badminton but not both",COBNB)

#3.Players playing neither Cricket nor badminton
NCNB = []
for player in Football:
 if player not in Cricket:
     if player not in Badminton:
        NCNB.append(player)
print("Players playing neither Cricket nor badminton",NCNB)

#4.Players playing Cricket and Football but not Badminton
CAFNB=[]
for player in Cricket:
 if player in Football:
    if player not in Badminton:
        CAFNB.append(player)
print("Players playing Cricket and Football but not Badminton",CAFNB)
