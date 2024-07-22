from django.shortcuts import render, redirect, get_object_or_404
from .models import person
from django.core.files.storage import FileSystemStorage
from .forms import UploadExcelForm
from django.conf import settings
import pandas as panda



def index(request):   
    data = person.objects.all()  # Fetch all person objects from database
    context = {
        'data': data  # Pass the queryset to the template context
    }
    return render(request, 'index.html',context)



def insertData(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        number = request.POST.get('number')
        address = request.POST.get('address')
        
        # Create and save person object
        new_person = person(name=name, age=age, number=number, address=address)
        new_person.save()

        return redirect('index')

    
    return render(request, 'index.html')

def updateData(request, id):
    obj = get_object_or_404(person, id=id)
    if request.method == "POST":
        obj.name = request.POST.get('name')
        obj.age = request.POST.get('age')
        obj.number = request.POST.get('number')
        obj.address = request.POST.get('address')
        obj.save()
        return redirect('index')
    
    return render(request, 'edit.html', {'person': obj})

def deleteData(request,id ):
    data = person.objects.get(id=id)  # Fetch all person objects from database
    data.delete()
    return redirect('index')

def process_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = panda.read_excel(excel_file, engine='openpyxl')  # Read Excel file into DataFrame
            
            # Process each row in DataFrame
            for index, row in df.iterrows():
                # Example: Save each row to database
                name = row['Name']
                age = row['Age']
                number = row['Number']
                address = row['Address']
                patient = person(name=name, age=age, number=number, address=address)
                patient.save()
            return render(request, 'process_success.html', {'num_rows': len(df)})
    else:
        form = UploadExcelForm()
    return render(request, 'upload_excel.html', {'form': form})