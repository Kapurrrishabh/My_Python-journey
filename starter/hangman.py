import random
words=("apple","banana","pinaple")
hangman_art={0:("  ",
                "  ",
                "  "),
             1:(" o ",
                "   ",
                "   "),
             2:(" o ",
                " | ",
                "  "),
             3:(" o ",
                "/| ",
                "  "),
             4:(" o ",
                "/|\\ ",
                "  "),
             5:(" o ",
                "/|\\ ",
                "/  "),
             6:(" o ",
                "/|\\ ",
                "/ \\ ")}
def display_hangman(guess):
    print("******************")
    for line in hangman_art[guess]:
        print(line)
    print("******************")    
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
   print(" ".join(answer))
def main():
    print("####### WELCOME TO GAME OF HANGMAN ########")
    word=random.choice(words)
    hint=['_']*len(word)
    guess_wrong=0
    is_running=True
    guessed_set=set()
    while is_running:
        display_hangman(guess_wrong)
        word_guessed=input("Enter the guessed letter:-").lower()
        
        if len(word_guessed)!=1 or not word_guessed.isalpha():
            print("invalid input(only single character )")
            continue
        if word_guessed in guessed_set:
            print("already guessed this word")
            continue
        guessed_set.add(word_guessed)
        if word_guessed in word:
            for i in range(len(word)):
                if word[i]==word_guessed:
                    hint[i]=word_guessed
                    display_hint(hint)
        elif guess_wrong==6:
            print(f"You Have Guessed {guess_wrong} wrong letters")
            display_hangman(guess_wrong)
            print("Sorry you loose")
            is_running=False
        else:
         guess_wrong+=1
        if "_" not in hint:
            display_hangman(guess_wrong)
            display_answer(word)
            print("Congrats!  You Win")
            is_running=False  
        
    
if __name__=="__main__":
    main()