#include "palindrome.h"
#include <stdio.h>

/**
 * is_palindrome - Check integer is a palindrome
 * @n: The number to be check
 *
 * Return:
 */
int is_palindrome(unsigned long n)
{
    unsigned long original = n;
    unsigned long reversed = 0;

    while (n > 0)
    {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }

    return (original == reversed);
}
