//enqueue, dequeue, peek, print -- 1, 1, 1, n

class Node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.head = this.tail = null;
    this.length = 0;
    //head is front of queue
    //tail is end of queue
  }
  
  enqueue(val) {
    const node = new Node(val);
    if (this.length === 0) {
      this.head = this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.length++;
  }
  dequeue() {
    if (this.length === 0) return;
    if (this.length === 1) {
      this.head = this.tail = null;
    } else {
      this.head = this.head.next;
    }
    this.length--;
  }

  peek() {
    console.log(this.head.val);
    return this.head.val;
  }

  print() {
    let current = this.head,
      print = "";
    while (current !== null) {
      print += ` ${current.val} `;
      current = current.next;
    }
    console.log(print);
    return print;
  }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.enqueue(4);
queue.print();
queue.dequeue();
queue.print();
queue.peek();
