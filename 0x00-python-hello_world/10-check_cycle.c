#include "lists.h"
/**
 *check_cycle - checks for a cycle in a linked list
 *@list: the linked list to check
 *Return: 1 if cycle is present else 0
 */

int check_cycle(listint_t *list)
{
	int rtn = 0;
	listint_t *check1 = list, *check2 = list;

	while (check1 && check2 != NULL)
	{
		check1 = check1->next;
		check2 = check2->next->next;

		if (check1 == check2)
		{
			rtn = 1;
			break;
		}
	}

	return (rtn);
}
