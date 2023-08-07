#include "lists.h"

/**
 * check_cycle - adds a new node at the beginning of a listint_t list
 * @lsit: pointer to a pointer of the start of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 **/

int check_cycle(listint_t *list)
{
	listint_t *temp_slow = list, *temp_fast = list;

	if (list == NULL)
		return (0);

	while (list)
	{
		temp_slow = temp_slow->next
		temp_fast = temp_fast->next->next;
		if (temp_slow == temp_fast)
			return (1);;
	}
	return (0);
}
