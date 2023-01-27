from getCurrentTime import getTime
from time import sleep
"""
name = JASMINE AHMED
name = HANNAH BAKER
name = ALBA FLORES
name = SALMA HAYEK
"""
nameList = ["JASMINE AHMED", "HANNAH BAKER", "ALBA FLORES", "SALMA HAYEK"]
#print(nameList)

#dataLog function
def dataLog():
	print("\nWHOSE DATA WANNA LOG")
	print(
	 "1 FOR JASMINE AHMED\n2 FOR HANNAH BAKER\n3 FOR ALBA FLORE'S\n4 FOR SALMA HAYEK"
	)
	nameChoice = int(input("ENTER YOUR CHOICE: "))
	if nameChoice == 1:
		print("\nJASMINE AHMED")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		jFoodExerciseChoice = int(input("ENTER YOUR CHOICE: "))
		if jFoodExerciseChoice == 1:
			print("\nENTER YOUR FOOD")
			jFoodData = input("=>").title()
			fTime = getTime()
			with open("NAMES//JASMINE//jFood.txt", "a") as jFood:
				jFood.write("\n" + fTime + "\n")
				jFood.write(jFoodData + "\n")
		elif jFoodExerciseChoice == 2:
			print("\nENTER YOUR EXERCISE")
			jExerciseData = input("=>").title()
			eTime = getTime()
			with open("NAMES//JASMINE//jExercise.txt", "a") as jExercise:
				jExercise.write("\n" + eTime + "\n")
				jExercise.write(jExerciseData + "\n")
		else:
			print("\nINVALID INPUT!!!")
	elif nameChoice == 2:
		print("\nHANNAH BAKER")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		hFoodExerciseChoice = int(input("ENTER YOUR CHOICE: "))
		if hFoodExerciseChoice == 1:
			print("\nENTER YOUR FOOD: ")
			hFoodData = input("=>").title()
			fTime = getTime()
			with open("NAMES//HANNAH//hFood.txt", "a") as hFood:
				hFood.write("\n" + fTime + "\n")
				hFood.write(hFoodData + "\n")
		elif hFoodExerciseChoice == 2:
			print("\nENTER YOUR EXERCISE: ")
			hExercieeData = input("=>").title()
			eTime = getTime()
			with open("NAMES//HANNAH//hExercise.txt", "a") as hExercise:
				hExercise.write("\n" + eTime + "\n")
				hExercise.write(hExercieeData + "\n")
		else:
			print("\nINVALID INPUT!!!")

	elif nameChoice == 3:
		print("\nALBA FLORE'S")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		afFoodExerciseChoice = int(input("ENTER YOUR CHOICE: "))
		if afFoodExerciseChoice == 1:
			print("\nENTER YOUR FOOD: ")
			afFoodData = input("=>").title()
			fTime = getTime()
			with open("NAMES//ALBA//aFood.txt", "a") as afFood:
				afFood.write("\n" + fTime + "\n")
				afFood.write(afFoodData + "\n")
		elif afFoodExerciseChoice == 2:
			print("\nENTER YOUR EXERCISE: ")
			afExerciseData = input("=>").title()
			eTime = getTime()
			with open("NAMES//ALBA//aExercise.txt", "a") as afExercise:
				afExercise.write("\n" + eTime + "\n")
				afExercise.write(afExerciseData + "\n")
		else:
			print("\nINVALID INPUT")
	elif nameChoice == 4:
		print("\nSALMA HAYEK")
		print("WHAT DO YOU WANNA LOG\n1 FOR FOOD\n2 FOR EXERCISE")
		shFoodExerciseChoice = int(input("ENTER YOUR CHOICE: "))
		if shFoodExerciseChoice == 1:
			print("\nENTER YOUR FOOD: ")
			shFoodData = input("=>").title()
			fTime = getTime()
			with open("NAMES//SALMA//sFood.txt", "a") as shFood:
				shFood.write("\n" + fTime + "\n")
				shFood.write(shFoodData + "\n")
		elif shFoodExerciseChoice == 2:
			print("\nENTER YOUR EXERCISE: ")
			shExerciseData = input("=>").title()
			eTime = getTime()
			with open("NAMES//SALMA//sExercise.txt", "a") as shExercise:
				shExercise.write("\n" + eTime + "\n")
				shExercise.write(shExerciseData + "\n")
		else:
			print("\nINVALID INPUT!!!")

