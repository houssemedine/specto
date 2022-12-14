from dataclasses import field
from django.forms import ModelForm
from .models import Division, Program, Product, Qualification, Workshop, Employee, EmployeeFile, VMS_Planning, VMQ_Planning
from django import forms


class DivisionForm(ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Division name'}))
    location = forms.CharField(label='Location', widget=forms.TextInput(attrs={'placeholder': 'Division location'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'placeholder': 'Division description'}))
    class Meta:
        model = Division
        fields = ['name','location','description']


class ProgramForm(ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Program name'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'placeholder': 'Program description'}))
    class Meta:
        model = Program
        fields = ['name','description']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','description']


class WorkshopForm(ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Workshop name'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'placeholder': 'Workshop description'}))
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

class VMS_PlanningForm(ModelForm):
    class Meta:
        model = VMS_Planning
        fields = ['vms_employee_qualified','vms_employee_visited','month','year']

class VMQ_PlanningForm(ModelForm):
    class Meta:
        model = VMQ_Planning
        fields = ['vmq_employee_qualified','vmq_employee_visited','month','year']

class VMQ_PlanningForm_Custom(ModelForm):
    class Meta:
        model = VMQ_Planning
        fields = ['vmq_employee_qualified','vmq_employee_visited']