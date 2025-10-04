import pr1.Employee,pickle
fileobj=open("empdata.txt","wb")
empobj=Employee.employee(12,"rahul",2.0)
pickle.dump(empobj,fileobj)
fileobj.close()

