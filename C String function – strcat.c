C String function – strcat
char *strcat(char *str1, char *str2)
It concatenates two strings and returns the concatenated string.

Example of strcat:

#include <stdio.h>
#include <string.h>
int main()
{
     char s1[10] = "Hello";
     char s2[10] = "World";
     strcat(s1,s2);
     printf("Output string after concatenation: %s", s1);
     return 0;
}
