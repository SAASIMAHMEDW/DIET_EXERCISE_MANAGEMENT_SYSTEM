
import datetime

def getTime():
	current_time = datetime.datetime.now()
	#print(current_time)
	date_mon_year = current_time.strftime("| %d-%-m-%Y ]")
	#print(date_mon_year)

	formated_current_time = current_time.strftime("[ %I:%-M:%-S |")
	#print (formated_current_time)

	finalDateTime = formated_current_time + date_mon_year
	#print(finalDateTime)
	return finalDateTime

if __name__ == "__main__":
	x = getTime()
	print(x)