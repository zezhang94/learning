#include <stdio.h>
#include <binary_search_tree.h>

struct Node *insert(struct Node *T, struct Node *x) {
	
	if (T == NULL) {
		T = x;
		return T;
	}
	
	struct Node *current = T;
	struct Node *pre = NULL;
	while (current != NULL) {
		pre = current;
		if (x->key < current->key) {
			current = current->left;
		} else if (x->key > current->key) {
			current = current->right;
		} else {
			if (current->flag > 0) {
				if (current->left != NULL) {
					current->left->parent = x;
				}
				x->left = current->left;
				current->left = x;
			} else {
				if (current->right != NULL) {
					current->right->parent = x;
				}
				x->right = current->right;
				current->right = x;
			}
			x->parent = current;
			current->flag = 0 - current->flag;
			return T;
		}
	}
	
	if (x->key < pre->key) {
		pre->left = x;
	} else {
		pre->right = x;
	}
	x->parent = pre;
	return T;
}

void recursive_inorder_tree(struct Node *node) {
	if (node != NULL) {
		recursive_inorder_tree(node->left);
		printf("%d ", node->key);
		recursive_inorder_tree(node->right);
	}
};

void iterative_inorder_tree(struct Node *start) {
};
