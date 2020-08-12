#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <node.h>
#include <binary_search_tree.h>
#include <consts.h>
#include <binary_tree.h>

int const data_range = 100;
int const tree_size = 10;

int main(int argc, char **argv) {
	//normal_banary_search_tree();
	rb_tree();
	return 0;
}

void normal_banary_search_tree() {
	
	srand(time(NULL));
	printf("Build start.\n");
	struct BinaryTree *binaryTree = new_binary_tree();
	// for test
	struct Node *node_arr[tree_size];
	int count = 1;
	printf("Source sequence:\n");
	for (int index = 0; index != tree_size; ++index) {
		int key = rand() % data_range;
		struct Node *node = new_node(key, Red, binaryTree->nil);
		printf("%p---%d ", (void*) node, key);
		if (!(count++ % 4)) {
			printf("\n");
		}
		node_arr[index] = node;
		insert(binaryTree, node);
	}
	if (count % 4 != 1) {
		printf("\n");
	}
	printf("Build end.\n\n");
	
	printf("Iterative inorder walk tree without stack.\n");
	iterative_inorder_tree_walk(binaryTree, binaryTree->root);
	printf("\n\n");
	
	printf("Recursive inorder walk tree.\n");
	recursive_inorder_tree_walk(binaryTree, binaryTree->root);
	printf("\n\n");
	
	int target = rand() % data_range;
	struct Node *target_node = iterative_search(binaryTree, binaryTree->root, target);
	printf("Search target: %d\n", target);
	printf("Iterative search result: [%p] --- [%d]\n", (void*) target_node, target_node != NULL ? target_node->key : -1);
	target_node = recursive_search(binaryTree, binaryTree->root, target);
	printf("Recursive search result: [%p] --- [%d]\n", (void*) target_node, target_node != NULL ? target_node->key : -1);
	printf("\n");
	
	struct Node *min = minimum(binaryTree, binaryTree->root);
	printf("Minimun: %d\n", min->key);
	struct Node *max = maximum(binaryTree, binaryTree->root);
	printf("Maximun: %d\n", max->key);
	printf("\n");
		
	for (int index = 0; index != tree_size; ++index) {
		struct Node *successor_node = successor(binaryTree, node_arr[index]);
		struct Node *predecessor_node = predecessor(binaryTree, node_arr[index]);
		printf("Node [%p] --- [%d], successor [%p] --- [%d], predecessor [%p] --- [%d]\n", 
			(void*) node_arr[index], node_arr[index]->key,
			(void*) successor_node, successor_node != NULL ? successor_node->key : -1,
			(void*) predecessor_node, predecessor_node != NULL ? predecessor_node->key : -1
		);
	}
	printf("\n");
	
	for (int index = 0; index != tree_size; ++index) {
		printf("Deletion target: [%p] --- [%d]\n", (void*) node_arr[index], node_arr[index]->key);
		deletion(binaryTree, node_arr[index]);
		printf("After deletion: ");
		recursive_inorder_tree_walk(binaryTree, binaryTree->root);
		printf("\n");
	}
	printf("\n");
	for (int index = 0; index != tree_size; ++index) {
		printf("%p ", (void*) node_arr[index]);
	}
	printf("\n");
	
}

void rb_tree() {
	
	srand(time(NULL));
	printf("Build start.\n");
	struct BinaryTree *binaryTree = new_binary_tree();
	// for test
	struct Node *node_arr[tree_size];
	int count = 1;
	printf("Source sequence:\n");
	for (int index = 0; index != tree_size; ++index) {
		int key = rand() % data_range;
		struct Node *node = new_node(key, Red, binaryTree->nil);
		printf("%p---%d ", (void*) node, key);
		if (!(count++ % 4)) {
			printf("\n");
		}
		node_arr[index] = node;
		rb_insert(binaryTree, node);
	}
	if (count % 4 != 1) {
		printf("\n");
	}
	printf("Build end.\n\n");
	
	printf("Iterative inorder walk tree without stack.\n");
	iterative_inorder_tree_walk(binaryTree, binaryTree->root);
	printf("\n\n");
	
	printf("nil [%p]\n", (void*) binaryTree->nil);
	for (int index = 0; index != tree_size; ++index) {
		struct Node *node = node_arr[index];
		printf("self [%p] parent [%p] left [%p] right [%p] color [%s] key [%d]", 
			(void*) node, (void*) node->parent, (void*) node->left, (void*) node->right, 
			node->color == Black ? "B" : "R", node->key);
		printf("\n");
	}
}
