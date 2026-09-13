# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowels(self, word):
        vowels = "aeuoi"
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
        return count 
        
    def round_winner(self, player1_word: str, player2_word: str):
        if self.count_vowels(player1_word) > self.count_vowels(player2_word):
            return 1
        elif self.count_vowels(player1_word) < self.count_vowels(player2_word):
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def validate(self, word):
        if word == "rock" or word == "scissors" or word == "paper":
            return True
        return False


    def round_winner(self, player1_word: str, player2_word: str):
        if self.validate(player1_word) and self.validate(player2_word): 
            if player1_word == "rock":
                match player2_word:
                    case "paper":
                        return 2
                    case "scissors":
                        return 1
                    case "rock":
                        pass
            elif player1_word == "scissors":
                match player2_word:
                    case "paper":
                        return 1
                    case "scissors":
                        pass
                    case "rock":
                        return 2
            elif player1_word == "paper":
                match player2_word:
                    case "paper":
                        pass
                    case "scissors":
                        return 2
                    case "rock":
                        return 1
        else:
            if self.validate(player1_word) and self.validate(player2_word) == False:
                return 1
            elif self.validate(player1_word) == False and self.validate(player2_word):
                return 2






if __name__ == "__main__":
    p = RockPaperScissors(6)
    p.play()

