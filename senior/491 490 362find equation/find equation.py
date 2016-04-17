def find(equation,value,valueFind,valueMainFind,checkLoopInfinit):
	if(checkLoopInfinit==0):
		return False
	checkLoopInfinit-=1
	print("หา ",valueFind ," check : ",checkLoopInfinit)
	#print(equation)
	for i in range(len(equation)):
		if(valueFind in equation[i][0]):
			equation[i][2]=True
	for i in value:
		for j in range(len(equation)):
			if(equation[j][2] and i in equation[j][0]):
				equation[j][1]-=1
	#print(equation)
	for missing in range(1,5):
		for NumEquation in range(len(equation)):
			if(equation[NumEquation][2] and equation[NumEquation][1]==missing):
				print(equation[NumEquation])
				#print(equation)
				if(missing==1):
					return True
				else:
					status=1
					setValueFindNext=set(equation[NumEquation][0])
					setValueFindNext-=set(value)
					setValueFindNext-=set(valueFind)
					if(not(valueMainFind in setValueFindNext)):
						#print(setValueFindNext)
						a=list(setValueFindNext)
						if(find(resetZeroCountEquation(equation),value,a[0],valueMainFind,checkLoopInfinit)):
							return True
						'''
						for findValue in setValueFindNext:
							if(not find(resetZeroCountEquation(equation),value,findValue,valueMainFind,checkLoopInfinit)):#return false
								status=0
								break
						if(status==1):
							return True'''
		
	return False
	
def IOEquation():
	f=open('equation.cwt')
	return f.read().split()

def setEquation(equation):
	for i in range(len(equation)):
		equation[i]=[equation[i]]+[len(equation[i])]+[False]
	return equation

def resetZeroCountEquation(equation):
	for i in range(len(equation)):
		equation[i][1]=len(equation[i][0])
		equation[i][2]=False
	return equation


equationa=IOEquation()
equationa= setEquation(equationa)


print(find(equationa,'fmst','u','u',10))
