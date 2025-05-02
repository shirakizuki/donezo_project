from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Priority, Label
from .forms import PriorityForm, LabelForm  # Import the custom forms

# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Get user by email
            user = User.objects.get(email=email)
            # Authenticate with username and password
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home', user_id=user.id, section='today')
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if all fields are filled
        if not all([first_name, last_name, email, password, confirm_password]):
            messages.error(request, "All fields are required.")
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        try:
            # Validate password
            validate_password(password)
            
            # Create user with email as username
            user = User.objects.create_user(
                username=email,  # Using email as username
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Log user in
            auth_login(request, user)
            return redirect('home', user_id=user.id)
            
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('register')
    
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('landing_page')

@login_required
def home(request, user_id, section='today'):
    if request.user.id != user_id:
        return redirect('home', user_id=request.user.id, section=section)
    
    valid_sections = ['today', 'upcoming', 'filter', 'profile']
    if section not in valid_sections:
        return redirect('home', user_id=user_id, section='today')

    # Base context with user and section
    context = {'user': request.user, 'section': section}
    
    # If we're on the filter section, fetch priorities and labels
    if section == 'filter':
        priorities = Priority.objects.filter(user=request.user)
        labels = Label.objects.filter(user=request.user)
        # Add form instances to the context
        priority_form = PriorityForm(user=request.user)
        label_form = LabelForm(user=request.user)
        context.update({
            'priorities': priorities,
            'labels': labels,
            'priority_form': priority_form,
            'label_form': label_form
        })

    return render(request, 'dashboard.html', context)

@login_required # READ
def filters(request, user_id):
    if request.user.id != user_id:
        return redirect('filters', user_id=request.user.id)
    
    # Get user's priorities and labels for display
    priorities = Priority.objects.filter(user=request.user)
    labels = Label.objects.filter(user=request.user)
    
    # Create form instances
    priority_form = PriorityForm(user=request.user)
    label_form = LabelForm(user=request.user)
    
    return render(request, 'dashboard/filter.html', {
        'user': request.user,
        'priorities': priorities,
        'labels': labels,
        'priority_form': priority_form,
        'label_form': label_form
    })

@login_required # UPDATE
def edit_priority(request, user_id, priority_id):
    if request.user.id != user_id:
        return redirect('edit_priority', user_id=request.user.id, priority_id=priority_id)
    
    priority = get_object_or_404(Priority, id=priority_id, user=request.user)
    
    if request.method == 'POST':
        # Map the priority_name from the form to the name field expected by our form
        form_data = request.POST.copy()
        if 'priority_name' in form_data:
            form_data['name'] = form_data['priority_name']
            
        form = PriorityForm(user=request.user, data=form_data, instance=priority)
        if form.is_valid():
            form.save()
            messages.success(request, "Priority updated successfully.")
        else:
            for error in form.errors.get('name', []):
                messages.error(request, error)
        
        return redirect('home', user_id=user_id, section='filter')
    
    # This should never be called directly anymore as editing is done in the modal
    return redirect('home', user_id=user_id, section='filter')

@login_required
def delete_priority(request, user_id, priority_id):
    if request.user.id != user_id:
        return redirect('delete_priority', user_id=request.user.id, priority_id=priority_id)
    
    priority = get_object_or_404(Priority, id=priority_id, user=request.user)
    priority_name = priority.name
    priority.delete()
    
    messages.success(request, f"Priority '{priority_name}' deleted successfully.")
    # Redirect back to the home filter page instead of filters page
    return redirect('home', user_id=user_id, section='filter')

@login_required
def edit_label(request, user_id, label_id):
    if request.user.id != user_id:
        return redirect('edit_label', user_id=request.user.id, label_id=label_id)
    
    label = get_object_or_404(Label, id=label_id, user=request.user)
    
    if request.method == 'POST':
        # Map the label_name from the form to the name field expected by our form
        form_data = request.POST.copy()
        if 'label_name' in form_data:
            form_data['name'] = form_data['label_name']
            
        form = LabelForm(user=request.user, data=form_data, instance=label)
        if form.is_valid():
            form.save()
            messages.success(request, "Label updated successfully.")
        else:
            for error in form.errors.get('name', []):
                messages.error(request, error)
        
        return redirect('home', user_id=user_id, section='filter')
    
    # This should never be called directly anymore as editing is done in the modal
    return redirect('home', user_id=user_id, section='filter')

@login_required
def delete_label(request, user_id, label_id):
    if request.user.id != user_id:
        return redirect('delete_label', user_id=request.user.id, label_id=label_id)
    
    label = get_object_or_404(Label, id=label_id, user=request.user)
    label_name = label.name
    label.delete()
    
    messages.success(request, f"Label '{label_name}' deleted successfully.")
    # Redirect back to the home filter page instead of filters page
    return redirect('home', user_id=user_id, section='filter')

@login_required
def add_priority(request, user_id):
    if request.user.id != user_id:
        return redirect('add_priority', user_id=request.user.id)
    
    if request.method == 'POST':
        # Check if user already has 5 priorities
        if Priority.objects.filter(user=request.user).count() >= 5:
            messages.error(request, "Maximum limit of 5 priorities reached. Please delete an existing priority first.")
            return redirect('home', user_id=user_id, section='filter')
            
        # Map the priority_name from the form to the name field expected by our form
        form_data = request.POST.copy()
        if 'priority_name' in form_data:
            form_data['name'] = form_data['priority_name']
            
        form = PriorityForm(user=request.user, data=form_data)
        if form.is_valid():
            form.save()
            messages.success(request, f"Priority '{form.cleaned_data['name']}' added successfully.")
        else:
            for error in form.errors.get('name', []):
                messages.error(request, error)
    
    # Redirect back to the home filter page
    return redirect('home', user_id=user_id, section='filter')

@login_required
def add_label(request, user_id):
    if request.user.id != user_id:
        return redirect('add_label', user_id=request.user.id)
    
    if request.method == 'POST':
        # Map the label_name from the form to the name field expected by our form
        form_data = request.POST.copy()
        if 'label_name' in form_data:
            form_data['name'] = form_data['label_name']
            
        form = LabelForm(user=request.user, data=form_data)
        if form.is_valid():
            form.save()
            messages.success(request, f"Label '{form.cleaned_data['name']}' added successfully.")
        else:
            for error in form.errors.get('name', []):
                messages.error(request, error)
    
    # Redirect back to the home filter page
    return redirect('home', user_id=user_id, section='filter')

def logout_view(request):
    logout(request)
    return redirect('landing_page')

