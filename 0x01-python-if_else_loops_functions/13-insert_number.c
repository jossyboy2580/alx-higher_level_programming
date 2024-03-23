#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *moving_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!moving_node)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		while (moving_node->next->n < number && moving_node->next != NULL)
			moving_node = moving_node->next;
		new_node->next = moving_node->next;
		moving_node->next = new_node;
	}
	return (new_node);
}
