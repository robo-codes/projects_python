#include<stdio.h>
#include<conio.h>
void main ()
{
    char a[100];
    int i = 2, j = 0, l = 0;
    printf("Enter Line:\n");
    gets(a);
    if(a[0] == '/')
    {
        if(a[1] == '/')
        {
            printf("It is a comment.\n");
        }
        else
        {
            printf("Not a comment");
        }
    }
    else if(a[0] == '*')
        {
            if(a[1] == '/')
            {
                l = strlen(a);
                if(a[l-2] == '/' && a[l-1] == '*')
                {
                    printf("It is a comment.\n");
                }
                else
                {
                    printf("Not a comment.\n");
                }
            }
        }

    else
    {
        printf("Not a comment");
    }
}
