from django.shortcuts import render
from joblib import load



# Create your views here.



def index(request):

    if request.method=="POST":
        age = request.POST["age"]
        salary = request.POST["salary"]

        rfc = load("final_suv_model")
        pred = rfc.predict([[age,salary]])

        if pred[0] ==0:
            res = "The person will Not purchase SUV car "
        else:
            res = "The person will purchase SUV car "

        
        return render(request,"index.html",{"result":res})





    return render(request, "index.html")
