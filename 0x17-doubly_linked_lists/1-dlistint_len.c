#include "lists.h"

/**
 * dlistint_len - Gets length of list
 * @h: Head of list
 * Return: Lengtg of list
 */


size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *temp = h;
	size_t len = 0;

	if (h == NULL)
		return (len);

	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (len);
}
