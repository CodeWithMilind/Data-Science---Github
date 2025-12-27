from django import forms

class EmployeePerformanceForm(forms.Form):
    # 1. Age
    Age = forms.IntegerField(
        label='Age', 
        min_value=18, 
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 30'})
    )
    
    # 2. DistanceFromHome
    DistanceFromHome = forms.IntegerField(
        label='Distance From Home (km)', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10'})
    )
    
    # 3. EmpEnvironmentSatisfaction
    EmpEnvironmentSatisfaction = forms.IntegerField(
        label='Environment Satisfaction (1-4)', 
        min_value=1, 
        max_value=4,
        help_text='1: Low, 4: High',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # 4. EmpJobSatisfaction
    EmpJobSatisfaction = forms.IntegerField(
        label='Job Satisfaction (1-4)', 
        min_value=1, 
        max_value=4,
        help_text='1: Low, 4: High',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # 5. EmpJobInvolvement
    EmpJobInvolvement = forms.IntegerField(
        label='Job Involvement (1-4)', 
        min_value=1, 
        max_value=4,
        help_text='1: Low, 4: High',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # 6. EmpLastSalaryHikePercent
    EmpLastSalaryHikePercent = forms.FloatField(
        label='Last Salary Hike Percent', 
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'e.g. 15.5'})
    )
    
    # 7. TrainingTimesLastYear
    TrainingTimesLastYear = forms.IntegerField(
        label='Training Times Last Year', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # 8. OverTime
    # Mapping based on previous analysis: No=1, Yes=0
    # However, for a generic form, we usually map Yes=1, No=0.
    # IMPORTANT: The prompt asks to use "employee_performance_rf_pipeline.pkl".
    # Without the model training code, we must rely on the previous encoding logic found in data_processing.ipynb:
    # data.OverTime = data.OverTime.map({'No':1,'Yes':0})
    OVERTIME_CHOICES = [
        (0, 'Yes'),
        (1, 'No')
    ]
    OverTime = forms.ChoiceField(
        choices=OVERTIME_CHOICES, 
        label='OverTime',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
