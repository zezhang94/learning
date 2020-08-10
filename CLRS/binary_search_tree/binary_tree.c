#include <binary_tree.h>

struct BinaryTree *new_binary_tree() {
	struct Node *nil = new_nil();
	struct Node *root = nil;
	
	struct BinaryTree *binaryTree = malloc(sizeof(struct BinaryTree));
	binaryTree->root = root;
	binaryTree->nil = nil;
	return binaryTree;
}