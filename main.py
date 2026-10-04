str_total_seconds=input("please type the number of seconds :\n")
int_total_seconds=int (str_total_seconds)
int_Tminutes=int_total_seconds//60
int_seconds=int_total_seconds%60
int_hours=int_Tminutes//60
int_minutes=int_Tminutes%60
print("this corse is : "+str(int_hours)+" hours and "+str(int_minutes)+" minutes and "+str(int_seconds)+" seconds long")