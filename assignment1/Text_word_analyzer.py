word_list= []
vowels=0
consonents=0
longest=""
short=0
medium=0
large=0
word= input("Ënter the Words: " ).lower()
while word!="end":
    if word=="":
        continue
    else:
        if 1<=len(word)<=3:
            short+=1
        elif (3<len(word)<=7):
            medium+=1
        else:
            large
        word_list.append(word)
        if len(longest)<len(word):
            longest=word
        for char in word:
            if char =="a" or char=="e" or char=="i" or char=="o" or char=="u":
                vowels+=1
            else:
                consonents+=1
    word= input("Ënter the Words: " ).lower()
print(f"The total Wordsare: {len(word_list)}")
print(f"Total Vowels: {vowels}")
print(f"Total Consonents: {consonents}")
print(f"The short words  are {short}")
print(f"The medium words  are {medium}")
print(f"The long words  are {longest}")


            

    
