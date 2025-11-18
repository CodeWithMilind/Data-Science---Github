from django import forms

class HouseInputForm(forms.Form):
    OverallQual = forms.IntegerField(label="Overall Quality (1-10)")
    GrLivArea = forms.IntegerField(label="Living Area (sqft)")
    GarageCars = forms.IntegerField(label="Garage Capacity (cars)")
    TotalBsmtSF = forms.IntegerField(label="Basement Area (sqft)")
    FullBath = forms.IntegerField(label="Full Bathrooms")
    YearBuilt = forms.IntegerField(label="Year Built")
