def score(x):
    if(x >= 0):
        if(x < 12):
            print("مشروط")
        elif(x < 17):
            print("عادی")
        elif(x <= 20):
            print("ممتاز")
        else:
            print("لطفا نمره کمتر از 20 وارد شود")
    else:
        print("لطفا نمره بزرگتر مساوی عدد 0 بااشد")
        
score(19)

input()