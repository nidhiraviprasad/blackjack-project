'''
Created on February 6, 2019
  
@authors: Meghana Muddireddy & Nidhi Raviprasad
 
Description: Final Project Submission with all extra features.
 
Extra Features: multiple decks, autoplayer mode, betting in manual mode
 
Any comment marked with a ">>" is a comment written for information/explanation.
The rest are print statements used for testing.
 
'''
from card import Card
from cards import Cards
from player import Player
  
#>>make a BlackjackCard Class inherit from Card
class BlackjackCard(Card):
      
    def getValue(self):
        if self.rank == 'A':
            return(11)
        elif self.rank == 'J':
            return(10)
        elif self.rank == 'Q':
            return(10)
        elif self.rank == 'K':
            return(10)
        elif self.rank == '10':
            return(10)
        elif self.rank in '23456789':
            return(int(self.rank))
        else:
            raise ValueError('{} is of unknown value'.format(self.rank))
  
#>>make a BlackjackHand Class
class BlackjackHand(Cards): 
      
    #>>to get total cards make
    def getTotalWithAce(self): 
        numberOfAces = 0
        total = 0
        #>>adds values of everything except aces
        for i in self.cards:
            if i.rank == 'A':
                numberOfAces+=1
            else:
                total += i.getValue()
                  
        #>>adds values of aces (either 1 or 11)
        if numberOfAces == 1:
            if total < 11:
                total+=11
            else:
                total +=1
                 
        elif numberOfAces > 1:
            if ((numberOfAces-1) + 11) + total <= 21:
                total+=(numberOfAces-1)+11
            else:
                total+=numberOfAces
                  
        return total
      
    #>>uses getTotalWithAce() class to check if total will bust
    def bust(self):
        if self.getTotalWithAce() > 21:
            return True
        else:
            return False
              
#>>make a BlackjackPlayer Class
  
class BlackjackPlayer(Player):
     
    def __init__ (self, name, amount):
        self.name = name
        self.amount = amount
        self.hand = BlackjackHand()
         
    def tossHand(self):
        self.hand = BlackjackHand()
      
    #>>asks player (with user input) whether to hit or not
    def askHit(self):
        ans = input("{}, would you like to hit? ".format(self.name))
        while (ans != 'y' and ans != 'n'):
             ans = input("Please answer with either a 'y' for yes or an 'n' for no: ")
               
        if ans == 'y':
            return True
        elif ans == 'n':
            return False
 
            
#>>make a BlackjackDealer Class 
class BlackjackDealer (BlackjackPlayer):
    #>>overwrites askHit() from BlackjackPlayer class to hit until total > 16
    def askHit(self):
        if self.hand.getTotalWithAce() < 17:
            return True
        else:
            return False
      
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
      
