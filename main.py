letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# ----- Tasks -----------
# 1 create new dictionary
letter_to_points = {key:value for key,value in zip(letters,points)}

# 2 add empty key with value 0
letter_to_points[""]=0

# 3, 4, 5,6 create function score_word and loop over all values, assign 0 if the key does not exists and return point_total
def score_word(word,listin):
  point_total = 0
  for letters in word:
     if letters.islower():
       lettersin = letters.upper()
       point_total += listin.get(lettersin,0)
       print(f"{letters} : {listin.get(lettersin,0)} points")
     else:
      point_total += listin.get(letters,0)
      print(f"{letters} : {listin.get(letters,0)} points")
  return point_total

# 7, 8 test the function: Result  = 15
print(score_word("BROWNIe",letter_to_points))


# ---- Score the Game
# 9 create dictionary player_to_words
player_to_words = {
  "player1":["BLUE","TENNIS","EXIT"],
  "wordNerd":["EARTH","EYES","MACHINE"],
  "LexiCon":["ERASER","BELLY","HUSKY"],
  "ProfReader":["ZAP","COMA","PERIOD"]
}
test={"player1":["e","a"],
     "ProfReader":["A","C"]
     }
# 10 create an empty dictionary
player_to_points = {}

# 11,12,13,14 iterate through the items player_to_words for each word and get total scores for each player
# --- get total score for one player ---
def onePlayerWordList(wordlist):
  temp_score = 0  
  for char in wordlist:
    temp_score += score_word(char,letter_to_points)
  return temp_score

# --- get total score for all players ---
def iterate_players(listin):
  player_to_points = {}
  onePlayer = 0
  for player,wordlist in listin.items():
    print("\n")
    print(f"Score for player {player}")
    onePlayer = onePlayerWordList(wordlist)
    print("--------------------------")
    print(f"Total score : {onePlayer}")
    player_to_points[player]=onePlayer
  return player_to_points
      
# 15 get scores of all players
player_to_points=iterate_players(player_to_words)
print("\n --- Display all player ---")
print(player_to_points)
