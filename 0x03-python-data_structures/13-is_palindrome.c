#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

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


int check(int *list, int idx1, int idx2)
{
	if (idx1 >= idx2)
	{
		return (1);
	}

	if (list[idx1] != list[idx2])
	{
		return (0);
	}

	return check(list, idx1 + 1, idx2 -1);
}
