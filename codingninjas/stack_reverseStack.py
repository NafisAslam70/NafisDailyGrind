def insertAtBottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insertAtBottom(stack, item)
    stack.append(top)

def reverseStack(inputStack, extraStack):
    if not inputStack:
        return
    top = inputStack.pop()
    reverseStack(inputStack, extraStack)
    insertAtBottom(inputStack, top)