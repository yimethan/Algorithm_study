#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct TreeNode {
    element key;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode *search(TreeNode *node, element key) {
    if (node == NULL) {
        return NULL;
    } 
    if (node -> key == key) {
        return node;
    } else if (node -> key > key) {
        return search(node -> left, key);
    } else {
        return search(node -> right, key);
    }
}

TreeNode *new_node(element item) {
    TreeNode *temp = (TreeNode *)malloc(sizeof(TreeNode));
    temp -> key = item;
    temp -> left = temp -> right = NULL;

    return temp;
}

TreeNode *insert_node(TreeNode *node, element key) {
    if (node == NULL) {
        return new_node(key);
    }

    if (key < node->key) {
        node->left = insert_node(node->left, key);
    } else {
        node->right = insert_node(node->right, key);
    }

    return node;
}

TreeNode *min_value_node(TreeNode *node) {
    TreeNode *current = node;

    while (current->left != NULL) {
        current = current->left;
    }

    return current;
}

TreeNode *delete_node(TreeNode *root, element key) {
    if (root == NULL) {
        return root;
    }

    if (key < root -> key) {
        root->left = delete_node(root->left, key);
    } else if (key > root->key) {
        root->right = delete_node(root->right, key);
    } else {
        if (root->left == NULL) {
            TreeNode *temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            TreeNode *temp = root->left;
            free(root); 
            return temp;
        } else {
            TreeNode *temp = min_value_node(root->right);

            root->key = temp->key;
            root->right = delete_node(root->right, temp->key);
        }
    }
    return root;
}