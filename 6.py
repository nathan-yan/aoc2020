# day 6
# part 1 -> 00:03:28 [365th  place]
# part 2 -> 00:09:57 [1092th place]

with open("6.in" , 'r') as f:
    lines = f.readlines()
    c = 0
    acc = ''
    count = 0
    for l in lines:
        if l == '\n':
            prev = None
            counts = {}

            for person in acc.split('\n')[:-1]:
                
                
                for c in person:
                    if c != '\n':
                        if c in counts:
                            counts[c] += 1
                        else:
                            counts[c] = 1
                

            for c in counts:
                if counts[c] == len(acc.split("\n")) - 1:
                    count+=1

            acc = ''
        else:
            acc += l
    print(count)
                