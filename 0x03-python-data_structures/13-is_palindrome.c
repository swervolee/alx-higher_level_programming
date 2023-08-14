#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *is_palindrome - verifys if a linked list is a palindrome
 *@head: first element of the palindrome
 *Return:1 if palindrome, else zero
 */

int is_palindrome(listint_t **head)
{
	int i, k;
	int *list = NULL;
	listint_t *current = *head;

	for (i = 0; current != NULL; i++)
	{
		current = current->next;
	}

	list = malloc(i * sizeof(int));
	if (!list)
	{
		exit(EXIT_FAILURE);
	}

	current = *head;

	for (k = 0; current != NULL; k++)
	{
		list[k] = current->n;
		current = current->next;
	}

	return (check(list, 0, k - 1));
}

/**
 *check - a helper function to check for palindrome
 *@list: an array containing the linked lists elements
 *@idx1: first index
 *@idx2: last index
 *Return: 1 if palindrome else 0
 */

int check(int *list, int idx1, int idx2)
{

	for (idx1, idx2; idx1 < idx2; idx1++, idx2--)
	{
		if (list[idx1] != list[idx2])
		{
			{
				return (0);
			}
		}
	}
	return (1);
}
