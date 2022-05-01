class Stack {
  constructor() {
    this.stack = [];
  }

  //push, pop, peek, print -- 1, 1, 1, n
  print() {
    let string = "";
    for (const idx in this.stack) {
      string += ` ${this.stack[idx]} `;
    }
    console.log(string);
    return string;
  }

  push(val) {
    this.stack.push(val);
  }

  pop(val) {
    return this.stack.pop(val);
  }

  peek() {
    const top = this.stack[this.stack.length - 1];
    console.log(top);
    return top;
  }

  isEmpty() {
    return this.stack.length === 0;
  }
}

let stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.print();
stack.pop();
stack.print();
stack.peek();
console.log(stack.isEmpty());
