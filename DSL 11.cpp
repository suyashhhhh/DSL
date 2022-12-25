#include <iostream>
using namespace std;

class node
{
public:
    int data;
    node *next;

    // constructor
    node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
    ~node()
    {
        int value = this->data;
        // memory free
        if (this->next != NULL)
        {
            delete next;
            this->next = NULL;
        }
        cout << "the meomery is free for NODE the data: " << value << endl;
    }
};

void InsertHead(node *&head, int d)
{
    node *temp = new node(d);
    temp->next = head;
    head = temp;
}

void insertTail(node *&tail, int d)
{
    node *temp = new node(d);
    tail->next = temp;
    tail = temp;
}

void print(node *&head)
{

    node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void insertAtposition(node *&head, int position, int d)
{
    node *temp = head;
    int cnt = 1;

    while (cnt < position - 1)
    {
        temp = temp->next;
        cnt++;
    }
    node *nodetoinsert = new node(d);
    nodetoinsert->next = temp->next;
    temp->next = nodetoinsert;
}

void deletenode(int position, node *&head)
{

    if (position == 1)
    {

        node *temp = head;
        head = head->next;
        temp->next = NULL;
        delete temp;
    }
    else
    {
        node *current = head;
        node *previous = NULL;

        int cnt = 1;
        while (cnt <= position)
        {
            previous = current;
            current = current->next;
            cnt++;
        }
        previous->next = current->next;
        current->next = NULL;
        delete current;
    }
}

int main()
{
    // crerating the new node
    node *node1 = new node(4);
    // cout << node1->data << endl;
    // cout << node1->next << endl;

    // head pointed to node1
    node *head = node1;
    node *tail = node1;
    print(head);

    InsertHead(head, 12);
    print(head);

    InsertHead(head, 15);
    print(head);

    insertTail(tail, 5);
    print(head);

    insertTail(tail, 6);
    print(head);

    insertAtposition(head, 2, 11);
    print(head);

    deletenode(1, head);
    print(head);
    return 0;
}
