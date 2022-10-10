from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.utils.safestring import mark_safe
from algorithm.models import *
from django.core.exceptions import ValidationError

year_list=[
   #('2023-','First year'),
   ('2022-12-21','Second year'), 
   ('2023-01-07','Third year'),
   ('2022-12-23','Fourth year'),
]
class Newform(forms.Form):
   #branch=forms.CharField(label=mark_safe('<b>Branch'),widget=forms.Select(choices=branches))
   yr=forms.CharField(label=mark_safe("<b>Year of Study:"),widget=forms.Select(choices=year_list))
   #subject=forms.CharField(label=mark_safe("<b><br><br>Subject"))
   mon=forms.IntegerField(label=mark_safe("<br><br>As per timetable no of periods of a subject:<br>Monday:"),min_value=0,max_value=6,initial=0)
   tue=forms.IntegerField(label=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tuesday:"),min_value=0,max_value=6,initial=0)
   wed=forms.IntegerField(label=mark_safe("<br><br>Wednesday:"),min_value=0,max_value=6,initial=0)
   th=forms.IntegerField(label=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thursday:"),min_value=0,max_value=6,initial=0)
   fri=forms.IntegerField(label=mark_safe("<br><br>Friday:"),min_value=0,max_value=6,initial=0)
   att_no=forms.IntegerField(label=mark_safe("<b><br><br><u>Current attendance</u><br>No of classes attended till now"),min_value=0,max_value=200)
   tt_no=forms.IntegerField(label=mark_safe("<br><b>Total no of classes till now &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "),min_value=1,max_value=200)


def att_pred(request):
   # get_subjects =Attendance.objects.all()
   if request.method == "POST":
      form=Newform(request.POST)

      if form.is_valid():

         a=form.cleaned_data["att_no"]
         t=form.cleaned_data["tt_no"]
         mon=form.cleaned_data["mon"]
         tue=form.cleaned_data["tue"]
         wed=form.cleaned_data["wed"]
         th=form.cleaned_data["th"]
         fri=form.cleaned_data["fri"]
         yr=form.cleaned_data["yr"]
         if a>t:
            return HttpResponse('Oops....No of attended classes cannot be greater than total no classes.')



         from datetime import date
         import datetime
         import calendar
         from dateutil.rrule import rrule, DAILY
         import numpy as np

         ans=[]

         def weekday_count(start, end):

            leaves=["2022-10-24","2022-12-25"]
            l1 = [0, 0, 0, 0, 0]
            for dt in rrule(DAILY, dtstart=start, until=end):
               if bool(np.is_busday([dt.strftime("%Y-%m-%d")],
                                   holidays=leaves)):
                   l1[dt.weekday()] += 1
            return l1


         today = date.today()
         last=date(int(yr[0:4]),int(yr[5:7]),int(yr[8:10]))

         w_days=weekday_count(today,last)

         #get from html form period distribution,no of attended classes(a),total no of classes(t)
         periods=[mon,tue,wed,th,fri]
         at=a
         tt=t
         for i in range(5):
           a += periods[i]*w_days[i]
           t += periods[i]*w_days[i]
         ans=[]
         if (t-tt>13):
             y=13
         else:
             y=t-tt
         for i in range(y+1):
           ans.append(round((a/t)*100))
           a-=1

         return render(request,'algorithm/base2.html',{"form":form,"ans_m":round((ans[0])),"ans":ans })


      else:
         return render(request,'algorithm/base.html',{"form":form}) # 2 nd form is from line 26
                                                                     # it is a new form

   return render(request,'algorithm/base.html',{"form":Newform()}) 

















# branches=[
#    ('Computer Science','Computer Science'),
#    ('Computer Science:AI and Machine Learning','Computer Science:AI and Machine Learning'),
#    ('Electronics and Communication A','Electronics and Communication A'),
#    ('Electronics and Communication B','Electronics and Communication B'),
#    ('Biotechnology',"Biotechnology"),
#    ('Mechanical Engineering A','Mechanical Engineering A'),
#    ('Mechanical Engineering B','Mechanical Engineering B'),

#    ]
# sems_drop=[
# ("Semester 1 ","Semester 1"),
# ("Semester 2","Semester 2"),
# ("Semester 3","Semester 3"),
# ("Semester 4","Semester 4"),
# ("Semester 5","Semester 5"),
# ("Semester 6","Semester 6"),
# ("Semester 7","Semester 7"),
# ("Semester 8","Semester 8"),
# ("Minors","Minors"),
# ("Honours","Honours")


#    ]