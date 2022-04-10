from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from apps.forms import SignupForm
from apps.models import Chat,ChatGroup

# Create your views here.
def home(request):
    return render(request, 'apps/home.html')

def group_page(request):
    return render(request, 'apps/chat/groups.html')

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'apps/registration/signup.html'

def chatting(request,group_name):
    group = ChatGroup.objects.get(name=group_name)
    chats = []
    if group:
        print(group)
        chats = Chat.objects.filter(group=group)
        # print(chats)
    else:
        group = ChatGroup(name=group_name)
        group.save()
    return render(request, 'apps/chat/chatting.html',{'group_name':group_name,'chats':chats})