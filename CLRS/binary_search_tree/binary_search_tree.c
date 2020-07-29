#include <stdio.h>
#include <stdlib.h>
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

struct Node *right_most(struct Node *start) {	
	struct Node *current = start;
	while (current->right != NULL) {
		current = current->right;
	}
	return current;
}

struct Node *left_most(struct Node *start) {	
	struct Node *current = start;
	while (current->left != NULL) {
		current = current->left;
	}
	return current;
}

void recursive_inorder_tree_walk(struct Node *node) {
	if (node != NULL) {
		recursive_inorder_tree_walk(node->left);
		printf("%d ", node->key);
		recursive_inorder_tree_walk(node->right);
	}
};

struct Node *right_most_until(struct Node *start, struct Node *until) {	
	struct Node *current = start;
	while (current->right != NULL && current->right != until) {
		current = current->right;
	}
	return current;
}

void iterative_inorder_tree_walk(struct Node *start) {
	struct Node *current = start;
	struct Node *left_right_most = NULL;
	
	while (current != NULL) {
		if (current->left == NULL) {
			printf("%d ", current->key);
			current = current->right; 
		} else {
			left_right_most = right_most_until(current->left, current);
			if (left_right_most->right == current) {
				printf("%d ", current->key);
				left_right_most->right = NULL;
				current = current->right;
			} else {
				left_right_most->right = current;
				current = current->left;
			}
		}
	}
};

struct Node *recursive_search(struct Node *node, int key) {
	if (node == NULL || key == node->key) {
		return node;
	} else if (key < node->key) {
		return recursive_search(node->left, key);
	} else {
		return recursive_search(node->right, key);
	}
}

struct Node *iterative_search(struct Node *start, int key) {
	struct Node *current = start;
	while (current != NULL) {
		if (key == current->key) {
			return current;
		} else if (key < current->key) {
			current = current->left;
		} else {
			current = current->right;
		}
	}
	return NULL;
}

struct Node *minimum(struct Node *node) {
	while (node->left != NULL) {
		node = node->left;
	}
	return node;
}

struct Node *maximum(struct Node *node) {
	while (node->right != NULL) {
		node = node->right;
	}
	return node;
}

struct Node *successor(struct Node *target) {
	if (target->right != NULL) {
		return left_most(target->right);
	}
	
	struct Node* pre;
	do {
		pre = target;
		target = target->parent;
	} while (target != NULL && target->left != pre);
	return target;
}

struct Node *predecessor(struct Node *target) {
	if (target->left != NULL) {
		return right_most(target->left);
	}
	
	struct Node* pre;
	do {
		pre = target;
		target = target->parent;
	} while (target != NULL && target->right != pre);
	return target;
}

struct Node *transplant(struct Node *T, struct Node *replacement, struct Node *replaced) {
	if (replaced->parent == NULL) {
		T = replacement;
	} else if (replaced->parent->left == replaced) {
		replaced->parent->left = replacement;
	} else {
		replaced->parent->right = replacement;
	}
	if (replacement != NULL) {
		replacement->parent = replaced->parent;
	}
	return T;
}

struct Node *deletion(struct Node *T, struct Node *target) {
	if (target->left == NULL) {
		// no left child
		T = transplant(T, target->right, target);
	} else if (target->right == NULL) {
		// only left child
		T = transplant(T, target->left, target);
	} else {
		// two children
		struct Node* target_successor = successor(target);
		if (target_successor->parent != target) {
			T = transplant(T, target_successor->right, target_successor);
			target_successor->right = target->right;
			target_successor->right->parent = target_successor;
		}
		target_successor->left = target->left;
		target_successor->left->parent = target_successor;
		T = transplant(T, target_successor, target);
	}
	free(target);
	return T;
}