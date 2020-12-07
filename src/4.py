# day 4
# part 1 -> 00:08:54 [1105th place]
# part 2 -> 00:14:40 [157th  place]

with open("../inputs/4.in", 'r') as f: 
    lines = f.readlines()
    passport = ""
    valid = 0
    passports = 0
    print(len(lines))
    for l in lines:
        
        if l == '\n':
            #print(passport)
            keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            split = passport.split(" ")
            #print(split)
            for i in range (len(split)):
                s = split[i].split(":")
               
                if s[0] == 'byr' and 2002 >= int(s[1]) >= 1920:
                    del keys[keys.index(s[0])]
                

                if s[0] == 'iyr' and 2020 >= int(s[1]) >= 2010:
                    del keys[keys.index(s[0])]

                
                if s[0] == 'eyr' and 2030 >= int(s[1]) >= 2020:
                    del keys[keys.index(s[0])]
                
                if s[0] == 'hgt' and s[1][-2:] in ['cm', 'in']:
                    if (s[1][-2:] == 'cm' and 193 >= int(s[1][:-2]) >= 150) or (s[1][-2:] == 'in' and 76 >= int(s[1][:-2]) >= 59):
                        del keys[keys.index(s[0])]
                
                if s[0] == 'hcl' and s[1][0] == '#' and len(s[1]) == 7:
                    for c in s[1][1:]:
                        if c not in '0123456789abcdef':
                            break;
                    else:
                        del keys[keys.index(s[0])]

                if s[0] == 'ecl' and s[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    del keys[keys.index(s[0])]
                if s[0] == 'pid' and len(s[1]) == 9:
                    del keys[keys.index(s[0])]
                
             
                
                #print(s[0])
            #print(keys)
            if len(keys) == 0:
                valid += 1
            passports += 1 
            passport = ''
        else:
            passport += l.replace("\n", ' ')

    print(valid)
    print(passports)