#dataRetrieve
def dataFetch():
	print("\nWHOSE DATA DO YOU WANNA RETRIEVE/FETCH\n1 FOR JASMINE AHMED\n2 FOR HANNAH BAKER\n3 FOR ALBA FLORES\n4 FOR SALMA HAYEK")
	nameChoice = int(input("ENTER YOUR CHOICE: "))
	if nameChoice == 1:
		print("\nJASMINE AHMED")
		print("WHAT DO YOU WANNA FETCH\n1 FOR JASMINE'S FOOD DATA\n2 FOR JASMINE'S EXERCISE DATA")
		jFoodExerciseDataFetchChoice = int(input("ENTER YOUR CHOICE: "))
		if jFoodExerciseDataFetchChoice==1:
			print ("\nFETCHING JASMINE'S FOOD DATA...")
			sleep(3)
			with open("NAMES//JASMINE//jFood.txt","rt") as jFoodDataF:
				foodData = jFoodDataF.read()
				print(foodData)
		elif jFoodExerciseDataFetchChoice==2:
			print("\nFETCHING JASMINE'S EXERCISE DATA...")
			sleep(3)
			with open("NAMES//JASMINE//jExercise.txt","rt") as jExerciseDataF:
				exerciseData = jExerciseDataF.read()
				print(exerciseData)
		else:
			print("INVALID INPUT!!!")
	elif nameChoice==2:
		print("\nHANNAH BAKER")
		print("WHAT DO YOU WANNA FETCH\n1 FOR HANNAH'S FOOD DATA\n2 FOR HANNAH'S EXERCISE DATA")
		hFoodExerciseDataFetchChoice=int(input("ENTER YOUR CHOICE: "))
		if hFoodExerciseDataFetchChoice ==1:
			print("\nFETCHING HANNAH'S FOOD DATA...")
			sleep(3)
			with open("NAMES//HANNAH//hFood.txt","rt") as hFoodDataF:
				foodData=hFoodDataF.read()
				print(foodData)
		elif hFoodExerciseDataFetchChoice==2:
			print("\nFETCHING HANNAH'S EXERCISE DATA...")
			sleep(3)
			with open("NAMES//HANNAH//hExercise.txt","rt") as hExerciseDataF:
				exerciseData = hExerciseDataF.read()
				print (exerciseData)
		else:
			print("\nINVALID INPUT!!!")
	elif nameChoice==3:
		print ("\nALBA FLORE'S")
		print("WHAT DO YOU WANNA FETCH\n1 FOR ALBA'S FOOD DATA\n2 FOR ALBA'S EXERCISE DATA")
		aFoodExerciseDataFetchChoice=int(input("ENTER YOUR CHOICE: "))
		if aFoodExerciseDataFetchChoice==1:
			print("\nFETCHING ALBA'S FOOD DATA...")
			sleep(3)
			with open("NAMES//ALBA//aFood.txt","rt") as aFoodDataF:
				foodData=aFoodDataF.read()
				print(foodData)
		elif aFoodExerciseDataFetchChoice==2:
			print("\nFETCHING ALBA'S EXERCISE DATA...")
			sleep(3)
			with open ("NAMES//ALBA//aExercise.txt","rt") as aExerciseDataF:
				exerciseData=aExerciseDataF.read()
				print(exerciseData)
		else:
			print("\nINVALID INPUT...")
	elif nameChoice==4:
		print("\nSALMA HAYEK")
		print("WHAT DO YOU WANNA FETCH\n1 FOR SALMA'S FOOD DATA\n2 FOR SALMA'S EXERCISE DATA")
		sFoodExerciseDataFetchChoice=int(input("ENTER YOUR CHOICE: "))
		if sFoodExerciseDataFetchChoice==1:
			print("\nFETCHING SALMA'S FOOD DATA")
			sleep(3)
			with open("NAMES//SALMA//sFood.txt","rt") as sFoodDataF:
				foodData=sFoodDataF.read()
				print (foodData)
		elif sFoodExerciseDataFetchChoice==2:
			print("\nFETCHING SALMA'S EXERCISE DATA")
			sleep(3)
			with open("NAMES//SALMA//sExercise.txt","rt") as sExerciseDataF:
				exerciseData=sExerciseDataF.read()
				print(exerciseData)
		else:
			print("\nINVALID INPUT!!!")



print("=" * 43)
print("DIET AND EXERCISE MANAGEMENT SYSTEM ".center(43))
print("×" * 43)
print("\nWHAT DO YOU WANNA DO?\n1 FOR LOG / 0 FOR RETRIEVE/FETCH\n")
try:
	userResponse = int(input("ENTER YOUR CHOICE: "))
except ValueError as VE:
	#print(VE)
	print(
	 "INVALID INPUT\nRE-RUN THE PROGRAM AND ENTER VALID INPUT\n1 FOR LOG\n0 FOR RETRIEVE/FETCH"
	)
else:
	if userResponse == 1:
		dataLog()
	elif userResponse == 0:
		dataFetch()
	else:
		print("WRONG PROMPT HAS BEEN ENTERED!!!\nPLEASE ENTER CORRECT PROMPT")
