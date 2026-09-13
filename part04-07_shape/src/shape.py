# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if string == "":
        print(number * "*")
    else:
        print(number * string[0])

def shape(size, character_triangle, height_rectangle, character_rectangle):
    i = 0
    j = 0
    while i < size:
        i += 1
        line(i, character_triangle)
    while j < height_rectangle:
        line(size, character_rectangle)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")