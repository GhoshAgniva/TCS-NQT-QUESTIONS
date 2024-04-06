###An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:

###1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
###2nd data, Total number of wheels = W


v=int(input("Enter the number of two-wheelers and four-wheelers: "))
w=int(input("Enter the total number of wheels: "))
if w % 2 != 0 or v > w:
    print("Invalid Input")
else:
    FW=(w-(2*v))//2
    TW=(v-FW)
    print("TW=",TW,"FW=",FW)
    

