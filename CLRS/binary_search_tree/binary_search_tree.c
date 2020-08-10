#include <stdio.h>
#include <stdlib.h>
#include <binary_search_tree.h>

void insert(struct BinaryTree *binaryTree, struct Node *x) {
	
	if (binaryTree->root == binaryTree->nil) {
		binaryTree->root = x;
		return;
	}
	
	struct Node *current = binaryTree->root;
	struct Node *pre = binaryTree->nil;
	while (current != binaryTree->nil) {
		pre = current;
		if (x->key < current->key) {
			current = current->left;
		} else if (x->key > current->key) {
			current = current->right;
		} else {
			if (current->flag > 0) {
				if (current->left != binaryTree->nil) {
					current->left->parent = x;
				}
				x->left = current->left;
				current->left = x;
			} else {
				if (current->right != binaryTree->nil) {
					current->right->parent = x;
				}
				x->right = current->right;
				current->right = x;
			}
			x->parent = current;
			current->flag = 0 - current->flag;
			return;
		}
	}
	
	if (x->key < pre->key) {
		pre->left = x;
	} else {
		pre->right = x;
	}
	x->parent = pre;
}

struct Node *right_most(struct BinaryTree *binaryTree, struct Node *start) {	
	struct Node *current = start;
	while (current->right != binaryTree->nil) {
		current = current->right;
	}
	return current;
}

struct Node *left_most(struct BinaryTree *binaryTree, struct Node *start) {	
	struct Node *current = start;
	while (current->left != binaryTree->nil) {
		current = current->left;
	}
	return current;
}

void recursive_inorder_tree_walk(struct BinaryTree *binaryTree, struct Node *node) {
	if (node != binaryTree->nil) {
		recursive_inorder_tree_walk(binaryTree, node->left);
		printf("%d ", node->key);
		recursive_inorder_tree_walk(binaryTree, node->right);
	}
};

struct Node *right_most_until(struct BinaryTree *binaryTree, struct Node *start, struct Node *until) {	
	struct Node *current = start;
	while (current->right != binaryTree->nil && current->right != until) {
		current = current->right;
	}
	return current;
}

void iterative_inorder_tree_walk(struct BinaryTree *binaryTree, struct Node *start) {
	struct Node *current = start;
	struct Node *left_right_most = binaryTree->nil;
	
	while (current != binaryTree->nil) {
		if (current->left == binaryTree->nil) {
			printf("%d ", current->key);
			current = current->right; 
		} else {
			left_right_most = right_most_until(binaryTree, current->left, current);
			if (left_right_most->right == current) {
				printf("%d ", current->key);
				left_right_most->right = binaryTree->nil;
				current = current->right;
			} else {
				left_right_most->right = current;
				current = current->left;
			}
		}
	}
};

struct Node *recursive_search(struct BinaryTree *binaryTree, struct Node *node, int key) {
	if (node == binaryTree->nil || key == node->key) {
		return node;
	} else if (key < node->key) {
		return recursive_search(binaryTree, node->left, key);
	} else {
		return recursive_search(binaryTree, node->right, key);
	}
}

struct Node *iterative_search(struct BinaryTree *binaryTree, struct Node *start, int key) {
	struct Node *current = start;
	while (current != binaryTree->nil) {
		if (key == current->key) {
			return current;
		} else if (key < current->key) {
			current = current->left;
		} else {
			current = current->right;
		}
	}
	return binaryTree->nil;
}

struct Node *minimum(struct BinaryTree *binaryTree, struct Node *node) {
	while (node->left != binaryTree->nil) {
		node = node->left;
	}
	return node;
}

struct Node *maximum(struct BinaryTree *binaryTree, struct Node *node) {
	while (node->right != binaryTree->nil) {
		node = node->right;
	}
	return node;
}

struct Node *successor(struct BinaryTree *binaryTree, struct Node *target) {
	if (target->right != binaryTree->nil) {
		return left_most(binaryTree, target->right);
	}
	
	struct Node* pre;
	do {
		pre = target;
		target = target->parent;
	} while (target != binaryTree->nil && target->left != pre);
	return target;
}

struct Node *predecessor(struct BinaryTree *binaryTree, struct Node *target) {
	if (target->left != binaryTree->nil) {
		return right_most(binaryTree, target->left);
	}
	
	struct Node* pre;
	do {
		pre = target;
		target = target->parent;
	} while (target != binaryTree->nil && target->right != pre);
	return target;
}

void transplant(struct BinaryTree *binaryTree, struct Node *replacement, struct Node *replaced) {
	if (replaced->parent == binaryTree->nil) {
		binaryTree->root = replacement;
	} else if (replaced->parent->left == replaced) {
		replaced->parent->left = replacement;
	} else {
		replaced->parent->right = replacement;
	}
	if (replacement != binaryTree->nil) {
		replacement->parent = replaced->parent;
	}
}

void deletion(struct BinaryTree *binaryTree, struct Node *target) {
	if (target->left == binaryTree->nil) {
		// no left child
		transplant(binaryTree, target->right, target);
	} else if (target->right == binaryTree->nil) {
		// only left child
		transplant(binaryTree, target->left, target);
	} else {
		// two children
		struct Node* target_successor = successor(binaryTree, target);
		if (target_successor->parent != target) {
			transplant(binaryTree, target_successor->right, target_successor);
			target_successor->right = target->right;
			target_successor->right->parent = target_successor;
		}
		target_successor->left = target->left;
		target_successor->left->parent = target_successor;
		transplant(binaryTree, target_successor, target);
	}
	free(target);
}