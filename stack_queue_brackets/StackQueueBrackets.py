from stack_queue_brackets.StackAndQueue import Queue , Stack
def validateBrackets(str):
    stack1 = Stack()
    queue2 = Stack()
    stack3 = Stack()
    for i in str:
        if i == '{' or i == '(' or i == '[':
            stack1.push(i)
            # print('here'+ stack1.top.value)
        elif i == '}' or i == ')' or i == ']':
            queue2.push(i)
            # print('there'+stack3.top.value)
    # for i in range(stack3.size):
    #     queue2.push(stack3.pop())

    for _ in range(stack1.size):
        if stack1.size != queue2.size:
            return False
        if stack1.top.value == '{':
            if queue2.top.value=='}':
                stack1.pop()
                queue2.pop()
            else:
                return False
        elif stack1.top.value == '(':
            if queue2.top.value==')':
                stack1.pop()
                queue2.pop()
            else:
                return False    
        elif stack1.top.value == '[':
            if queue2.top.value==']':
                stack1.pop()
                queue2.pop()
            else:
                return False
    return True
        
    # check = False
    # brackets_Queue = Queue()
    
    # for i in str:
    #     brackets_Queue.enqueue(i)
    # new_front = brackets_Queue.front
    # new_front.next =None
    # brackets_Queue.front= brackets_Queue.rear.next
    # while brackets_Queue.front != None:
    #     if brackets_Queue.rear == "{":
    #         while brackets_Queue.front != None:
    #             if brackets_Queue.front=='}':
                    
    #                 brackets_Queue.rear = brackets_Queue.front.next
    #                 brackets_Queue.front= brackets_Queue.rear.next
    #             else:
    #                 check = False
    #                 brackets_Queue.front= brackets_Queue.front.next
    #         if not check:
    #             return False
    #     elif brackets_Queue.rear == "(":
    #         while brackets_Queue.front != None:
    #             if brackets_Queue.front==')':
    #                 check = True
    #                 brackets_Queue.rear = brackets_Queue.front.next
    #                 brackets_Queue.front= brackets_Queue.rear.next
    #             else:
    #                 check = False
    #                 brackets_Queue.front= brackets_Queue.front.next
    #         if not check:
    #             return False
    #     elif brackets_Queue.rear == "[":
    #         while brackets_Queue.front != None:
    #             if brackets_Queue.front==']':
    #                 check = True
    #                 brackets_Queue.rear = brackets_Queue.front.next
    #                 brackets_Queue.front= brackets_Queue.rear.next
    #             else:
    #                 check = False
    #                 brackets_Queue.front= brackets_Queue.front.next
    #         if not check:
    #             return False
    #     else:
    #         brackets_Queue.rear = brackets_Queue.rear.next
    #         brackets_Queue.front = brackets_Queue.front.next
    # return check

print(validateBrackets("{}"))
print(validateBrackets("{}(){}"))
print(validateBrackets("()[[Extra Characters]]"))
print(validateBrackets("(){}[[]]"))
print(validateBrackets("{}{Code}[Fellows](())"))
print(validateBrackets("[({})]"))
print(validateBrackets("(]("))
print(validateBrackets("{(})"))


