three = 0
previous = -1
answers = set()
while True : 
    previous = three
        
    two = three | 0b10000000000000000
    three = 7637914
    while True : 
        three += two & 255
        three &= 0b111111111111111111111111
        three *= 65899
        three &= 0b111111111111111111111111
        
        if two >= 256 :
            two //= 256
        else : 
            break
            
    if three in answers :
        break
    answers.add(three)
          
print(previous)
