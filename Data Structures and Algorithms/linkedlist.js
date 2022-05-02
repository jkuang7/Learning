//LinkedList
class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    //Insertion, Deletion, and Searching
    //Searching O(n)
    search(value) {
        let current = this.head;
        while (current !== null) {
            if (current.value === value) return current;
            current = current.next;
        }
        return null;
    }

    //Insertion -- addLast, addFirst, addAt -- 1, 1, n
    addLast(value) {
        const newNode = new Node(value);
        if (this.size === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.size++;
    }

    addFirst(value) {
        const newNode = new Node(value);
        if (this.size === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.size++;
    }

    addAt(index, value) {
        /*
          - index w/n bounds [0, size]
          - index is 0 -> deal with head case (and tail case if necessary)
          - if index is gt 0 
            find node at index - 1
            deal with tail case if necessary
            current.next = node;
            node = current.next.next;
        */
        const node = new Node(value);
        if (index < 0 && index > this.size) return;
        if (index === 0) {
            node.next = this.head;
            if (this.tail === this.head) {
                this.tail = node;
            }
            this.head = node;
        } else {
            let currentIdx = 0;
            let current = this.head;
            while (currentIdx !== index - 1) {
                currentIdx++;
                current = current.next;
            }
            if (current.next === this.tail) this.tail = node;

            node.next = current.next;
            current.next = node;
        }

        this.size++;
    }

    //Deletion -- deleteFirst, deleteLast, deleteAt -- 1, 1, n
    deleteFirst() {
        if (this.size === 0) return;
        if (this.size === 1) {
            this.head = this.tail = 0;
        } else {
            this.head = this.head.next;
        }
        this.size--;
    }

    deleteLast() {
        if (this.size === 0) return;
        if (this.size === 1) {
            this.head = this.tail = null;
        } else {
            let current = this.head;
            while (current !== null) {
                if (current.next === this.tail) {
                    this.tail = current;
                    this.tail.next = null;
                }
                current = current.next;
            }
        }
        this.size--;
    }

    deleteAt(index) {
        /*
          1 -> 2 -> null size: 2
          - outOfBound [0, size)
          - size is 0
            return
          - size is 1
            head = tail = null
          - size > 1
            - if index is at 0 -> shift head
            - else
              - find node before index - 1
              - shift tail if necessary
            - delete at the idx
              - current = current.next.next
          - decrement size
        */

        if (index < 0 || index >= this.size || this.size === 0) return;
        if (this.size === 1) {
            this.head = this.tail = null;
        } else {
            if (index === 0) {
                this.head = this.head.next;
            } else {
                let current = this.head,
                    currentIdx = 0;
                while (currentIdx !== index - 1) {
                    current = current.next;
                    currentIdx++;
                }
                if (current.next === this.tail) {
                    this.tail = current;
                }
                current.next = current.next.next;
                current = current.next;
            }
            this.size--;
        }
    }

    print() {
        //O(n)
        let current = this.head,
            linkedList = '';
        while (current !== null) {
            linkedList += current.value + ' -> ';
            current = current.next;
        }
        linkedList += 'null';
        console.log(linkedList);
        return linkedList;
    }
}

//search, addLast, addFirst, addAt, deleteLast, deleteFirst, deleteAt
const newLL = new SinglyLinkedList();
newLL.addLast(1);
newLL.addLast(2);
newLL.addLast(3);
newLL.addLast(4);
newLL.print();

newLL.addFirst(0);
newLL.print();

newLL.deleteAt(1);
newLL.print();

newLL.addAt(1, 1);
newLL.print();

newLL.deleteLast();
newLL.print();

newLL.deleteFirst();
newLL.print();

newLL.deleteAt(1);
newLL.print();