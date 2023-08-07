#include "lists.h"

/**
 * check_cycle - adds a new node at the beginning of a listint_t list
 * @lsit: pointer to a pointer of the start of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 **/

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (temp == NULL)
		return (0);

	while (temp)
	{
		if (temp->next == NULL)
			return (0);
		temp = temp->next;
		if (temp == list)
			break;
	}
	return (1);
}
