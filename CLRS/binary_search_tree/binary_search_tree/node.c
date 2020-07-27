#include <node.h>

struct Node *new_node(int x) {
	struct Node *node = malloc(sizeof(struct Node));
	node->key = x;
	node->flag = 1;
	node->parent = NULL;
	node->left = NULL;
	node->right = NULL;
	return node;
}