#>>make a BlackjackGame function
def BlackjackGame():
          
    #>>make the 2 players
    name = input("Welcome to Blackjack! What is your name? ")
    player = BlackjackPlayer(name, 1)
    dealer = BlackjackDealer("Dealer", 1)
    player.money = 1000
     
    #>>get number of rounds
    roundsin = input("How many rounds would you like to play, {}? ".format(player.name))
    #while (ans != 'y' and ans != 'n'):
             #ans = input("Please answer with either a 'y' for yes or an 'n' for no: ")          
    print()
    rounds = int(roundsin)
     
    #>>checking if player wants to use autoplayer. 
    autoplaying = False
    betting = False
    print ("There are two different modes you can use to play this game: Autoplayer or Manual with betting.")
    print ("Keep in mind that autoplayer mode does not involve money.")
    autoplayermode = input("Do you want the computer to automatically play for you? (Autoplayer mode) ")
    while (autoplayermode != 'y' and autoplayermode != 'n'):
            autoplayermode = input("Please answer with either a 'y' for yes or an 'n' for no: ")
            print()
    if autoplayermode == 'y':
        autoplaying = True
    elif autoplayermode == 'n':
        autoplaying = False
        betting = True
    #>>game executes itself for specified number if rounds     
    print()
    if autoplaying:
        player = BlackjackDealer(name, 1)
         
    else:
        print ("You have $1000 to begin with.")  
        print()       
     
    #>>make a deck of card
    deck = Cards()  # make empty deck
    #>>number of cards -> to know when to shuffle
    cardCount = 0
     
    #>>single deck
    if rounds <= 6:
        for s in Card.SUIT:
            for r in Card.RANK:
                x = BlackjackCard(r,s)
                deck.add(x)
        cardCount = 52
    #>>6 deck shoe
    else:
        for i in range (6):
            for s in Card.SUIT:
                for r in Card.RANK:
                    x = BlackjackCard(r,s)
                    deck.add(x)
        cardCount = 312
    deck.shuffle()
     
    #print (deck)
     
    #>>special deck for testing
    #deck = Cards()
    #cardCount = 12345
    #deck.add(BlackjackCard('2', 'd'))
    #deck.add(BlackjackCard('3', 'd'))
    #deck.add(BlackjackCard('2', 's'))
    #deck.add(BlackjackCard('3', 's'))
    #deck.add(BlackjackCard('5', 's'))
    #deck.add(BlackjackCard('5', 's'))
    #deck.add(BlackjackCard('A', 's'))
     
    #>>number of rounds won by each player
    playerWin = 0
    dealerWin = 0
     
    #>>whether the player has money
    hasMoney = False
     
    #>>starts the game
    for i in range(rounds):
        print("***************!ROUND {} of {}!***************".format(i+1, rounds))
         
        #>>shuffling cards if necessary
        if cardCount < 15:
            print("Please wait one moment while the deck is being shuffled...")
            while (cardCount > 0):
                cardCount-=1
                deck.deal()
            for s in Card.SUIT:
                for r in Card.RANK:
                    x = BlackjackCard(r,s)
                    deck.add(x)
            deck.shuffle()
            cardCount = 52
             
        #>>asking betting money
        valid = False
        if betting:
            print ("You have ${} now.".format(player.money))
            if int(player.money > 0): 
                betting_money = int(input ("How much money would you like to bet? "))
                if betting_money <= player.money and betting_money > 0:
                         valid = True
                while (valid == False):
                     betting_money = int(input('''Please answer with a betting amount less than or equal to ${}. 
Remember betting value has to be greater than $0. '''.format(player.money)))
                     if betting_money <= player.money and betting_money > 0:
                         valid = True
                   
         
        #>>adding first 2 cards to hand
        player.addCard(deck.deal())
        dealer.addCard(deck.deal())
        player.addCard(deck.deal())
        dealer.addCard(deck.deal())
         
        cardCount-=4
        #print(player)
        #print(dealer)
         
        #>>initial print statements with hand, score
        print("{}'s Current Score: {}".format(player.name, playerWin))
        print("Dealer's Current Score: {}".format(dealerWin))
         
        print(player)
        #print(player.hand.getTotalWithAce())
         
        visibleDealerCard = str(dealer.hand)
        print("Dealer: [{} ??]".format(visibleDealerCard[1:3]))
        #print(dealer)
         
                 
        #>>game (checks for blackjack, then does hitting routine)
        if (player.hand.getTotalWithAce() == 21 and dealer.hand.getTotalWithAce() == 21):
            print("Push 21 vs. 21")
             
        elif (player.hand.getTotalWithAce() == 21):
            print("Blackjack! {} wins!".format(player.name))
            playerWin+=1
            if betting:
                player.money+= betting_money
             
        elif (dealer.hand.getTotalWithAce() == 21):
            print("Blackjack! Dealer wins!")
            dealerWin+=1
            if betting:
                player.money-= betting_money
             
        else:
            #>>to see how far into the game we go
            continueToDealer = True
            continueToScore = True
             
            #>>player hitting and busting
            hit = True
            while (hit):
                if (player.askHit() == False):
                    hit = False
                else:
                    cardCount-=1
                    player.addCard(deck.deal())
                    print(player, "=> {}".format(player.hand.getTotalWithAce()))
                    if (player.hand.bust()):
                        print("Dealer wins! {} busts with {}.".format(player.name, player.hand.getTotalWithAce()))
                        dealerWin+=1
                        if betting:
                            player.money-= betting_money
                        hit = False
                        continueToDealer = False
                        continueToScore = False
                         
            #>>dealer hitting and busting
            if (continueToDealer):
                hit = True
                while (hit):
                    if (dealer.askHit() == False):
                        hit = False
                    else:
                        cardCount-=1
                        dealer.addCard(deck.deal())
                        print(dealer, "=> {}".format(dealer.hand.getTotalWithAce()))
                        if (dealer.hand.bust()):
                            print("{} wins! Dealer busts with {}.".format(player.name, dealer.hand.getTotalWithAce()))
                            playerWin+=1
                            if betting:
                                player.money+= betting_money
                            hit = False
                            continueToScore = False    
                                    
                #>>compare final scores and see who wins!
                playerTotal = player.hand.getTotalWithAce()
                dealerTotal = dealer.hand.getTotalWithAce()
                if (continueToScore):
                    print (player)
                    print (dealer)
                    if playerTotal > dealerTotal:
                        print("{} wins with a total of {} vs {}!".format(player.name, playerTotal, dealerTotal))
                        playerWin+=1
                        if betting:
                            player.money+= betting_money
                    elif playerTotal < dealerTotal:
                        print("Dealer wins with a total of {} vs {}!".format(dealerTotal, playerTotal))
                        dealerWin+=1
                        if betting:
                            player.money-= betting_money
                    else:
                        print("Push! {} vs {}.".format(playerTotal, dealerTotal))
                    
         
        #>>ending: where hands are cleared & all variables are set to be ready for next round
        player.tossHand()
        dealer.tossHand()
        print()
         
        #>>checks if player still has money left
        if betting:
            if player.money <= 0:
                hasMoney = False
                break
     
    #>>for manual mode    
    #>>checking betting/money value of player
    if betting:
        #>>if the player still has money
        if player.money > 0:
            if player.money > 1000:
                print("Congratulations! You have earned money! You now have a total of ${}!!!".format(player.money))
            else:
                print("Congratulations! You have not lost all of your money! You now have a total of ${}!!".format(player.money))
                    
            #>>printing final scores after all rounds are over!
            winGame = ""
            if (playerWin > dealerWin):
                caps = player.name.upper()
                winGame = "FINAL SCORE: Dealer {} vs {} {}. {} WINS!!!".format(dealerWin, player.name, playerWin, caps)
                print()
             
            elif (playerWin < dealerWin):
                winGame = "FINAL SCORE: Dealer {} vs {} {}. DEALER WINS!!".format(dealerWin, player.name, playerWin)
                print()
            else:
                winGame = "FINAL SCORE: Dealer {} vs {} {}. TIE!".format(dealerWin, player.name, playerWin)
                print()
             
            print(">>> {} <<<".format(winGame))
             
        #>>if the player lost all of their money    
        else:
            print(">>> GAME OVER! You have lost all of your money! <<<")
             
    else:
        #>>for autoplayer mode
        #>>printing final scores after all rounds are over!
            winGame = ""
            if (playerWin > dealerWin):
                caps = player.name.upper()
                winGame = "FINAL SCORE: Dealer {} vs {} {}. {} WINS!!!".format(dealerWin, player.name, playerWin, caps)
                print()
             
            elif (playerWin < dealerWin):
                winGame = "FINAL SCORE: Dealer {} vs {} {}. DEALER WINS!!".format(dealerWin, player.name, playerWin)
                print()
            else:
                winGame = "FINAL SCORE: Dealer {} vs {} {}. TIE!".format(dealerWin, player.name, playerWin)
                print()
             
            print(">>>{}<<<".format(winGame))
     
     
     
     
     
         
         
     
def main():
    BlackjackGame()
      
if __name__ == "__main__":
    main()
     
