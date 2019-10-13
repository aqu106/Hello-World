# This comment has been made in the branch "aNewBranchInUbuntu"
import os
import time
PID = os.fork()
if PID == 0 :
	time.sleep(30)
	print("Aquib")
elif PID > 0 :
	print("Nazri")
	time.sleep(20)
	print("Aquib Nazri")
