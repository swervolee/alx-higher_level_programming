#include "lists.h"
/**
 *check_cycle - checks for a cycle in a linked list
 *@list: the linked list to check
 *Return: 1 if cycle is present else 0
 */

int check_cycle(listint_t *list)
	{
	listint_t *p2;
	listint_t *prev;

	p2 = list;
	prev = list;
	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;

		if (list == p2)
		{
			list = prev;
			prev =  p2;
			while (1)
			{
				p2 = prev;
				while (p2->next != list && p2->next != prev)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
/*{
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
*/
