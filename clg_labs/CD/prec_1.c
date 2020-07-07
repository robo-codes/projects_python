/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

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
