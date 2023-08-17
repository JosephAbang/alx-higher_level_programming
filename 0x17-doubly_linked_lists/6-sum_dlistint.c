#include "lists.h"

/**
 * sum_dlistint - Sums data in linked list
 * @head: head of list
 * Return: the sum of all the data (n) of a dlistint_t linked list
 */


int sum_dlistint(dlistint_t *head)
{
	dlistint_t *temp;
	int result = 0;

	if (head == NULL)
		return (result);
	temp = head;
	while (temp)
	{
		result += temp->n;
		temp = temp->next;
	}
	return (result);
}
