#include "lists.h"

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *temp1 = *h, *temp2 = *h, *new_node;
	unsigned int cnt;

	while (temp1)
	{
		temp1 = temp1->next;
		cnt++;	
	}
	if (idx > cnt)
		return (NULL);
	else if (idx == 0)
		return (add_dnodeint(h, n));
	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return NULL;
	temp1 = *h;
	while (idx != 1)
	{
		temp1 = temp1->next;
		idx--;
	}
	if (temp1->next == NULL)
		return (add_dnodeint_end(h, n));
	else
	{
		new_node->n = n;
		temp2 = temp1->next;
		new_node->prev = temp1;
		new_node->next = temp2;
		temp2->prev = new_node;
		temp1->next = new_node;
	}
	return (new_node);
}
