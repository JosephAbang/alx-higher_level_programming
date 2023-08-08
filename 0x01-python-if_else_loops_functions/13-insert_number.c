#include "lists.h"

/**
 * insert_node - Inserts a node
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node = *head;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current_node->next && (current_node->next->n < number))
	{
		current_node = current_node->next;
	}
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
