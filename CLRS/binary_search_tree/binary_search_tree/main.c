#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <node.h>
#include <binary_search_tree.h>

int main(int argc, char **argv)
{
	srand(time(NULL));
	printf("Build start.\n");
	struct Node *T = NULL;
	for (int i = 0; i != 20; ++i) {
		int key = rand() % 5;
		struct Node *node = new_node(key);
		T = insert(T, node);
	}
	printf("Build end.\n\n");
	
	recursive_inorder_tree(T);
	printf("\n");
	
	return 0;
}
