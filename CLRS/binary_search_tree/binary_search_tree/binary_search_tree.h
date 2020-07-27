#ifndef BINARY_SEARCH_TREE
#define BINARY_SEARCH_TREE

#include <node.h>
#include <stdio.h>

struct Node *insert(struct Node *T, struct Node *x);
void recursive_inorder_tree(struct Node *start);
void iterative_inorder_tree(struct Node *start);
#endif