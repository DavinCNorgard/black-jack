import random
import time


def deal():
    rand = random.randint(1, 13)
    if (rand > 10):
        return 10
    else:
        return rand

def play():

    player = []
    dealer = []

    dealersTurn = True

    # setup game
    player.append(deal())
    player.append(deal())
    dealer.append(deal())
    dealer.append(deal())

    # eleven rule
    if(player.__contains__(1)):
        player[player.index(1)] = 11
    
    if(dealer.__contains__(1)):
        dealer[dealer.index(1)] = 11

    # players turn
    while True:
        print('\n\n')
        print('-------------' + ' dealer: ' + str(dealer[0]))
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('-------------' + ' player: ' + str(player) + ' sum: ' + str(sum(player)))
        print('\n\n')

        playerInput = input("hit or pass?: ")

        if playerInput == 'hit':
            player.append(deal())
            # check eleven rule
            if(player.__contains__(11)):
                player[player.index(11)] = 1


        if playerInput == 'pass':
            break

        if sum(player) > 21:
            print("you busted: ", player, sum(player))
            print("Dealer wins")
            dealersTurn = False
            break

    # dealers turn
    while dealersTurn:


        print('\n\n')
        print('-------------' + ' dealer: ' + str(dealer) + ' sum: ' + str(sum(dealer)))
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('----------------------------------------------')
        print('-------------' + ' player: ' + str(player) + ' sum: ' + str(sum(player)))
        print('\n\n')
            
        if (sum(dealer) > 21):
            print("dealer busted: ", sum(dealer))
            print("you win!")
            break

        if (sum(dealer) <= 15):
            dealer.append(deal())

            if(dealer.__contains__(11)):
                dealer[dealer.index(11)] = 1      

        else:

            if (sum(dealer) > sum(player)):
                print(sum(dealer), sum(player))
                print("Dealer wins")
                break

            if (sum(dealer) < sum(player)):
                print(sum(dealer), sum(player))
                print("You win!")
                break

            if (sum(dealer) == sum(player)):
                print(sum(dealer), sum(player))
                print("draw")
                break


        time.sleep(2)


play()

