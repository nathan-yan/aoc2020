# day 7
# part 1 -> 00:08:35 [93rd place!]
# part 2 -> 00:11:32 [48th place!]

with open("7.in", 'r') as f:
    rules = f.readlines()

    contains = {}
    for r in rules:
        target, bags = r.split(" contain ") 
        if 'no' in bags:
            contains[target.replace(" bags", "")] = [] 
        else:
            bags = [(' '.join(b.split(' ')[1:-1]), int(b.split(' ')[0])) for b in bags.split(", ")]
            contains[target.replace(' bags', '')] = bags

    def check(r):
        for e in contains[r]:
            if e[0] == 'shiny gold':
                return True
        if contains[r] == []:
            return False 
        
        for n in contains[r]:
            if check(n[0]):
                return True 
            
        return False
    
    def count(r):
        if len(contains[r]) == 0:
            return 0
        else:
            c = 0
            for n in contains[r]:
                c += n[1] + n[1] * count(n[0])
            
            return c
    
    p1 = 0
    for r in contains:
        p1 += check(r)
    
    print("part 1:", p1)
    print("part 2:", count('shiny gold'))

    