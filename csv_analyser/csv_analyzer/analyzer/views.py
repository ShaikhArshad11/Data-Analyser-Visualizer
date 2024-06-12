from django.shortcuts import render
from django.shortcuts import render
from .forms import CSVUploadForm
from .models import CSVFile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            CSVFile.objects.create(file=csv_file)
            return render(request, 'analyzer/upload_success.html')
    else:
        form = CSVUploadForm()
    return render(request, 'analyzer/upload.html', {'form': form})


def process_csv(request):
    csv_file = CSVFile.objects.latest('id')
    df = pd.read_csv(csv_file.file.path)
    
    # Display the first few rows of the data
    head = df.head().to_html()
    
    # Calculate summary statistics
    summary_stats = df.describe().to_html()
    
    # Identify and handle missing values
    missing_values = df.isnull().sum().to_html()
    
    return render(request, 'analyzer/results.html', {
        'head': head,
        'summary_stats': summary_stats,
        'missing_values': missing_values,
    })