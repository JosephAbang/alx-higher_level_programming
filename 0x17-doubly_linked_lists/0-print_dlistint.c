#include "lists.h"

/**
 * print_dlistint - prints the elements of a linked list
 * @h: head of list
 * Return: length of list
 **/

size_t print_dlistint(const dlistint_t *h)
{
	size_t len = 0;
	const dlistint_t *temp = h;

	if (h == NULL)
		return (len);
	while (temp)
	{
		printf("%d\n", temp->n);
		temp = temp->next;
		len++;
	}
	return (len);
}
