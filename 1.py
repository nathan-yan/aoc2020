# day 1 
# part 1 -> 00:48:21 [5397th place]
# part 2 -> 00:51:10 [4936th place!]

match = set()

def f():
    with open('1.in', 'r') as f:
        lines = f.readlines()

        for l in lines:
            l = int(l)
            if l in match:
                print("part 1: %s" % (l * (2020 - l)))
                break;

            match.add(2020 - l)

        for i in range (len(lines)):
            for j in range (len(lines)):
                for k in range (len(lines)):
                    if i != j and j != k and i != k:
                        l1 = int(lines[i])
                        l2 = int(lines[j])
                        l3 = int(lines[k])

                        if l1 + l2 + l3 == 2020:
                            print("part 2: %s" % (l1 * l2 * l3))
                            return 

f()
                
