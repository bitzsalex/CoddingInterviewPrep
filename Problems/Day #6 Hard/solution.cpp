#include <iostream>
#include <stdint.h>

using namespace std;

class XORDoublyLinkedList {
    private:
        class Node {
            public:
                int data;
                Node *both = NULL;

                Node(int num) {
                    data = num;
                }
        };
        
        Node *head, * tail;


    public:
        XORDoublyLinkedList() {
            head = NULL;
            tail = NULL;
        }

        void add(int num) {
            Node *node = new Node(num);

            if (head == NULL && tail == NULL) {
                head = node;
                tail = node;
            } else {
                node->both = XORAddress(node->both, tail);
                tail->both = XORAddress(tail->both, node);
                tail = node;
            }
        }

        Node *get(int index) {
            Node *next_ptr = head;
            Node *prev_ptr = NULL;

            while (index != 0 && next_ptr != NULL) {
                Node *currentAddress = XORAddress(prev_ptr, next_ptr->both);
                prev_ptr = next_ptr;
                next_ptr = currentAddress;
                index--;
            }

            return index == 0 ? next_ptr : NULL;
        }

        void traverse(string direction="forward") {
            Node *next_ptr = direction == "forward" ? head : tail;
            Node *prev_ptr = NULL;

            while (next_ptr != NULL) {
                cout << next_ptr->data << " ";
                Node *currentAddress = XORAddress(prev_ptr, next_ptr->both);
                prev_ptr = next_ptr;
                next_ptr = currentAddress;
            }
            cout << endl;
        }

        Node *XORAddress(Node *ptr1, Node *ptr2) {
            return (Node *)((uintptr_t)ptr1 ^ (uintptr_t)ptr2);
        }
};


int main() {
    XORDoublyLinkedList list;
    list.add(10);
    list.add(100);
    list.add(1000);
    list.traverse();
    cout << list.get(0)->data << endl;
    return 0;
}