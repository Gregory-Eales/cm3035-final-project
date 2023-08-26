from django.shortcuts import render

def home(request):

    
    # -----------------------------------
    # this will return all of the post data
    post_title = "test title"
    post_content = "test content"
    post_author = "test author"
    post_date = "test date"
    post = {
        'title': post_title,
        'content': post_content,
        'author': post_author,
        'date_posted': post_date,
    }
    posts = [post] * 5
    # -----------------------------------


    return render(request, 'home.html', {'posts': posts})


from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next', '/'))
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to a URL pattern with the name 'home'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: Log the user in after registration
            return redirect('home')  # Redirect to home page or any other page as needed
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


from django.shortcuts import render

def chat_view(request, conversation_id=1):
    # Dummy data for active conversations
    active_conversations = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'},
    ]

    # Dummy data for the current conversation
    current_conversation = {
        'id': conversation_id,
        'name': 'Sample Conversation',
        'messages': [
            {'author': 'Alice', 'content': 'Hello there'},
            {'author': 'You', 'content': 'General Kenobi'},
            {'author': 'Alice', 'content': 'How are you?'}
        ]
    }

    return render(request, 'chat.html', {
        'active_conversations': active_conversations,
        'current_conversation': current_conversation
    })


def profile_view(request):
    return render(request, 'profile.html', {})