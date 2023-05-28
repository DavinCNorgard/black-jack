# black-jack
Very simplistic approach to a CLI blackjack minigame, built in couple of hours.

## Description
My cousin Nathan was interested in python basics and learning some programming. This mini game was my attempt to show him some of the basics in a fun and interactive way.
He has extensive knowledge of the casino games, and was able to clearly explain the official blackjack casino rules to me so I could convert them into logical statements. 
We had a lot of fun building this project together! (hopefully i didnt bore him too much)

## Blackjack rules
- A link to the rules for review: https://bicyclecards.com/how-to-play/blackjack/

## How to play
1. To start, simply run the python script `blackjack.py`
2. It is the players turn first, and the dealers turn second. 
3. It will show you the table, it will look something like this:
<!-- 
  ------------- dealer: [9]
----------------------------------------------
----------------------------------------------
----------------------------------------------
----------------------------------------------
----------------------------------------------
------------- player: [9, 5] sum: 14 -->

3. The list contains the cards in the players and dealers hands respectively.
4. The sum is the addition of all the cards in the list.
5. You will also get prompted with this message:

hit or pass?:

6. Either type `hit` or `pass` depending on your choice.
7. You will be prompted by this message until you bust or decide to pass.
8. Now it is the dealers turn!

## Dealer protocol
- The dealer MUST hit until their sum is above 15
- The dealer will continue to hit until he has achieved a greater hand than the players OR has busted (over 21)
