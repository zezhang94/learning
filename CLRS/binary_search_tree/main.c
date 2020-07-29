#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <node.h>
#include <binary_search_tree.h>

int const data_range = 100;
int const tree_size = 10;

int main(int argc, char **argv)
{
	srand(time(NULL));
	printf("Build start.\n");
	struct Node *T = NULL;
	// for test
	struct Node *node_arr[tree_size];
	int count = 1;
	printf("Source sequence:\n");
	for (int index = 0; index != tree_size; ++index) {
		int key = rand() % data_range;
		struct Node *node = new_node(key);
		printf("%p---%d ", (void*) node, key);
		if (!(count++ % 4)) {
			printf("\n");
		}
		node_arr[index] = node;
		T = insert(T, node);
	}
	if (count % 4 != 1) {
		printf("\n");
	}
	printf("Build end.\n\n");
	
	printf("Iterative inorder walk tree without stack.\n");
	iterative_inorder_tree_walk(T);
	printf("\n\n");
	
	printf("Recursive inorder walk tree.\n");
	recursive_inorder_tree_walk(T);
	printf("\n\n");
	
	int target = rand() % data_range;
	struct Node *target_node = iterative_search(T, target);
	printf("Search target: %d\n", target);
	printf("Iterative search result: [%p] --- [%d]\n", (void*) target_node, target_node != NULL ? target_node->key : -1);
	target_node = recursive_search(T, target);
	printf("Recursive search result: [%p] --- [%d]\n", (void*) target_node, target_node != NULL ? target_node->key : -1);
	printf("\n");
	
	struct Node *min = minimum(T);
	printf("Minimun: %d\n", min->key);
	struct Node *max = maximum(T);
	printf("Maximun: %d\n", max->key);
	printf("\n");
		
	for (int index = 0; index != tree_size; ++index) {
		struct Node *successor_node = successor(node_arr[index]);
		struct Node *predecessor_node = predecessor(node_arr[index]);
		printf("Node [%p] --- [%d], successor [%p] --- [%d], predecessor [%p] --- [%d]\n", 
			(void*) node_arr[index], node_arr[index]->key,
			(void*) successor_node, successor_node != NULL ? successor_node->key : -1,
			(void*) predecessor_node, predecessor_node != NULL ? predecessor_node->key : -1
		);
	}
	printf("\n");
	
	for (int index = 0; index != tree_size; ++index) {
		printf("Deletion target: [%p] --- [%d]\n", (void*) node_arr[index], node_arr[index]->key);
		T = deletion(T, node_arr[index]);
		printf("After deletion: ");
		recursive_inorder_tree_walk(T);
		printf("\n");
	}
	printf("\n");
	for (int index = 0; index != tree_size; ++index) {
		printf("%p ", (void*) node_arr[index]);
	}
	printf("\n");
	return 0;
}
