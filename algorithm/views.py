
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.utils.safestring import mark_safe


year_list=[
   ('2024-04-30','First year'),
   ('2024-04-30','Second year'),
   ('2024-04-30','Third year'),
   ('2024-04-30','Fourth year'),
]
class Newform(forms.Form):
   #branch=forms.CharField(label=mark_safe('<b>Branch'),widget=forms.Select(choices=branches))
   yr=forms.CharField(label=mark_safe("<b>Year of Study:"),widget=forms.Select(choices=year_list))
   att_no=forms.IntegerField(label=mark_safe("<b><br><br><h4><u>Current attendance</u>(Etlab)</h4>No of classes attended till now"),min_value=0,max_value=200)
   tt_no=forms.IntegerField(label=mark_safe("<br><br><b>Total no of classes till now&nbsp;"),min_value=1,max_value=200)
   mon=forms.IntegerField(label=mark_safe("<br><br><u>Check Timetable</u><br>No of periods of the subject each day:<br>Monday&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"),min_value=0,max_value=5,initial=0)
   tue=forms.IntegerField(label=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tuesday&nbsp;"),min_value=0,max_value=5,initial=0)
   wed=forms.IntegerField(label=mark_safe("<br><br>Wednesday:"),min_value=0,max_value=5,initial=0)
   th=forms.IntegerField(label=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thursday:"),min_value=0,max_value=5,initial=0)
   fri=forms.IntegerField(label=mark_safe("<br><br>Friday&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"),min_value=0,max_value=5,initial=0)

   #att_no=forms.IntegerField(label=mark_safe("<b><br><br><br><h3><u>Current attendance</u>(Etlab)</h4><br>No of classes attended till now"),min_value=0,max_value=200)
   #tt_no=forms.IntegerField(label=mark_safe("<br><br><b>Total no of classes till now&nbsp;"),min_value=1,max_value=200)


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
            return HttpResponse('Oops....No of attended classes cannot be greater than total no classes.Reload site:)')



         from datetime import date
         from dateutil.rrule import rrule, DAILY
         import numpy as np

         ans=[]

         def weekday_count(start, end):

            leaves = [
            '2024-03-08',
            '2024-03-28',
            '2024-03-29',
            '2024-04-10',
            '2024-05-01',
            '2024-06-17',
            '2024-07-16',
            '2024-08-15',
            '2024-08-26',
            '2024-08-28'
]

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

















