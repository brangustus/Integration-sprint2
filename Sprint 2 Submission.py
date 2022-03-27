#importing zone
import time
import math
import random



#Calculator for all functions using any 2 given numbers (sprint 1)
def miniCalculator():
    randomNum1=float(input("Any integer: "))
    randomNum2=float(input("Any integer: "))
#booleen
    print(randomNum1==randomNum2)
    print(randomNum2!=randomNum2)
    print(not(randomNum2!=randomNum2))
    if randomNum1<4 and randomNum1>2:
        print("I like this number")
    if randomNum2<0 or randomNum2<100:
        print("cool number")
#calculator
    print("Exponential: ", format(randomNum1**randomNum2,".2f"))
    print("Multiplication: ", format(randomNum1*randomNum2,".2f"))
    print("Division: ", format(randomNum1/randomNum2,".2f"))
    print("Modulus", format(randomNum1%randomNum2,".2f"))
    print("Division(no remainder): ", format(randomNum1//randomNum2,".2f"))
    print("Addition: ", format(randomNum1+randomNum2,".2f"))
    print("Subtraction: ", format(randomNum1-randomNum2,".2f"))
miniCalculator()

time.sleep(2)

def strConcatinator():
    randomStr1=input("\nenter anything here: ")
    randomStr2=input("enter anything here: ")
#prints the first input 10 times
    print(randomStr1*10)
#prints the first input next to the second input (concatinates the strings)
    print (randomStr1+randomStr2)
strConcatinator()

time.sleep(5)

#catergories: Action,Comedy,Horror,Sports,Drama
def animeGenerator():
    categoryLoopCounter=0
    while categoryLoopCounter==0:
        categoryList=["action","comedy","horror","sports","dramas"]
        print("\nAction: 0\nComedy: 1\nHorror: 2\nSports: 3\nDramas: 4")
        favCategory = int(input ("\nEnter the number of your favorite category here: "))
        if favCategory<=4:
#picking a category
            categoryList[favCategory]
            try:
                if categoryList[favCategory]=="action":
                    print ("\nYour favorite Category is Action.")
                    categoryLoopCounter+=1
                elif categoryList[favCategory]=="comedy":
                    print ("\nYour favorite Category is Comedy.")
                    categoryLoopCounter+=1
                elif categoryList[favCategory]=="horror":
                    print ("\nYour favorite Category is Horror.")
                    categoryLoopCounter+=1
                elif categoryList[favCategory]=="sports":
                    print ("\nYour favorite Category is Sports.")
                    categoryLoopCounter+=1
                elif categoryList[favCategory]=="dramas":
                    print ("\nYour favorite Category is Dramas.")
                    categoryLoopCounter+=1
                else:
                    print ("Thats not a valid category.")
            except:
                print ("Thats not a valid category.")
        else:
            print ("Thats not a valid category.")
        
        time.sleep(2)
        
    animeLoopCounter=0
    while animeLoopCounter==0:
#picking an anime
        if favCategory==0:
            print ("1: Fighting Giants\n2: Sword Fighting\n3: Mechas and Drills\n4: Psychic Battles"
                   "\n5: Realistic super powers with severe drawbacks")
            actionAnime = int(input ("Enter only one (1,2,3,4,5): "))
            if actionAnime==1:
                print ("I recommend: Attack on titan")
                animeLoopCounter+=1
            elif actionAnime==2:
                print ("I recommend: Bleach")
                animeLoopCounter+=1
            elif actionAnime==3:
                print ("I recommend: Guran Lagan")
                animeLoopCounter+=1
            elif actionAnime==4:
                print ("I recommend: Mob Psycho 100")
                animeLoopCounter+=1
            elif actionAnime==5:
                print ("I recommend: Darker than black")
                animeLoopCounter+=1
            else:
                print ("that is not a valid input")

        if favCategory==1:
            print ("1: Funny english dub about ghosts\n2: Comedy about schoolgirls\n3: Funny anime about a samurai"
                   "\n4: Hilarious adventurers guild featuring a traveler, a goddess, and a masochist"
                   "\n5: Comedy about college frats and the a diving club (HIGHLY RECCOMEND)")
            comedyAnime = int(input ("Enter only one (1,2,3,4,5): "))
            if comedyAnime==1:
                print ("I recommend: Ghost Stories (english dub)")
                animeLoopCounter+=1
            elif comedyAnime==2:
                print ("I recommend: Azumanga Daioh")
                animeLoopCounter+=1
            elif comedyAnime==3:
                print ("I recommend: Gintama")
                animeLoopCounter+=1
            elif comedyAnime==4:
                print ("I recommend: Konosuba")
                animeLoopCounter+=1
            elif comedyAnime==5:
                print ("I recommend: Grand Blue")
                animeLoopCounter+=1
            else:
                print ("that is not a valid input")
            
        if favCategory==2:
            print ("1: Very gory story about a cursed highschool\n2: Very gruesome anime about demons and feasting on humans"
                   "\n3: Anime about demons taking over a high school murdering highschoolers"
                   "\n4: An immortal vampire fighting Nazis, zombies, and priests in no particular order"
                   "\n5: Highschool whose arm was taken over by an alien parasyte inhabiting who has made the"
                   "decision to kill the other alien intruders (HIGHLY RECCOMEND)")
            horrorAnime = int(input ("Enter only one (1,2,3,4,5): "))
            if horrorAnime==1:
                print ("I recommend: Another")
                animeLoopCounter+=1
            elif horrorAnime==2:
                print ("I recommend: Blood-C")
                animeLoopCounter+=1
            elif horrorAnime==3:
                print ("I recommend: Corpse Party")
                animeLoopCounter+=1
            elif horrorAnime==4:
                print ("I recommend: Hellsing")
                animeLoopCounter+=1
            elif horrorAnime==5:
                print ("I recommend: Parasyte the Maxim")
                animeLoopCounter+=1
            else:
                print ("that is not a valid input")

        if favCategory==3:
            print ("1: baseball\n2: Boxing\n3: Volleyball"
                   "\n4: Martial arts and muscles"
                   "\n5: Basketball (HIGHLY RECCOMEND)")
            sportsAnime = int(input ("Enter only one (1,2,3,4,5): "))
            if sportsAnime==1:
                print ("I recommend: Ace of Diamond")
                animeLoopCounter+=1
            elif sportsAnime==2:
                print ("I recommend: Hajime no Ippo")
                animeLoopCounter+=1
            elif sportsAnime==3:
                print ("I recommend: Haikyu!!")
                animeLoopCounter+=1
            elif sportsAnime==4:
                print ("I recommend: Baki")
                animeLoopCounter+=1
            elif sportsAnime==5:
                print ("I recommend: Kuroko's Basketball")
                animeLoopCounter+=1
            else:
                print ("that is not a valid input")

        if favCategory==4:
            print ("1: love story between two highschoolers\n2: Story about a split group of highschoolers reunited by"
                   " the ghost of their late friend\n3: a film about 2 close friends grdually growing apart and the time they lost"
                   "\n4: a highschool in the afterlife (limbo) where teens who expirienced trauma work to get over it before they can pass on to heaven"
                   "\n5: Story about a trauma ridden pianist and an ill violinist who with the violinist's help, works to overcome his trauma and play for her"
                   " and the blossoming love between them (HIGHLY RECCOMEND)")
            dramaAnime = int(input ("Enter only one (1,2,3,4,5): "))
            if dramaAnime==1:
                print ("I recommend: Clannad")
                animeLoopCounter+=1
            elif dramaAnime==2:
                print ("I recommend: Ano Hara")
                animeLoopCounter+=1
            elif dramaAnime==3:
                print ("I recommend: 5 centimeters per second")
                animeLoopCounter+=1
            elif dramaAnime==4:
                print ("I recommend: Angel Beats")
                animeLoopCounter+=1
            elif dramaAnime==5:
                print ("I recommend: Your lie in April")
                animeLoopCounter+=1
            else:
                print ("that is not a valid input")

            time.sleep(5)
            
#continue: yes or no?
        continueLoop=0
        for continueLoop in range (1):
            print("\nwould you like to retry with another category?","\nenter 1 for yes","\nenter 0 for no","\n1 or 0: ")
            userContinue=int(input("continue?: "))
            if userContinue==1:
                continueLoop+=1
                categoryLoopCounter=0
            elif userContinue==0:
                continueLoop+=1
                print("thank you for using my program :)")
            else:
                print("try a valid input, 1 or 0")
                
            
animeGenerator()
