#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	int *values = NULL;
	size_t i;
	listint_t *current = *head;
	size_t values_count = 0;

	while (current)
	{
		values = realloc(values, sizeof(int) * ++values_count);
		if (!values)
		{
			return (0);
		}
		values[values_count - 1] = current->n;
		current = current->next;
	}
	for (i = 0; i < values_count / 2; i++)
	{
		if (values[i] != values[values_count - i - 1])
		{
			free(values);
			return (0);
		}
	}
	free(values);
	return (1);
}
