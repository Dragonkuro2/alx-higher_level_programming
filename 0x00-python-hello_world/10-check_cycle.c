#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - this function checks if there's a cycle or no
 * @list: the input pointer of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t* here = list;
	listint_t* next_one = list;

	while (next_one != NULL && next_one->next != NULL)
	{
		here = here->next;
		next_one = next_one->next->next;
		if (next_one == here)
			return (1);
	}
	return (0);
}
