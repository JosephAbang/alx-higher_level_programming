#include "lists.h"

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *temp = *head, *new_node;
	unsigned int cnt;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return NULL;
	new_node->n = n;
	while (temp)
	{
		if (idx == cnt)
		{
			if (temp->next == NULL)
			{
				new_node->next = NULL;
				new_node->prev = temp;
				temp->next = new_node;
			}
			else if (temp->prev == NULL)
			{
				new_node->next = temp;
				new_node->prev = NULL;
				temp->next = NULL;
				temp->prev = new_node;
				*head = new_node
			}
			else
			{
				new_node->next = temp;
				new_node->prev = temp->prev;
				temp->prev = new_node;
			}
		}
		temp = temp->next;
	}
}
