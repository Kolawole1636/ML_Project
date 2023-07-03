from django.shortcuts import render
from joblib import load

# Create your views here.

def diabetes_home(request):

    
    if request.method=="POST":
        pregnancy = request.POST["pregnancy"]
        glucose = request.POST["glucose"]
        bp = request.POST["bp"]
        skin = request.POST["skin"]
        insulin = request.POST["insulin"]
        bmi = request.POST["bmi"]
        dpf = request.POST["dpf"]
        age = request.POST["age"]

        rfc = load("final_diabetes_model")
        pred = rfc.predict([[pregnancy,glucose,bp,skin,insulin,bmi,dpf,age]])

        if pred[0] ==1:
            res = "The person has diabetes "
        else:
            res = "The person has no diabetes "

        
        return render(request,"home.html",{"result":res})




    return render(request,"home.html")
