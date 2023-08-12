#include "lists.h"

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 **/

int is_palindrome(listint_t **head)
{
	listint_t *rev_list, *temp1, *new_node;

	if (head == NULL)
		return (0);

	rev_list = NULL;
	temp1 = *head;

	while (temp1)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (-1);
		new_node->n = temp1->n;
		new_node->next = rev_list;
		rev_list = new_node;
		temp1 = temp1->next;
	}

	temp1 = *head;

	while (temp1 && new_node)
	{
		if (temp1->n != new_node->n)
			return (0);
		temp1 = temp1->next;
		new_node = new_node->next;
	}
	return (1);
}
