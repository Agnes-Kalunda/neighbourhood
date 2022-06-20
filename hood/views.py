from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SignupForm, BusinessForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood, Profile, Business, Post
from .forms import UpdateProfileForm, NeighbourHoodForm, PostForm
from django.contrib.auth.models import User


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

# Create your views here.
