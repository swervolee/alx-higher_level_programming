#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return 1;

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *stack = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        stack_push(&stack, slow->n);
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        int data = stack_pop(&stack);
        if (data != slow->n)
            return 0;
        slow = slow->next;
    }

    return 1;
}

/**
 * stack_push - pushes a value onto the stack
 * @stack: pointer to the top of the stack
 * @value: value to push onto the stack
 */
void stack_push(listint_t **stack, int value)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    new_node->n = value;
    new_node->next = *stack;
    *stack = new_node;
}

/**
 * stack_pop - pops a value from the stack
 * @stack: pointer to the top of the stack
 * Return: the value popped from the stack
 */
int stack_pop(listint_t **stack)
{
    if (*stack == NULL)
    {
        fprintf(stderr, "Stack is empty\n");
        exit(EXIT_FAILURE);
    }

    listint_t *top = *stack;
    *stack = top->next;
    int value = top->n;
    free(top);
    return value;
}
