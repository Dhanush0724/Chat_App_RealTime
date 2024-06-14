from django.shortcuts import render , get_list_or_404
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def chat_view(request):
    chat_group = get_list_or_404(ChatGroup,group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    return render(request,'chat.html',{'chat_messages':chat_messages})