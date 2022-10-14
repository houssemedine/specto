from dataclasses import field
from django.forms import ModelForm
from .models import Division, Program, Product, Qualification, Workshop, Employee, EmployeeFile, VMS_Planning
from django import forms

class DivisionForm(ModelForm):
    class Meta:
        model = Division
        fields = ['name','location','description']


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['name','description']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','description']


class WorkshopForm(ModelForm):
    class Meta:
        model = Workshop
        fields = ['name','description']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeFileForm(ModelForm):
    class Meta:
        model = EmployeeFile
        fields = '__all__'

class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = ['employee','vms_qualification','vmq_qualification','fives_qualification']
        labels = {
            'fives_qualification': '5S qualification',
        }

class Vms_PlanningForm(ModelForm):
    class Meta:
        model = VMS_Planning
        fields = ['employee_qualified','employee1_visited','employee2_visited','month','year']
        
        