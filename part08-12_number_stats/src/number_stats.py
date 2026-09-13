# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers) / len(self.numbers)

def main():
    print("Please type in integer numbers:")
    stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()

    while True:
        
        
        number = int(input())
        if number == -1:
            break
        stats.add_number(number)

        if number % 2 == 0:
            even_stats.add_number(number)
        else:
            odd_stats.add_number(number)



    
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", even_stats.get_sum())
    print("Sum of odd numbers:", odd_stats.get_sum())



main()