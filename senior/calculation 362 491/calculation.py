def printE(left,right):
	for i in left:
		print(i,end="")
	print('=',end="")
	for i in right:
		print(i,end="")
	print("")
def addList(List):
	List+=')'
	List.insert(0,'(')
	List.insert(0,'sin^-1')
	return List
def AddMinus(List):
	List+=')'
	List.insert(0,'(')
	List.insert(0,'*')
	List.insert(0,')')
	List.insert(0,'1')
	List.insert(0,'-')
	List.insert(0,'(')
	return List

def AddDivision(List):
	List+=')'
	List+=')'
	List.insert(0,'(')
	List.insert(0,'/')
	List.insert(0,')')
	List.insert(0,'1')
	List.insert(0,'(')
	List.insert(0,'(')
	return List
def poly(equation):
	left=[]
	right=[]
	for i in equation:
		if(i=='='):
			right=equation[equation.index('=')+1:]
			break
		left+=[i]
	left+=['-']+['(']+right+[')']
	right=['0']
	return left+['=']+right


def SwapValue(equation,valueFind):
	#print("		",equation,valueFind)
	left=[]
	right=[]
	for i in equation:
		if(i=='='):
			right=equation[equation.index('=')+1:]
			break
		left+=[i]
	if(valueFind[0] in right):
		#print("asdadsad")
		i= right[:]
		right=left[:]
		left=i[:]


		
	Braces=0
	calleft=[]
	subleft=[]

	for i in left:
		if(i=='('):
			Braces+=1
		if(i==')'):
			Braces-=1

		subleft+=[i]
		if(Braces==0):
			calleft+=[subleft]
			subleft=[]
	countValueFind=0

	#---------------check poly
	for i in calleft:
		if(valueFind[0] in i):
			countValueFind+=1
	if(countValueFind>1):
		#call function poly  /// it may be poly
		return 'poly'
	if(len(calleft)==2):
		if(calleft[0]=='-'):
			right=AddMinus[right[:]]

	if(len(calleft)==3):
		#swap land
		if(valueFind[0] in calleft[2]):
			i=calleft[0][:]
			calleft[0]=calleft[2][:]
			calleft[2]=i[:]

			if(calleft[1][0]=='/'):
				right=AddDivision(right[:])
			if(calleft[1][0]=='-'):
				right=AddMinus[right[:]]
		left=calleft[0]
		right.insert(0,'(')
		right+=')'
	
		if(calleft[1][0]=='+'):
			right+='-'
		if(calleft[1][0]=='-'):
			right+='+'
		if(calleft[1][0]=='*'):
			right+='/'
		if(calleft[1][0]=='/'):
			right+='*'
		if(calleft[1][0]=='^'):
			right+='^'
			calleft[2]=AddDivision(calleft[2][:])
		right+=calleft[2]
		if(left[0]=='('):
			del left[0]
			del left[-1]

	#print(calleft)

	#print(left,right)
	#printE(left,right)

	return left+['=']+right


def changeEquation(equation,valueFind):
	if(valueFind[0] == 'theta' and (('sin' or 'cos') in equation)):
		triangle=True
		if( 'sin' in equation):
			del equation[equation.index('sin')]
		if( 'cos' in equation):
			del equation[equation.index('cos')]
	while(True):
		if(SwapValue(equation[:],valueFind[:])=='poly'):
			equation=poly(equation)
			break
	
		equation=SwapValue(equation[:],valueFind[:])
		#printE(equation,[])

		left=[]
		right=[]
		for i in equation:
			if(i=='='):
				right=equation[equation.index('=')+1:]
				break
			left+=[i]
		printE(left,right)

		if(len(left)==1):
			break
	try:
		triangle
	except NameError:
		pass
	else:
		left=[]
		right=[]
		for i in equation:
			if(i=='='):
				right=equation[equation.index('=')+1:]
				break
			left+=[i]
		right=addList(right)
		return left+['=']+right
	return equation


f=open('equation')
f=f.read().split('\n')
for i in range(len(f)):
	f[i]=f[i].split()
#print(f[4])
#equation = [['F', 'm', 'omega', 'r'], ['vav', 'omega', 'r']]
#valueDefine=['s','omega','r']
valueFind=['theta']

#printE(f[4],[])

print(changeEquation(f[11][:],valueFind[:]))