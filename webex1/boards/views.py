from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Item, Plan, Topic, Post
from django.http import Http404
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def plans(request):
    plans = Plan.objects.all()
    return render(request, 'plans.html', {'plans': plans})

def products(request):
    boards = Item.objects.all()
    return render(request, 'products.html', {'boards': boards})

def contact(request):
    return render(request, 'contact.html')

    
def board_topics(request, pk):
    board = get_object_or_404(Item, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Item, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})