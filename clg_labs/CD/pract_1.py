pt ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
ct ={'Z','X','Y','W','U','V','T','R','S','Q','O','P','N','L','M','K','I','J','H','F','G','E','C','D','A','B'}
text=str{'\0'}
dtext=str{'\0'}
c=str{'\0'}
t,d,i,j=0,0,0,0
text = input("\n Enter a message to encrypt: ")
while (text[t] != '\0'):
    if (text[t] == ' '):
        temp = t
        if (text[temp] != '\0'):
            while (text[temp] == ' ' and text[temp] != '\0'):
                if (text[temp] == ' '):
                    t+=1
                temp+=1
    dtext[d] = text[t]
    t+=1
    d+=1
print("\n Text after removing blanks : "+dtext)
for i in len(dtext):
    for j in range(0,26):
        if(pt[j]==dtext[i]):
            c[i]=ct[j]
print("\n Encrypted message: "+c)
