import random

word = ["UMBRELLA","GADGETS","ELECTRONIC","SMARTPHONE"]
word = random.choice(word)

total_chances = 7
guesssed_word = "-"*len(word)

while total_chances !=0:
   print(guesssed_word)
   letter = input("Guess a letter: ").upper()
   if letter in word:
        for index in range(len(word)):
           if word[index]==letter:
               guesssed_word = guesssed_word [:index]+letter+guesssed_word[index+1:]            
        if guesssed_word == word:
           print ("congratulations you won!!!")  
           break
   else:
        total_chances -= 1
        print("Incorrect guess")
        print("the remaining chances are: ",total_chances)
else:
  print("Game Over")
  print("You Lose")
  print("All the chances are exhausted")
  print("the correct word is",word)
