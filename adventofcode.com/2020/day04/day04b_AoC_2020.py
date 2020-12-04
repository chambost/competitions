puzzleinput = r"""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

count = 0
passports = puzzleinput.split("\n\n")
for p in passports :
  entries = p.split()
  fields = set()
  validcount = 0
  for e in entries :
    field,value = e.split(":")
    fields.add(field)
    if field == "byr" :
        value = int(value)
        if 1920 <= value <= 2020 :
            validcount += 1
    if field == "iyr" :
        value = int(value)
        if 2010 <= value <= 2020 :
            validcount += 1
    if field == "eyr" :
        value = int(value)
        if 2020 <= value <= 2030 :
            validcount += 1
    if field == "hgt" :
        if value[-2:] == "cm" :
            value = int(value[:-2])
            if 150 <= value <= 193 :
                validcount += 1
        elif value[-2:] == "in" :
            value = int(value[:-2])
            if 59 <= value <= 76 :
                validcount += 1
    hexchars = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"}
    if field == "hcl" :
        if len(value) == 7 :
            if value[0] == "#" and value[1] in hexchars and value[2] in hexchars \
                    and value[3] in hexchars and value[4] in hexchars and value[5] in hexchars \
                    and value[6] in hexchars :
                validcount += 1
    if field == "ecl" :
        if value in { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" } :
              validcount += 1
    digits = { "0","1","2","3","4","5","6","7","8","9" }
    if field == "pid" :
        if len(value) == 9 :
            if value[0] in digits and value[1] in digits and value[2] in digits \
                    and value[3] in digits and value[4] in digits and value[5] in digits \
                    and value[6] in digits and value[7] in digits and value[8] in digits :
                validcount += 1
        
  if validcount == 7 :
    if fields == { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid" } :
        count += 1
    if fields == { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" } :
        count += 1
print(count)
