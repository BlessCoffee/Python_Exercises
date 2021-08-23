s = 'boboboboboboboobbbbobobobbdfdfdfsdbob'
bobs = 0
for num in range(len(s)):
    if(num+1 > len(s)):
        break
    if(num+2 > len(s)):
        break
    if(s[num] == 'b'):
        if(s[num+1] == 'o'):
            if(s[num+2] == 'b'):
                bobs+=1
print("Number of times bob occurs is : " + str(bobs))
