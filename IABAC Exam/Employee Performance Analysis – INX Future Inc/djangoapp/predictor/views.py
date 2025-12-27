import os
import pickle
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from .forms import EmployeePerformanceForm

# Define model path
# The task specifies the new model file: models/employee_performance_rf_pipeline.pkl
# This is relative to src/
MODEL_PATH = settings.BASE_DIR.parent / 'src' / 'models' / 'employee_performance_rf_pipeline.pkl'

def load_model():
    """
    Load the pickle model from the specified path.
    If the file does not exist, return None.
    """
    try:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        return None
    except Exception as e:
        # In a real app, logging would be better
        print(f"Error loading model: {e}")
        return None

# Load model once at startup
MODEL = load_model()

def predict_performance(request):
    result = None
    if request.method == 'POST':
        print("DEBUG: POST request received")
        form = EmployeePerformanceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(f"DEBUG: Cleaned data: {data}")
            
            # Helper to convert input to correct type
            def get_val(key, type_func=int):
                return type_func(data[key])

            # Prepare input vector for the LITE model
            # ORDER: 
            # 1. Age
            # 2. DistanceFromHome
            # 3. EmpEnvironmentSatisfaction
            # 4. EmpJobSatisfaction
            # 5. EmpJobInvolvement
            # 6. EmpLastSalaryHikePercent
            # 7. TrainingTimesLastYear
            # 8. OverTime
            
            input_features = [
                get_val('Age'),
                get_val('DistanceFromHome'),
                get_val('EmpEnvironmentSatisfaction'),
                get_val('EmpJobSatisfaction'),
                get_val('EmpJobInvolvement'),
                get_val('EmpLastSalaryHikePercent', float),
                get_val('TrainingTimesLastYear'),
                get_val('OverTime') # Already mapped to 0 (Yes) or 1 (No) in forms.py
            ]
            
            if MODEL:
                try:
                    # Predict expects a 2D array
                    prediction = MODEL.predict([input_features])[0]
                    result = prediction
                    print(f"DEBUG: Prediction result: {result}")
                    return render(request, 'predictor/result.html', {'result': result})
                except Exception as e:
                    result = f"Error during prediction: {str(e)}"
                    print(f"DEBUG: {result}")
                    return render(request, 'predictor/index.html', {'form': form, 'result': result})
            else:
                result = f"Error: Model file not found at {MODEL_PATH}. Please ensure the model exists."
                print(f"DEBUG: {result}")
                return render(request, 'predictor/index.html', {'form': form, 'result': result})
        else:
            print(f"DEBUG: Form errors: {form.errors}")
    else:
        form = EmployeePerformanceForm()

    return render(request, 'predictor/index.html', {'form': form, 'result': result})
