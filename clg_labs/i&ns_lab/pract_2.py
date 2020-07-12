'''#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
    char pt[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    char ct[26]={'Z','X','Y','W','U','V','T','R','S','Q','O','P','N','L','M','K','I','J','H','F','G','E','C','D','A','B'};
    char text[20]={'\0'},dtext[20]={'\0'},c[20]={'\0'},r[20]={'\0'};
    int i,j,t,d;
    clrscr();
    printf("\n Enter a message to encrypt: ");
    gets(text);
	while (text[t] != '\0')
	{
		if (text[t] == ' ')
		{
			int temp = t ;
			if (text[temp] != '\0')
			{
				while (text[temp] == ' ' && text[temp] != '\0')
				{
					if (text[temp] == ' ')
					{
						t++;
					}
					temp++;
				}
			}
		}
		dtext[d] = text[t];
		t++;
		d++;
	}
	printf("\n Text after removing blanks : %s", dtext);
    for(i=0;i<strlen(dtext);i++)
    {
		for(j=0;j<26;j++)
		{
			if(pt[j]==dtext[i])
			{
				c[i]=ct[j];
			}
		}
    }
    printf("\n Encrypted message: %s",c);
	return 0;
}'''

pt ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
ct ={'Z','X','Y','W','U','V','T','R','S','Q','O','P','N','L','M','K','I','J','H','F','G','E','C','D','A','B'}
text={'\0'}
dtext={'\0'}
c={'\0'}
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
