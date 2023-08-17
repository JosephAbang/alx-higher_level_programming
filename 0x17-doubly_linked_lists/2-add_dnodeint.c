#include "lists.h"

/**
 * add_dnodeint - Add node at beginning of list
 * @head: Head of list
 * @n: node data
 * Return: address of new node
 **/

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node = *head;

	new_node = malloc(sizeof(dlistint_t));
	new_node->n = n;
	new_node->prev = NULL;

	if (*(head) == NULL)
	{
		new_node->next = NULL;
		(*head) = new_node;
	}

	else {
		new_node->next = *head;
		(*head)->prev = new_node;
		*head = new_node;
	}
	return (new_node);
}
