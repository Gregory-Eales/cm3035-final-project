from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth.models import User
import json

# import image from models
from .models import Image, Post, Friend, Message

def home(request):

    # if user is not logged in, redirect to login page, return no data
    if not request.user.is_authenticated:
        return render(request, 'home.html')

    # GET ALL posts.user_id = user.id, order by created desdending
    posts = Post.objects.filter(user_id=request.user.id).order_by('-created')

    # get the user object
    profile_user = User.objects.get(id=request.user.id)

    # GET ALL image.user_id = user.id
    images = Image.objects.filter(user_id=request.user.id)

    friends = Friend.objects.filter(friender_id=request.user.id)
    # get the username of the friends
    for friend in friends:
        friend.username = User.objects.get(id=friend.friendee_id).username

    return render(request, 'home.html', {'profile_user': profile_user, 'posts': posts, 'friends': friends, 'images': images})


# can take a user and display their profile
def profile_view(request, username):

    if username is None:
        username = request.user.username

    # get the user object
    profile_user = User.objects.get(username=username)

    # get the user's posts
    posts = Post.objects.filter(user_id=profile_user.id).order_by('-created')

    friends = Friend.objects.filter(friender_id=profile_user.id)

    # GET ALL image.user_id = user.id
    images = Image.objects.filter(user_id=profile_user.id)

    # try and find the current user as the friender and the profile user as the friendee
    is_friend = Friend.objects.filter(friender_id=request.user.id, friendee_id=profile_user.id).exists()

    data = {
        'profile_user': profile_user,
        'posts': posts,
        'friends': friends,
        'images': images,
        'is_friend': is_friend 
    }
    
    return render(request, 'profile.html', data)


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


def chat_view(request, user_id=1):
    
    # get the user object
    profile_user = User.objects.get(id=request.user.id)
    # get the users friends
    friends = Friend.objects.filter(friender_id=request.user.id)

    for friend in friends:
        friend.username = User.objects.get(id=friend.friendee_id).username
        friend.user_id = friend.friendee_id


    return render(request, 'chat.html', {'profile_user': profile_user, 'friends': friends})


def search_view(request):
    query = request.GET.get('query', '')  # Retrieve the search query from GET parameters

    # Use the Q object for a case-insensitive 'icontains' search for username
    matching_profiles = User.objects.filter(Q(username__icontains=query))

    # print profiles in json format
    print(matching_profiles.values())

    # Pass the list of matching profiles to the template
    return render(request, 'search.html', {'matching_profiles': matching_profiles})


def image_view(request):

    '''
        class Image(models.Model):
        name = models.CharField(max_length=256, unique=True, db_index=True)
        image = models.FileField(blank=False)
        user_id = models.IntegerField(blank=False)
        def __str__(self):
            return self.name
    '''
    
    # if post then save image
    if request.method == 'POST':
        # save image
        image = Image()
        image.name = request.POST.get('name')
        image.image = request.FILES.get('image')
        image.user_id = request.POST.get('user_id')
        image.save()

        # redirect to home
        return redirect('/')


def create_post(request):

    # if post then save image
    if request.method == 'POST':
        
        # get the user_id of the user sending the request

        post = Post()
        post.content = request.POST.get('content')
        post.user_id = request.user.id
        post.save()

        # redirect to home
        return redirect('/')

def add_friend(request):

    # if post then save image
    if request.method == 'POST':
        
        # get the user_id of the user sending the request
        user_id = request.user.id

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        friend_id = body_data['friend_id']

        # add the friend
        friend = Friend()
        friend.friender_id = user_id
        friend.friendee_id = friend_id 
        friend.save()

        # redirect to home
        return redirect('/')