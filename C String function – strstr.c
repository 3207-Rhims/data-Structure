C String function – strstr
char *strstr(char *str, char *srch_term)
It is similar to strchr, except that it searches for string srch_term instead of a single char.

Example of strstr:

#include <stdio.h>
#include <string.h>
int main()
{
     char inputstr[70] = "String Function in C at BeginnersBook.COM";
     printf ("Output string is: %s", strstr(inputstr, 'Begi'));
     return 0;
}
