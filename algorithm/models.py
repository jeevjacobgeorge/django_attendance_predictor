from django.db import models
# from django.db.models import Model
# class holiday(models.Model):
#   holiday_name=models.CharField(default="unnamed holiday",max_length=15)
#   date=models.DateField()
#   def __str__(self):
#       return (self.holiday_name)













#days_options=(('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'))


# class branch(models.Model):

#    branch_name=models.CharField(choices=branch_drop,default='cs',max_length=50)
#    def __str__(self):
#       return self.branch_name
# class semesters(models.Model):

#    sem=models.CharField(choices=sems_drop,default="Semester 1",max_length=15)
#    def __str__(self):
#       return self.sem


#day=models.CharField(choices=days_options,default='Monday',max_length=10)


# class Subject(models.Model):
#    subject_name=models.CharField(max_length=40)
#    subject_branch=models.ManyToManyField(branch)
#    subject_semester=models.ManyToManyField(semesters)
#    number_of_peroids_on_monday=models.PositiveIntegerField(default=0)
#    number_of_peroids_on_tuesday=models.PositiveIntegerField(default=0)
#    number_of_peroids_on_wednesday=models.PositiveIntegerField(default=0)
#    number_of_peroids_on_thursday=models.PositiveIntegerField(default=0)
#    number_of_peroids_on_friday=models.PositiveIntegerField(default=0)

#    def __str__(self):
#       return (self.subject_name)
# class S1_Subject(Subject):
#    pass
# class S2_Subject(Subject):
#    pass
# class S3_Subject(Subject):
#    pass
# class S4_Subject(Subject):
#    pass
# class S5_Subject(Subject):
#    pass
# class S6_Subject(Subject):
#    pass
# class S7_Subject(Subject):
#    pass
# class S8_Subject(Subject):
#    pass




# class Class(models.Model):
#    branch=models.CharField(choices=branches,default='cs',max_length=45)
#    sem_no=models.IntegerField(default=0)



# Create your models here.
#days_options=(('monday','monday'),('tuesday','tuesday'))
#class Attendance(models.Model):
   # subject=models.CharField(max_length=100)
  #  day=models.CharField(choices=days_options,default='monday',max_length=10)
  #  number_of_peroids=models.IntegerField(default=0)

