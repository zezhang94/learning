#ifndef NODE
#define NODE

#include <stdlib.h>
#include <consts.h>

struct Node {
	int key;
	int flag;
	enum red_black color;
	struct Node *parent;
	struct Node *left;
	struct Node *right;
	// successor
	struct Node *succ;
};

struct Node *new_node(int x, enum red_black color, struct Node *nil);
struct Node *new_nil();

#endif