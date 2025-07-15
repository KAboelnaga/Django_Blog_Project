from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm

User = get_user_model()

def users_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})




def create_user_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already used.")
            elif password != confirm_password:
                messages.error(request, "Passwords do not match.")
            else:
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, "User created successfully.")
                return redirect('users_list')

    return render(request, 'users/create_user.html', {'form': form})
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'User updated successfully!')
        return redirect('users_list')
    return render(request, 'users/user_edit.html', {'user': user})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_superuser:
        messages.error(request, "You can't delete another admin.")
        return redirect('users_list')
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('users_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})


@login_required
def promote_user_view(request, user_id):
    user_to_promote = get_object_or_404(User, id=user_id)
    current_user = request.user

    if user_to_promote.is_superuser:
        messages.error(request, "لا يمكن تعديل صلاحيات سوبر يوزر.")
    elif user_to_promote.is_staff:
        if current_user.is_superuser:
            user_to_promote.is_staff = False
            user_to_promote.save()
            messages.success(request, "تم إزالة صلاحية الأدمن.")
        else:
            messages.error(request, "فقط السوبر يوزر يمكنه إزالة صلاحية الأدمن.")
    else:
        user_to_promote.is_staff = True
        user_to_promote.save()
        messages.success(request, "تم ترقية المستخدم لأدمن.")

    return redirect('users_list')