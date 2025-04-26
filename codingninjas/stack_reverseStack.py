def reverseStack(inputStack, extraStack) :
	#Your code goes here
    if len(inputStack)<=1:
        return

    while len(inputStack)!=1:
        el=inputStack.pop()
        extraStack.append(el)
    
    lastele=inputStack.pop()

    while len(extraStack)!=0:
        el=extraStack.pop()
        inputStack.append(el)
    
    reverseStack(inputStack,extraStack)
    inputStack.append(lastele)
