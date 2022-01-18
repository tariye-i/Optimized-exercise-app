class userhealth:

    def __init__(self,height,weight,gweight,workout):
        self.height = height
        self.weight = weight
        self.gweight = gweight
        self.workout = workout
    def __str__(self) -> str:
        print ("my weight is", self.weight)
        print ("my height is", self.height)
        

