from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from apps.forms import SignupForm
from apps.models import Chat,ChatGroup
from django.contrib.auth.views import LoginView
from django.conf import settings
# Create your views here.
def home(request):
    return render(request, 'apps/home.html')

def group_page(request):
    if request.user.is_authenticated:
        chat_groups = ChatGroup.objects.all()
        return render(request, 'apps/chat/groups.html',{'chat_groups':chat_groups})
    else:
        return redirect('/login')

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'apps/registration/signup.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        self.object = None
        return super().get(request, *args, **kwargs)
   


def chatting(request,group_name):
    if request.user.is_authenticated:
        group = ChatGroup.objects.filter(name__in=group_name)
        chats = []
        if group:
            print(group)
            chats = Chat.objects.filter(group__in=group)
        else:
            group = ChatGroup(name=group_name)
            group.save()
        return render(request, 'apps/chat/chatting.html',{'group_name':group_name,'chats':chats})
    else:
        return redirect('/login')