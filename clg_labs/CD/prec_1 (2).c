#include<stdio.h>
#include<conio.h>
void main ()
{
    char a[100];
    int i = 2, j = 0, count = 0;
    printf("Enter Line:\n");
    gets(a);
    if(a[0] == '/')
    {
        if(a[1] == '/')
        {
            printf("It is a comment.\n");
        }
    }
    else if(a[0] == '*')
        {
            if(a[1] == '/')
            {
                while(a[i] != "*")
                {
                    count++;
                }
                printf("%c",count);
            }
        }

    else
    {
        printf("not a comment");
    }
}
