def isBalanced(expression) :
	#Your code goes here
	li=[]

	for e in expression:
		if e is "(":
			li.append(e)
		else:
			if  (not len(li)) or(li[len(li)-1]) is not "(":
				return False 
			else:
				li.pop()
	
	if (not len(li)):
		return True 
	else:
		return False


