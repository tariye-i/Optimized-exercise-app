import healthclass
user_health = []
def create_health_data():
    print ("Please input height in centimeters")
    height = input()
    print ("please input weight in kg")
    weight = input()
    print ("please input goal weight")
    gweight = input()
    print ("please pick your preferred workout type from the list below")
    print ("Cardio\nAerobics\nYoga\nHIIT")
    workout = input()
    newuserhealth = healthclass.userhealth(height,weight,gweight,workout)
    user_health.append(newuserhealth)
    append_to_health_database(newuserhealth)
    append_all_info(newuserhealth)
    return newuserhealth

def append_to_health_database(object):
    write = open("health_database.txt","a")
    write.write(object.height)
    write.write("\n")
    write.write(object.weight)
    write.write("\n")
    write.close()

def append_all_info(object):
    write = open("full_health_database.txt","a")
    write.write("New health \n")
    write.write(object.height)
    write.write("\n")
    write.write(object.weight)
    write.write("\n")
    write.write(object.gweight)
    write.write("\n")
    write.write(object.workout)
    write.write("\n")
    write.close()
