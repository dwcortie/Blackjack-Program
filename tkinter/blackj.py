from tkinter import *
from random import randint
import time

root = Tk()
root.attributes("-fullscreen", True)
bgImg = PhotoImage(file="assets/background.png")
background = Label(
    image=bgImg
)
root.geometry("1920x1080")
background.place(x=0, y=0)
root.title("Blackjack")
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=1)
for i in range(5):
    root.columnconfigure(index=i, weight=1)
suits = ["spa", "dia", "hea", "clu"]
cardsInASuit = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cards = []
playerCards = []
dealerCards = []
cardImages = []
score = 0
dealerScore = 0
cardLabels = []
dealerCardLabels = []
hitButton = Button()
standButton = Button()
playAgain = Button()


label = Label(
    text="Your Score:\nDealer Score:",
    bg="gray",
    padx=10,
    pady=10,
    relief=RAISED,
    font=("Arial", 40, "bold")
)


exitButton = Button(
    text="Exit",
    command=root.quit,
    padx=5,
    pady=5
)


def startGame():
    global playAgain
    try:
        playAgain.destroy()
    finally:
        print("playAgain not destroyed")
    global standButton
    global hitButton
    standButton = Button(
        text="Stand",
        padx=5,
        pady=5,
        command=playerStand
    )
    hitButton = Button(
        text="Hit me!",
        command=playerHit,
        padx=5,
        pady=5
    )
    global score
    global suits
    global playerCards
    global dealerCards
    global cardImages
    global dealerScore
    global cardLabels
    global dealerCardLabels
    global cardsInASuit
    global cards
    label.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    hitButton.grid(row=3, column=0, sticky=NSEW)
    standButton.grid(row=3, column=4, sticky=NSEW)
    exitButton.grid(row=3, column=2, sticky=NSEW)
    suits = ["spa", "dia", "hea", "clu"]
    cardsInASuit = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    cards = []
    playerCards = []
    dealerCards = []
    cardImages = []
    score = 0
    dealerScore = 0
    cardLabels = []
    dealerCardLabels = []
    for i2 in suits:
        for i3 in cardsInASuit:
            cards.append(f"{i2}_{i3}")
    score += 1
    dealerHit()
    score -= 1
    dealerHit()
    for startHit in range(2):
        playerHit()


def dealerHit():
    global cards
    global dealerCardLabels
    global score
    global dealerScore
    isoCard = []
    aces = 0
    secretDealerScore = 0
    randCard = randint(0, len(cards) - 1)
    dealerCards.append(cards[randCard])
    cards.remove(cards[randCard])
    if score == 0:
        img = PhotoImage(file="playing-cards/back.png")
        card = Label(root, image=img, bg='#e0e0e0')
        card.photo = img
        card.grid(row=1, column=len(dealerCards) - 1)
        dealerCardLabels.append(card)
        for i5 in dealerCards:
            try:
                isoCard.append(int(i5[4:len(i5)]))
            except ValueError:
                isoCard.append(str(i5[4:len(i5)]))
        for i3 in isoCard:
            if isinstance(i3, str) is True:
                if i3 != "A":
                    secretDealerScore += 10
                else:
                    aces += 1
            else:
                secretDealerScore += i3
        for i4 in range(aces):
            if secretDealerScore + 11 > 21:
                secretDealerScore += 1
            else:
                secretDealerScore += 11
        if secretDealerScore == 21:
            playerStand()
    else:
        dealerScore = 0
        img = PhotoImage(file=f"playing-cards/{dealerCards[len(dealerCards) - 1]}.png")
        card = Label(root, image=img, bg='#e0e0e0')
        card.photo = img
        card.grid(row=1, column=len(dealerCards) - 1)
        dealerCardLabels.append(card)
        for i5 in dealerCards:
            try:
                isoCard.append(int(i5[4:len(i5)]))
            except ValueError:
                isoCard.append(str(i5[4:len(i5)]))
        for i3 in isoCard:
            if isinstance(i3, str) is True:
                if i3 != "A":
                    dealerScore += 10
                else:
                    aces += 1
            else:
                dealerScore += i3
        for i4 in range(aces):
            if dealerScore + 11 > 21:
                dealerScore += 1
            else:
                dealerScore += 11
    label.config(text=f"Your Score: {score}\nDealer Score: {dealerScore}")


def playerHit():
    global cardLabels
    global score
    global dealerScore
    randCard = randint(0, len(cards)-1)
    playerCards.append(cards[randCard])
    cards.remove(cards[randCard])
    img = PhotoImage(file=f"playing-cards/{playerCards[len(playerCards)-1]}.png")
    card = Label(root, image=img, bg='#e0e0e0')
    card.photo = img
    card.grid(row=2, column=len(playerCards)-1)
    cardLabels.append(card)
    if len(playerCards) > 5:
        standButton.grid_configure(row=3, column=len(playerCards)-1)
        label.grid_configure(row=0, columnspan=len(playerCards))
    score = 0
    aces = 0
    isoCard = []
    for i5 in playerCards:
        try:
            isoCard.append(int(i5[4:len(i5)]))
        except ValueError:
            isoCard.append(str(i5[4:len(i5)]))
    for i3 in isoCard:
        if isinstance(i3, str) is True:
            if i3 != "A":
                score += 10
            else:
                aces += 1
        else:
            score += i3
    for i4 in range(aces):
        if score+11 > 21:
            score += 1
        else:
            score += 11
    label.config(text=f"Your Score: {score}\nDealer Score: {dealerScore}")
    root.update()
    if score > 21:
        root.update()
        time.sleep(3)
        deleteCards("L")


def playerStand():
    hitButton.destroy()
    standButton.destroy()
    global score
    global dealerScore
    global dealerCardLabels
    img = PhotoImage(file=f"playing-cards/{dealerCards[1]}.png")
    card = Label(root, image=img, bg='#e0e0e0')
    card.photo = img
    card.grid(row=1, column=1)
    dealerCardLabels.append(card)
    while dealerScore < 17:
        dealerHit()
        root.update()
        time.sleep(0.5)
        root.update()
    time.sleep(3)
    root.update()
    if dealerScore > score:
        if dealerScore < 21:
            deleteCards("L")
        else:
            deleteCards("W")
    elif dealerScore < score:
        deleteCards("W")
    else:
        deleteCards("D")


def deleteCards(result):
    global playAgain
    hitButton.destroy()
    standButton.destroy()
    global score
    global dealerScore
    for widget in cardLabels:
        widget.destroy()
    for widget2 in dealerCardLabels:
        widget2.destroy()
    score = 0
    dealerScore = 0
    if result == "L":
        label.config(text="You Lose!\nPlay Again?")
    elif result == "W":
        label.config(text="You Win!\nPlay Again?")
    elif result == "D":
        label.config(text="It's a Draw!\nPlay Again?")
    playAgain = Button(
        root,
        text="Play Again",
        command=startGame,
        padx=5,
        pady=5,
    )
    playAgain.grid(row=2, column=2, sticky=NSEW)


startGame()

root.mainloop()
exit()
