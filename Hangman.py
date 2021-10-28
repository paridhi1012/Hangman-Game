import random
def hangman():
    fi=open("programming\dictionary.txt",'r')
    alltext = fi.read()
    words=list(map(str,alltext.split()))
    word=random.choice(words)
    validletters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main=main + letter
            else:
                main = main + "_" + " "
        
        if main == word:
            print(main)
            print("you win!")
            break
        print("Guess the word",main)
        guess = input().lower()
        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess=input().lower()

        if guess not in word:
            turns=turns-1
            if turns == 9:
                print("9 turns left")
                print(" ---------- ")
            if turns == 8:
                print("8 turns left")
                print(" ---------- ")
                print("   o   ")
            if turns == 7:
                print("7 turns left")
                print(" ---------- ")
                print("   o   ")
                print("   |   ")  
            if turns == 6:
                print("6 turns left")
                print(" ---------- ")
                print("   o   ")
                print("   |   ")
                print("   /   ")
            if turns == 5:
                print("5 turns left")
                print(" ---------- ")
                print("   o   ")
                print("   |   ")
                print("  / \  ")
            if turns == 4:
                print("4 turns left")
                print(" ---------- ")
                print(" \ o   ")
                print("   |   ")
                print("  / \  ")
            if turns == 3:
                print("3 turns left")
                print(" ---------- ")
                print(" \ o /  ")
                print("   |    ")
                print("  / \   ")
            if turns == 2:
                print("2 turns left")
                print(" ---------- ")
                print(" \ o /| ")
                print("   |    ")
                print("  / \   ")
            if turns == 1:
                print("1 turns left")
                print(" ---------- ")
                print(" |\ o /| ")
                print("    |    ")
                print("   / \   ")
            if turns == 0:
                print("You loose")
                print("you let a kind man die")
                print("    o_| ")
                print("   /|\    ")
                print("   / \   ")
                print("the word is :" + word)
                break
        
name=input("Enter your Name : ")
print("Welcome" , name)
print("-----------------")
print("try to guess the word in less than 10 trials")
hangman()
print()