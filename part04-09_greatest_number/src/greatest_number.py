# Write your solution here
def greatest_number(no1, no2, no3):
    if no1 >= no2 and no1 >= no3:
        return no1
    elif no1 <= no2 and no2 >= no3:
        return no2
    else: 
        return no3
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)