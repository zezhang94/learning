#include <node.h>

struct Node *new_node(int x, enum red_black color, struct Node *nil) {
	struct Node *node = malloc(sizeof(struct Node));
	node->key = x;
	node->flag = 1;
	node->parent = nil;
	node->left = nil;
	node->right = nil;
	node->succ = nil;
	node->color = color;
	return node;
}

struct Node *new_nil() {
	struct Node *node = malloc(sizeof(struct Node));
	node->color = Black;
	return node;
}
