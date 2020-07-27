/*C String function – strchr
char *strchr(char *str, int ch)
It searches string str for character ch (you may be wondering that in above definition I have given data type of ch as int, don’t worry I didn’t make any mistake it should be int only. The thing is when we give any character while using strchr then it internally gets converted into integer for better searching.

Example of strchr:*/


#include <stdio.h>
#include <string.h>
int main()
{
     char mystr[30] = "I’m an example of function strchr";
     printf ("%s", strchr(mystr, 'f'));
     return 0;
}
