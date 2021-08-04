from django.http import HttpResponse
from django.shortcuts import render
import pandas
import os
from django.conf import settings



# Create your views here.

def index(request):

        #Data preprocessing

        fl1 = os.path.join(settings.BASE_DIR, 'assignment', 'resources', 'April-2021.xlsx')
        f1 = pandas.read_excel(fl1)
        new_header = f1.iloc[1]   #removing top two rows 
        f1 = f1[2:] 
        f1.columns = new_header
        
        fl2 = os.path.join(settings.BASE_DIR, 'assignment', 'resources', 'May-2021.xlsx')
        f2 = pandas.read_excel(fl2)
        new_header = f2.iloc[1] 
        f2 = f2[2:] 
        f2.columns = new_header

        fl3 = os.path.join(settings.BASE_DIR, 'assignment', 'resources', 'June-2021.xlsx')
        f3 = pandas.read_excel(fl3)
        new_header = f3.iloc[1] 
        f3 = f3[2:] 
        f3.columns = new_header

        f4 = pandas.merge(f1,f2,how='outer', on='Vehicle Class')  #merging the files together
        df1 = pandas.merge(f4,f3,how='outer', on='Vehicle Class')
        df1.drop(['Serial No','Serial No_y','Serial No_x'], axis=1,inplace=True)
        
        df1.fillna('', inplace=True) # replacing null values with an empty string
        #creating index columns
        df1.index+=1
        df1.reset_index(inplace=True)

        df1.rename(columns={'index':'Serial No',"Total_x": "April", "Total_y": "May",  "Total": "June"},inplace=True)
        lis1=[df1.columns.values.tolist()]
        lis =df1.values.tolist()
        output=df1.to_csv()

        if request.method == "POST":# clicked on download table
            response = HttpResponse(output,
            content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=%s.csv' % 'Data'
            return response
        return render(request,"assignment/index.html",{
            "heading":lis1,
            "excel_data":lis })




