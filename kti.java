public class kti {

    // LinkedList implementation
    static class LinkedList {
        // Node class for linked list
        class Node {
            int data;
            Node next;

            Node(int data) {
                this.data = data;
                this.next = null;
            }
        }

        Node head = null;

        // Insert at the end
        public void insert(int data) {
            Node newNode = new Node(data);

            if (head == null) {
                head = newNode;
                return;
            }

            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }

        // Insert at the beginning
        public void insertAtBeginning(int data) {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
        }

        // Delete by value
        public void delete(int value) {
            if (head == null) {
                System.out.println("List is empty!");
                return;
            }

            if (head.data == value) {
                head = head.next;
                return;
            }

            Node temp = head;
            while (temp.next != null && temp.next.data != value) {
                temp = temp.next;
            }

            if (temp.next == null) {
                System.out.println("Value not found!");
            } else {
                temp.next = temp.next.next;
            }
        }

        // Search an element
        public boolean search(int value) {
            Node temp = head;
            while (temp != null) {
                if (temp.data == value) {
                    return true;
                }
                temp = temp.next;
            }
            return false;
        }

        // Display the linked list
        public void display() {
            if (head == null) {
                System.out.println("List is empty!");
                return;
            }

            Node temp = head;
            System.out.print("Linked List: ");
            while (temp != null) {
                System.out.print(temp.data + " -> ");
                temp = temp.next;
            }
            System.out.println("null");
        }
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.display();

        list.insertAtBeginning(5);
        list.display();

        list.delete(20);
        list.display();

        System.out.println("Searching 30: " + list.search(30));
        System.out.println("Searching 50: " + list.search(50));
    }
}
