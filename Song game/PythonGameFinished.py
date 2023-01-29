import random
#Checking user file for the stored usernames and passwords
with open("users.txt", "r") as user_file:
    users = {}
    for line in user_file:
        user, password = line.strip().split(":")
        users[user] = password

# Prompt the user to enter their username and password
while True:
    # Prompt the user to enter their username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username and password match the ones in the dictionary
    if username in users and users[username] == password:
        print("Welcome!" + ' '+username +'!')
        break
    else:
        print("Access denied. Please check your username and password.")


#To start the game
play = input("Please press enter to start the game. Q to go back ")
if play == 'q':
      print("Please press enter to start the game ")
else:
        print("Welcome to the song game. Choose the correct song")
        print("The category of songs are : The 100 most-streamed songs")    


#List storage for songs
with open("test.txt", "w") as f:
    f.write("Shape Of You\nEd Sheeran\nSunflower\nPost Malone featuring 21 Savage\n One Dance\nDrake\nSome You Loved\nLewis Capaldi\nCloser\nThe Chainsmokers featuring Halsey\nBeliever\nImagine Dragons\nStay\nThe Kid Laroi & Justin Bieber\nSenorita\nShawn Mendes & Camila Cabello\nPerfect\nEd Sheeran\nBad Guy\nBillie Eilish\nLucid Dreams\nJuice WRLD\nHeat Waves\nGlass Animals\nSay You Wont Let Go\nJames Arthur\nAll of Me\nJohn Legend")

with open("test.txt") as f:
    file = [i.strip() for i in f.readlines()]

print(len(file))

# Chooses a random song from test.txt
if len(file) > 0:
    x = random.randint(0, len(file)-1)
    if x % 2:
       x -= 1
   

# Outputting the artist and the first letter of each word in the song title
    artist = file[x+1]
    song = file[x]
    song_letters = ' '.join([word[0] for word in song.split()])
    print("Artist:", artist)
    print("Song:",song_letters)

#Score and Incorrect guesses variables
score = 0
incorrect_guesses = 0

#Incorrect guessing system. If it's song is guessed wrong twice it ends the game.
while True:
       answer = input("Guess the song name: ")
       if answer != file[x]:
              incorrect_guesses += 1
              print("You've got the song wrong!")
              if incorrect_guesses == 1:
                     print("Last chance!")
              if incorrect_guesses == 2:
                     print('Game over!')
                     break
# Function after you get the song correct
# Prints your score
       else:
              if incorrect_guesses == 0:
                score += 3
                print("-----------------------------------------")
                print("Well done, You have" ,(score), "points")
                print("-----------------------------------------")
              else:
                if incorrect_guesses == 1:
                  score += 2
                  print("------------------------------------------------------------")
                  print("You just got the answer. Well done! You have ", (score), "points")
                  print("----------------------------------------------------------------")
                  incorrect_guesses = 0
#Removes the song when it's correctly guessed
              file.remove(file[x])
              file.remove(file[x])
#Opens file again and choose another song
              if len(file) == 0:
               print(f"there are {len(file)} songs left...")
               print("You have completed the game!")
               exit()
              with open("songs.txt", "w") as f:
                  f.write("\n".join(file))
              x = random.randint(0, len(file)-1)
              if x % 2:
                  x -= 1
#Displaying the artist and the song with 1 letter
# Artist : ______
# Song : -_______
              artist = file[x+1]
              song = file[x]
              song_letters = ' '.join([word[0] for word in song.split()])
              print("Artist:", artist)
              print("Song:",song_letters)

if len(file) == 0:
  print(f"there are {len(file)} songs left...")
  print("You have completed the game!")
  exit()
