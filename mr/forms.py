from django import forms
from .models import Division, Status, Employee, Property, Service


class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ('user', 'firstname', 'lastname', 'middleI', 'division', 'profstatus', 'position', 'empStatus')
		labels = {
			'user':		'User Name',
			'firstname' : 'First Name',
			'lastname' : 'Last Name',
			'middleI' : 'M.I.',
			'division' : 'Division',
			'profstatus' : 'Professional Status',
			'position' : 'Position',
			'empStatus' : 'Emp Status'
		}

	def __init__(self, *args, **kwargs):
		super(EmployeeForm, self).__init__(*args, **kwargs)
		self.fields['user'].empty_label = "Select UserName"
		self.fields['division'].empty_label = "Select Division"
		self.fields['empStatus'].empty_label = "Select Status"
		self.fields['position'].required = False


class PropertyForm(forms.ModelForm):

	class Meta:
		model = Property
		fields = ('user', 'asset_type', 'unit_office', 'decription', 'property_no', 'serial_no', 'year_acquired',
			'issued_to', 'issued_by', 'original_value', 'useful_life', 'salvage_value')
		labels = {
			'user' : 'User Name',  # to be deleted
			'asset_type' : 'Asset Type',
			'unit_office' : 'Unit/Office',
			'decription' : 'Description',
			'property_no' : 'Property No.',
			'serial_no' : 'Serial No.',
			'year_acquired' : 'Year acquired',
			'issued_to' : 'Issued to',
			'issued_by' : 'Issued by',
			'original_value' : 'Original value',
			'useful_life' : 'Useful life',
			'salvage_value' : 'Salvage value'
		}
		

	def __init__(self, *args, **kwargs):
		super(PropertyForm, self).__init__(*args, **kwargs)
		self.fields['asset_type'].empty_label = "Select"
		self.fields['issued_to'].empty_label = "Select"
		self.fields['issued_by'].empty_label = "Select"


class ServiceForm(forms.ModelForm):

	class Meta:
		model = Service
		fields = ('prop', 'date', 'issues', 'service_rendered', 'action_officer', 'remarks')
		labels = {
			'prop' : 'Property',
			'date' : 'Date',
			'issues' : 'Issues',
			'service_rendered' : 'Service Rendered',
			'action_officer' : 'Action Officer',
			'remarks' : 'Remarks'
		}

	def __init__(self, *args, **kwargs):
		super(ServiceForm, self).__init__(*args, **kwargs)
		self.fields['prop'].empty_label = "Select"
		
			