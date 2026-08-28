def checkRedundantBrackets(expression) :
	# Your code goes here

	s=[]

	for e in expression:
		if e!=")":
			s.append(e)
		else:
			c=0
			while s[-1]!="(":
				s.pop()
				c+=1
			s.pop()
			if c<=1:
				return True 
	
	return False
