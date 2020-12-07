# day 3
# part 1 -> 00:03:29 [259th place]
# part 2 -> 00:04:50 [89th place!]

m = []

with open("3.in", 'r') as f:
    lines = f.readlines()

    for l in lines:
        m.append([i for i in l[:-1]])
    
    def getTrees(right, down):
        trees = 0
        start = [0, 0]
        while start[0] < len(m) - down:
            start[0] += down
            start[1] += right
            start[1] %= len(m[0])

            if m[start[0]][start[1]] == '#':
                trees += 1

        return trees
    
    # part 1
    print("part 1:", getTrees(3, 1)) 

    # part 2
    print("part 2:", getTrees(1, 1) * getTrees(3, 1) * getTrees(5, 1) * getTrees(7, 1) * getTrees(1, 2))

    