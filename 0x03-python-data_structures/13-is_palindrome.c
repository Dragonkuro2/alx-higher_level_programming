#include "lists.h"
#include<stddef.h>

/**
 * reverse_listint - This function Reverses a singly-linked.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *preve = NULL;

	while (node)
	{
		next = node->next;
		node->next = preve;
		preve = node;
		node = next;
	}

	*head = preve;
	return (*head);
}

/**
 * is_palindrome - This function Checks if a singly linked list is a palindrome
 * @head: A pointer to the head of the linked-list.
 * Return: If the linked list is not a palindrome return 0.
 *         If the linked list is a palindrome return 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *reve, *mide;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	reve = reverse_listint(&tmp);
	mide = reve;

	tmp = *head;
	while (reve)
	{
		if (tmp->n != reve->n)
			return (0);
		tmp = tmp->next;
		reve = reve->next;
	}
	reverse_listint(&mide);

	return (1);
}
