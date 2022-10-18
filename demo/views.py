from django.shortcuts import render
#import your model to be exported
from .models import Employee, ExcelFile
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
# Create your views here.

#create function to export database
def export_data_to_excel(request):
    objs = Employee.objects.all()

    #Sereslise the data
    data=[]

    for obj in objs:
        data.append({
            "employee_name" : obj.employee_name,
            "employee_contact" : obj.employee_contact,
            "employee_address" : obj.employee_address,
        })

    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status' : 200
    })

#creating function to import data from excel file database in django

def import_data_to_db(request):
    if request.method == 'Post':
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file = file
        )
        path = file.file
        print(f'{settings.BASE_DIR}+{Path}')
        df = pd.read_excel(path)
        for i in df.values:
            print (i)

    return render(request , 'excel.html')