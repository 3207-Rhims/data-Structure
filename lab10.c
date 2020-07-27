/*C String function – strlen
Syntax:

size_t strlen(const char *str)
size_t represents unsigned short
It returns the length of the string without including end character (terminating char ‘\0’).

Example of strlen: */

#include <stdio.h>
#include <string.h>
int main()
{
     char str1[20] = "BeginnersBook";
     printf("Length of string str1: %d", strlen(str1));
     return 0;
}

