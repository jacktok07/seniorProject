import math
def isNum(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
def calValue(equation,value,cost):
	Braces=0
	calE=[]
	subE=[]
	for i in equation:
		if(i=='('):
			Braces+=1
		if(i==')'):
			Braces-=1
		subE+=[i]
		if(Braces==0):
			calE+=[subE]
			subE=[]
	print(len(calE))
	print(calE)
	if(len(calE)==1):
		if('(' and ')' in calE[0]):
			del calE[0][0]
			print(calE[0])
			calE[0].pop()
			return calValue(calE[0][:],value[:],cost[:])
		if(isNum(calE[0][0])):
			return float(calE[0][0])
		return cost[value.index(calE[0][0])]
	if(len(calE)==2):
		print("calE2")
		if calE[0][0]=='-':
			return (-1*(calValue(calE[1][:],value[:],cost[:])))
		if calE[0][0]=='sin^-1':
			print("sin^-1")
			return math.asinh(calValue(calE[1][:],value[:],cost[:]))
	if(len(calE)==3):
		if calE[1][0]=='+':
			return calValue(calE[0][:],value[:],cost[:])+calValue(calE[2][:],value[:],cost[:])
		if calE[1][0]=='-':
			return calValue(calE[0][:],value[:],cost[:])-calValue(calE[2][:],value[:],cost[:])
		if calE[1][0]=='/':
			return calValue(calE[0][:],value[:],cost[:])/calValue(calE[2][:],value[:],cost[:])
		if calE[1][0]=='*':
			return calValue(calE[0][:],value[:],cost[:])*calValue(calE[2][:],value[:],cost[:])
		if calE[1][0]=='^':
			return math.pow(calValue(calE[0][:],value[:],cost[:]),calValue(calE[2][:],value[:],cost[:]))
	
	print("Bug dak")
x=['sin^-1', '(', '(', '(', '(', 'sy', ')', '*', 'a', ')', '^', '(', '(', '1', ')', '/', '(', '2', ')', ')', ')', '/', 'u', ')']
value=['sy','a','u']
cost=[90,10,30]
print(calValue(x[:],value[:],cost[:]))