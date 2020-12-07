# day 2
# part 1 -> 00:03:52 [352th place]
# part 2 -> 00:05:17 [172th place!]

with open('2.in', 'r') as f:
    lines = f.readlines()
    c = 0
    d = 0
    for l in lines:
        nums = l.split(" ")
        occ = nums[0].split('-')
        least = int(occ[0])
        most = int(occ[1])

        letter = nums[1][-2]

        password = nums[2]

        #print(least, most, letter, password)

        if (most >= password.count(letter) >= least):
            d += 1

        if (password[least - 1] == letter ) ^ (password[most - 1] == letter):
            c += 1
    
    print("part 1: %s" % d) 
    print("part 2: %s" % c)
