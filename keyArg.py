def keyArgFunc(empname, emprole):   
   print ("Emp Name: ", empname)
   print ("Emp Role: ", emprole)
   return;   
print("Calling in proper sequence")
keyArgFunc(empname = "Nick",emprole = "Manager" )
print("Calling in opposite sequence")
keyArgFunc(emprole = "Manager",empname = "Nick")