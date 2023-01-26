from getCurrentTime import getTime

"""
name = JASMINE AHMED
name = HANNAH BAKER
name = ALBA FLORES
name = SALMA HAYEK
"""
nameList = ["JASMINE AHMED","HANNAH BAKER","ALBA FLORES","SALMA HAYEK"]
#print(nameList)


def dataLog():
	print("\nWHOSE DATA WANNA LOG")
	print("1 FOR JASMINE AHMED\n2 FOR HANNAH BAKER\n3 FOR ALBA FLORE'S\n4 FOR SALMA HAYEK")
	nameChoice = int(input("ENTER YOUR CHOICE: "))
	if nameChoice == 1:
		print("\nJASMINE AHMED")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		jFoodExerciseChoice = int(input("ENTER YOUR CHOICE: "))
		if jFoodExerciseChoice == 1:
			print("\nENTER YOUR FOOD")
			jFoodData = input("=>").title()
			fTime = getTime()
			with open("NAMES//JASMINE//jFood.txt","a") as jFood:
				jFood.write("\n"+fTime+"\n")
				jFood.write(jFoodData+"\n")
		elif jFoodExerciseChoice == 2:
			print("ENTER YOUR EXERCISE")
			jExerciseData = input("=>").title()
			eTime = getTime()
			with open("NAMES//JASMINE//jExercise.txt","a") as jExercise:
				jExercise.write("\n"+eTime+"\n")
				jExercise.write(jExerciseData+"\n")
		else:
			print("INVALID INPUT!!!")
	elif nameChoice == 2:
		print("\nHANNAH BAKER")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		hFoodExerciseChoice = int(input("ENTER YOUR CHOICE: "))
		if hFoodExerciseChoice==1:
			print("\nENTER YOUR FOOD: ")
			hFoodData=input("=>").title()
			fTime = getTime()
			with open("NAMES//HANNAH//hFood.txt","a") as hFood:
				hFood.write("\n"+fTime+"\n")
				hFood.write(hFoodData+"\n")
		elif hFoodExerciseChoice==2:
			print("\nENTER YOUR EXERCISE: ")
			hExercieeData =input("=>").title()
			eTime = getTime()
			with open("NAMES//HANNAH//hExercise.txt","a") as hExercise:
				hExercise.write("\n"+eTime+"\n")
				hExercise.write(hExercieeData+"\n")
		else:
				print("\nINVALID INPUT!!!")
			
	elif nameChoice==3:
		print("\nALBA FLORE'S")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		afFoodExerciseChoice=int(input("ENTER YOUR CHOICE: "))
		if afFoodExerciseChoice==1:
			print("\nENTER YOUR FOOD: ")
			afFoodData = input("=>").title()
			fTime = getTime()
			with open("NAMES//ALBA//aFood.txt","a") as afFood:
				afFood.write("\n"+fTime+"\n")
				afFood.write(afFoodData+"\n")
		elif afFoodExerciseChoice==2:
			print("\nENTER YOUR EXERCISE: ")
			afExerciseData=input("=>").title()
			eTime = getTime()
			with open("NAMES//ALBA//aExercise.txt","a") as afExercise:
				afExercise.write("\n"+eTime+"\n")
				afExercise.write(afExerciseData+"\n")
		else:
			print("\nINVALID INPUT")
	elif nameChoice==4:
		print("\nSALMA HAYEK")
		print ("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		shFoodExerciseChoice=int(input("ENTER YOUR CHOICE: "))
		if shFoodExerciseChoice==1:
			print("\nENTER YOUR FOOD: ")
			shFoodData=input("=>").title()
			fTime = getTime()
			with open("NAMES//SALMA//sFood.txt","a") as shFood:
				shFood.write("\n"+fTime+"\n")
				shFood.write(shFoodData+"\n")
		elif shFoodExerciseChoice==2:
			print("\nENTER YOUR EXERCISE: ")
			shExerciseData=input("=>").title()
			eTime = getTime()
			with open("NAMES//SALMA//sExercise.txt","a") as shExercise:
				shExercise.write("\n"+eTime+"\n")
				shExercise.write(shExerciseData+"\n")
		else:
			print("\nINVALID INPUT!!!")


print("="*43)
print("DIET AND EXERCISE MANAGEMENT SYSTEM ".center(43))
print("×"*43)
print("\nWHAT DO YOU WANNA DO?\n1 FOR LOG / 0 FOR RETRIEVE\n")
try:
	userResponse=int(input("ENTER YOUR CHOICE: "))
except ValueError as VE:
	#print(VE)
	print("INVALID INPUT\nRE-RUN THE PROGRAM AND ENTER VALID INPUT\n1 FOR LOG\n0 FOR RETRIEVE")
else:
	if userResponse == 1:
		dataLog()
	elif userResponse == 0:
		pass
	else:
		print("WRONG PROMPT HAS BEEN ENTERED!!!\nPLEASE ENTER CORRECT PROMPT")
		
	
	
	