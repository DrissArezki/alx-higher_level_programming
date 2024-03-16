#ifndef LISTS
#define LISTS

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * struct listint_s - singly linked list
 * @n: int
 * @next: pointer to the next node
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t




#endif
