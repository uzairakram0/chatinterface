from django.shortcuts import render, redirect
import os
import openai
from .models import ChatMessage, ApiKey

openai.organization = "org-A7yjsJ6dsKmofOOM6S96voW8"
openai.api_key = os.getenv("OPENAI_API_KEY")

def index(request):
    if request.method == 'GET' and request.session.get('chat_messages'):
        del request.session['chat_messages']

    if not request.session.get('chat_messages'):
        request.session['chat_messages'] = []

    if request.method == 'POST':
        if openai.api_key == None:
            agent_message = "Please enter your OpenAI API key"
            request.session['chat_messages'].append({'sender': 'Agent', 'content': agent_message})
            request.session.modified = True
            return render(request, "chat/index.html", {'messages': request.session.get('chat_messages')})
        
        user_message = request.POST.get('prompt')
        if user_message:
            ChatMessage.objects.create(sender='User', content=user_message)
            request.session['chat_messages'].append({'sender': 'User', 'content': user_message})
            response = openai.ChatCompletion.create(
                    model= 'gpt-4',
                    messages = [
                    {"role": "assistant", "content":"you are a helpful assistant"},
                    {"role": "user", "content": user_message}
                ],
                temperature = 1
            )
            agent_message = f"{response['choices'][0]['message']['content']}"

            if len(agent_message) == 0:
                agent_message = "blah blah blah"
            request.session['chat_messages'].append({'sender': 'Agent', 'content': agent_message})
            ChatMessage.objects.create(sender='Agent', content=agent_message)
            
            request.session.modified = True
            
    messages = ChatMessage.objects.all()
    return render(request, "chat/index.html", {'messages': messages})


def key(request):
    if request.method == 'POST':
        openai.api_key = request.POST.get('apiKey')
    return redirect('index')

def clear(request):
    ChatMessage.objects.all().delete()
    return redirect('index')
