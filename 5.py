# day 5
# part 1 -> 00:04:12 [138th place]
# part 2 -> 00:11:34 [729th place]

with open("5.in", 'r') as f:
    lines = f.readlines()

    seats = set()
    for row in range (128):
        for col in range (9):
            seats.add((row, col))
    
    seen = set()

    ma = 0
    for l in lines:
        # convert first seven characters
        l = l.replace("B", '1').replace("F", '0').replace("R", '1').replace("L", '0')
        row = int(l[:7], 2)

        col = int(l[-4:-1], 2)
        i = row * 8 + col

        if i > ma:
            ma = i

        seen.add((row, col))
        
        if (row, col) in seats:
            seats.remove((row, col))
    
    for candidate in seats:
        c1 = (candidate[0], candidate[1] + 1)
        if candidate[1] == 7:
            c1 = (candidate[0] + 1, 0)

        c2 = (candidate[0], candidate[1] - 1)

        if candidate[1] == 0:
            c2 = (candidate[0] - 1, candidate[1] + 7)
        
        if c1 in seen and c2 in seen:
            print(candidate[0] * 8 + candidate[1])

    print(seats)
        
    print(ma)