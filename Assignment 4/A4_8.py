student_details = {101:'Judy', 102:'Victor', 103:'Sam'}
print ("original set:" + str(student_details))
replica = student_details.copy()
print("replica set:" + str(replica))

replica [103] = 'sally'
print("replica set after changing:" + str(replica))