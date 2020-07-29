#ifndef BINARY_SEARCH_TREE
#define BINARY_SEARCH_TREE

#include <node.h>
#include <stdio.h>

struct Node *insert(struct Node *T, struct Node *x);
void recursive_inorder_tree_walk(struct Node *start);
void iterative_inorder_tree_walk(struct Node *start);
struct Node *recursive_search(struct Node *start, int key);
struct Node *iterative_search(struct Node *start, int key);
struct Node *minimum(struct Node *start);
struct Node *maximum(struct Node *start);
struct Node *successor(struct Node *target);
struct Node *predecessor(struct Node *target);
struct Node *deletion(struct Node *T, struct Node *target);

#endif