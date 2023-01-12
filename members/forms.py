from django import forms
from .models import Division, Status, Employee


class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ('firstname', 'lastname', 'middleI', 'division', 'position', 'empStatus')
		labels = {
			'firstname' : 'First Name',
			'lastname' : 'Last Name',
			'middleI' : 'M.I.',
			'division' : 'Division',
			'position' : 'Position',
			'empStatus' : 'Emp Status'
		}

	def __init__(self, *args, **kwargs):
		super(EmployeeForm, self).__init__(*args, **kwargs)
		self.fields['division'].empty_label = "Select Division"
		self.fields['empStatus'].empty_label = "Select Status"
		self.fields['position'].required = False