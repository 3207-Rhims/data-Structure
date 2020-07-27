/*C String function – strncat
char *strncat(char *str1, char *str2, int n)
It concatenates n characters of str2 to string str1. A terminator char (‘\0’) will always be appended at the end of the concatenated string.

Example of strncat:*/

#include <stdio.h>
#include <string.h>
int main()
{
     char s1[10] = "Hello";
     char s2[10] = "World";
     strncat(s1,s2, 3);
     printf("Concatenation using strncat: %s", s1);
     return 0;
}
