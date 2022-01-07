import healthclass
userhealth =[]
def create_health_data():
    print ("Please input height in centimeters")
    height = int(input())
    print ("please input weight in kg")
    weight = int(input())
    print ("please input goal weight")
    gweight = int(input())
    print ("please pick your preferred workout type from the list below")
    print ("Cardio\nStrength build\nBalance training\nEndurance\nFlexibility\nHIIT")
    workout = input()
    newuserhealth = healthclass.userhealth(height,weight,gweight,workout)
    userhealth.append(newuserhealth)
    append_to_health_database(newuserhealth)
    return newuserhealth

def append_to_health_database(object):
    write = open("health_database.txt","a")
    write.write (object.height)
    write.write("\n")
    write.write(object.weight)
    write.write("\n")
    write.write(object.gweight)
    write.write("\n")
    write.write(object.workout)
    write.write("\n")
    write.close()

