class Some:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, nd_one):
        if self.x == nd_one.x:
            return self.y < nd_one.y
        else:
            return self.x < nd_one.x


# Accept number of elements from the user
n = int(input("Enter the number of elements: "))

lis = []
for _ in range(n):
    x = int(input("Enter x value: "))  # Input for x
    y = int(input("Enter y value: "))  # Input for y
    lis.append(Some(x, y))

# Sort the list based on __lt__ logic
lis.sort()

# Print the sorted list
for i in lis:
    print(i.x, i.y)
