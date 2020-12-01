#ifndef BINARY_TREE
#define BINARY_TREE

#include <stdlib.h>
#include <node.h>
#include <consts.h>

struct BinaryTree {
	struct Node *root;
	struct Node *nil;
};

struct BinaryTree *new_binary_tree();

#endif