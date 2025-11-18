from django.shortcuts import render
from .forms import HouseInputForm
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

def home(request):
    if request.method == "POST":
        form = HouseInputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            X = np.array([[
                data["OverallQual"],
                data["GrLivArea"],
                data["GarageCars"],
                data["TotalBsmtSF"],
                data["FullBath"],
                data["YearBuilt"]
            ]])
            pred = model.predict(X)[0]
            return render(request, "result.html", {"prediction": round(pred, 2)})
    else:
        form = HouseInputForm()
    return render(request, "index.html", {"form": form})
