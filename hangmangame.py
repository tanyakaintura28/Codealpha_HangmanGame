from wonderwords import RandomWord

def difficulty_level(difficulty):
  RandomWord() #needed so that each time while occurs there is a new word in it
  while True:
    random_word = RandomWord().word()
    if(difficulty==1 and 3 <= len(random_word) <= 7):
        return random_word
    if(difficulty==2 and 8 <= len(random_word) <= 13):
        return random_word
    if(difficulty==3 and 14 <= len(random_word)):
        return random_word

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

difficulty = int(input("Choose the level of difficulty -\n1. Easy\n2. Medium\n3. Hard\n"))
random_word = difficulty_level(difficulty)

blanks = []
for each_letter in random_word:
    blanks.append("_")
print("".join(blanks))

no_of_life = 6
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
                                                                                                                                    
while (no_of_life >0 and "".join(blanks) != random_word):
    letter = input("Guess a letter :\n")
    found = False #have boolean inside the loop
    if letter in random_word:
        for i, each_letter in enumerate(random_word): #enumerate can be used to have index and string together in for loop for a string
            if(each_letter == letter and blanks[i]=="_"):
                blanks[i] = letter
                print(f"\nLives = {no_of_life}")
                print(f"{"".join(blanks)}\n")
                found = True 
                break
        if (found == False): # use this to make sure that only one life increases in the whole loop completion
            no_of_life -= 1
            print(f"\nLives = {no_of_life}")
            print(stages[no_of_life])
            
    else :
        no_of_life -= 1
        print(f"\nLives = {no_of_life}")
        print(stages[no_of_life])
        
if no_of_life == 0 :
    print(f"\nLives = {no_of_life}")
    print(stages[no_of_life])
    print("You ran out of lives! The word was:", random_word)
    
else:
    print(random_word,"\nCongratulations! You guessed the word")
