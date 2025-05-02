from django import forms
from .models import Priority, Label

class PriorityForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter priority name'})
    )
    
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        self.instance = kwargs.pop('instance', None)
        super(PriorityForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].initial = self.instance.name
    
    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError("Priority name cannot be empty.")
            
        # Check if a priority with this name already exists for this user
        # Exclude the current priority when editing
        existing_priorities = Priority.objects.filter(user=self.user, name=name)
        if self.instance and self.instance.pk:
            existing_priorities = existing_priorities.exclude(pk=self.instance.pk)
            
        if existing_priorities.exists():
            raise forms.ValidationError(f"Priority '{name}' already exists.")
            
        return name
        
    def save(self, commit=True):
        if self.instance:
            # Update existing instance
            self.instance.name = self.cleaned_data['name']
            if commit:
                self.instance.save()
            return self.instance
        else:
            # Create new instance
            instance = Priority(
                name=self.cleaned_data['name'],
                user=self.user
            )
            if commit:
                instance.save()
            return instance


class LabelForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter label name'})
    )
    
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        self.instance = kwargs.pop('instance', None)
        super(LabelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].initial = self.instance.name
    
    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError("Label name cannot be empty.")
            
        # Check if a label with this name already exists for this user
        # Exclude the current label when editing
        existing_labels = Label.objects.filter(user=self.user, name=name)
        if self.instance and self.instance.pk:
            existing_labels = existing_labels.exclude(pk=self.instance.pk)
            
        if existing_labels.exists():
            raise forms.ValidationError(f"Label '{name}' already exists.")
            
        return name
        
    def save(self, commit=True):
        if self.instance:
            # Update existing instance
            self.instance.name = self.cleaned_data['name']
            if commit:
                self.instance.save()
            return self.instance
        else:
            # Create new instance
            instance = Label(
                name=self.cleaned_data['name'],
                user=self.user
            )
            if commit:
                instance.save()
            return instance