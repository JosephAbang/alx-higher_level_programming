#include "lists.h"

/**
 * free_dlistint - Free a list
 * @head: Head of list
 * Return: void
 **/

void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp;

	while (head)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}
