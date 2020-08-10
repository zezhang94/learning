#ifndef BINARY_SEARCH_TREE
#define BINARY_SEARCH_TREE

#include <node.h>
#include <stdio.h>
#include <consts.h>
#include <binary_tree.h>

void insert(struct BinaryTree *binaryTree, struct Node *x);
void recursive_inorder_tree_walk(struct BinaryTree *binaryTree, struct Node *start);
void iterative_inorder_tree_walk(struct BinaryTree *binaryTree, struct Node *start);
struct Node *recursive_search(struct BinaryTree *binaryTree, struct Node *start, int key);
struct Node *iterative_search(struct BinaryTree *binaryTree, struct Node *start, int key);
struct Node *minimum(struct BinaryTree *binaryTree, struct Node *start);
struct Node *maximum(struct BinaryTree *binaryTree, struct Node *start);
struct Node *successor(struct BinaryTree *binaryTree, struct Node *target);
struct Node *predecessor(struct BinaryTree *binaryTree, struct Node *target);
void deletion(struct BinaryTree *binaryTree, struct Node *target);

#endif