#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode {
    element data;
    struct ListNode *link;
} ListNode;

void error(char *message) {
    fprintf(stderr, "%s\n", message);
    exit(1);
}

ListNode* insert_first(ListNode *head, element value) {
    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p -> data = value;
    p -> link = head; // head는 링크 자체
    head = p;
    return head;
}

ListNode* insert(ListNode *head, ListNode *pre, element value) {
    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p -> data = value;
    p -> link = pre -> link;
    pre -> link = p;
    return head;
}

ListNode* delete_first(ListNode *head) {
    ListNode* removed;
    if(head == NULL) return NULL;
    removed = head;
    head = removed -> link;
    free(removed);
    return head;
}

ListNode* delete(ListNode *head, ListNode *pre) {
    ListNode* removed;
    if(head == NULL) return NULL;
    removed = pre -> link;
    free(removed);

    return head;
}

int main(void) {
    ListNode *head = NULL;

    for (int i = 0; i < 5; i++) {
        insert_first(head, i);
    }

    for(int i = 0; i < 5; i++) {
        delete_first(head);
    }
}