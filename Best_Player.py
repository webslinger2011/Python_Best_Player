#Create a Game Performance Evaluation Program
#Calculate Highest, Lowest and Average for each player

import random
#Input the person's name
playerName=[]
numPlayer = 3 #Store player names

#Create array for sorting scores and players
scoreArray=[]
#Create an Array ("LIST") to find out who has the highest average score
averageArray=[]
addplayerName =[]

#Use numScores for number of tries <see line 22>

for j in range(0,numPlayer,1):
    print(" ")
    newPlayer = str(input("Input Player Name: "))#cast everything as a string
    playerName.append(newPlayer)
    #Create an Array for Scores
    scores=[]
    #This can be made to ask input from the user
    #Convert the value to an integer
    #numScores=int(input("How many times did the person bowl? "))
    numScores = 10 #Specify tries per game                        
    #Input scores using for loop
    for i in range(0,numScores,1): #Start from 0 and increment by one
        #newScore=float(input("Enter the score: ")) 
        for p in range(0,numPlayer,1): #Generate random scores according to number of players
            newScore = random.randint(0,100) #Store value in newScore
            scores.append(float(newScore)) #Store the value in the scores Array
    print(" ")
    print("Player scores are: ")  
    for i in range(0,numScores,1):
        print(scores[i])
                 
    totalScore = 0 #Start the value at zero
    for i in range(0,numScores,1):
        totalScore=totalScore + scores[i]
    average = totalScore/numScores
    averageArray.append(average) #add result to averageArray
    print(" ")
    print("Player: " + playerName[j]) 
    print("The Average is: ",average)
    
    

    #Now to figure Highest and Lowest score
    highScore=0 #score
    lowScore =100
    for i in range(0,numScores,1):
        if scores[i] < lowScore:
            lowScore = scores[i]
        if scores[i] > highScore:
            highScore = scores[i]
           
               
    print("The High score is: ", highScore)
    print("The Low score is: ", lowScore)
    
#scoreArray.append(scores)
#Store all player names inside addplayerName Array
addplayerName.append(playerName)
#print(scoreArray)
#Store players overall score average
print(" ")
print("Average Player scores are: ",averageArray, addplayerName)


#print(" ")
#print("Sorted Average Scores Are: ")
#for i in range(0,numPlayer,1):
    #print(averageArray[i])
    #print(" ")
    

#print(addplayerName[numPlayer-1]) #to print player name with highest average from the index
#Find the player with the highest average

#Find the player with the highest average
#Ask how to find the name linked to the highest average player
averageArray_unsorted = averageArray #test alt sorting method
print(playerName)
a = averageArray_unsorted
print("Unsorted Player Average: ", a)
sort_a = a.sort()
print("Sorted Average: ",a)
print("The highest average is: ")
print(averageArray[numPlayer-1]) #to print highest average from the index