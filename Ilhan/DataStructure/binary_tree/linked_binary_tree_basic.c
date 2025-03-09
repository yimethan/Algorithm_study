#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode{
    int data;
    struct TreeNode *left, *right;
} TreeNode;

/*
    15
  4     20
1   16      25
*/

TreeNode n1 = {1, NULL, NULL};
TreeNode n2 = {16, NULL, NULL};
TreeNode n3 = {25, NULL, NULL};
TreeNode n4 = {4, &n1, &n2};
TreeNode n5 = {20, NULL, &n3};
TreeNode n6 = {15, &n4, &n5};
TreeNode *root = &n6;


//중위 선회 L V R
void inorder(TreeNode *root) {
    if (root != NULL) {
        inorder(root->left);
        printf("[%d] ", root->data);
        inorder(root->right);
    }
}

//전위 선회 V L R
void preorder(TreeNode *root) {
    if(root != NULL) {
        printf("[%d] ", root->data);
        inorder(root->left);
        inorder(root->right);
    }
}

//후위 선회 L R V
void postorder(TreeNode *root) {
    if(root != NULL) {
        inorder(root->left);
        inorder(root->right);
        printf("[%d] ", root->data);
    }
}

int main(void) {
    printf("---중위 순회---");
    inorder(root);

    printf("---전위 순회---");
    preorder(root);

    printf("---후위 순회---");
    postorder(root);

    return 0;
}