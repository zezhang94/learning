#ifndef NODE
#define NODE

#include <stdlib.h>

struct Node {
	int key;
	int flag;
	struct Node *parent;
	struct Node *left;
	struct Node *right;
};

struct Node *new_node(int x);

#endif