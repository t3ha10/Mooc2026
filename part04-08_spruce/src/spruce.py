# Write your solution here
def spruce2(size):
    print("a spruce!")
    i = 0
    sequence = ""
    while i < size:
        i += 1
        sequence += (size - i) * " " + "*" * (2 * i - 1) + "\n"

    sequence += " " * (size - 1) + "*"
    print(sequence)

def spruce(size):
    print("a spruce!")
    i = 0

    while i < size:
        i += 1

        # ...
        line_staring_space = (size - i) * " "
        # ...
        line_body = "*" * (2 * i - 1)

        print(line_staring_space + line_body)

    stump = " " * (size - 1) + "*"
    print(stump)


        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(4)