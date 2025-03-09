/*
How do I build a Stack with C++
1. Push
2. Pop
3. is full
4. is empty
5. top
6. peek
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100
#define MAX_STRING 100

typedef struct {
    int student_no;
    char name[MAX_STRING];
    char address[MAX_STRING];
} element;
 
element stack[MAX_STACK_SIZE];
int top = -1;

int is_empty() {
    if (top == -1) {
        return 1;
    }
}
int is_full() {
    if (top == MAX_STACK_SIZE) {
        return 1;
    }
}

void push(element n) {
    if (is_full() == 1) {
        return;
    }
    top++;
    stack[top] = n;
}

element pop() {
    if (is_empty() == 1) {
        return;
    }
    element n;
    n = stack[top];
    top--;
    return n;
}
element peek() {
    if (is_empty() == 1) {
        return;
    }

    element n;
    n = stack[top];
    return n;
}
