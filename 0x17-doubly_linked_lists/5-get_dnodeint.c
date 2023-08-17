#include "lists.h"

/**
 * get_dnodeint_at_index - Get the nth index of the list
 * @head: Head of the list
 * @index: index rto be returned
 * Return: the nth node of a dlistint_t linked list
 **/

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *temp;
	unsigned int cnt = 0;

	if (head == NULL)
		return (NULL);
	temp = head;
	while (temp->next)
	{
		if (index == cnt)
			return (temp);
		temp = temp->next;
		cnt++;
	}
	return (NULL);
}
