str_total_seconds=input("please type the number of seconds : \n")
int_total_seconds=int(str_total_seconds)
int_Tminutes= int_total_seconds//60
print(f" this corse is : {int_Tminutes//60} hours and {int_Tminutes%60} minutes and {int_total_seconds%60} seconds long")