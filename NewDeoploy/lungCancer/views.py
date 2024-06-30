from django.shortcuts import render
from joblib import load
model=load("./Saving/modelz")
def predictor(request):
    return render(request,"indexx.html")

def formInfo(request):
    a=int(request.GET["age"])
    b=int(request.GET["sex"])
    c=int(request.GET["chest_pain"])
    d=int(request.GET["bp"])
    e=int(request.GET["choresterol"])
    f=int(request.GET["fbp"])
    g=int(request.GET["electrograph"])
    h=int(request.GET["max"])
    ab=int(request.GET["angina"])
    j=int(request.GET["oldpeak"])
    k=int(request.GET["slope"])
    l=int(request.GET["vessels"])
    m=int(request.GET["thal"])
    
    
    kk=model.predict([[a,b,c,d,e,f,g,h,ab,j,k,l,m]])
    
    if kk[0]==0:
        kk="Have the disease"
    else :
        kk= "Have the Disease"
    return render(request,"resultss.html",{"result":kk})

