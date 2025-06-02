# from django.shortcuts import render, redirect
# from .forms import historyForm
# # from django.http import HttpResponse
# from .models import history

# def add_product(request):
#     if request.method == 'POST':
#         form = historyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect after POST
#     else:
#         form = historyForm()  # An empty form for GET request
    
#     return render(request, 'add_product.html', {'form': form})

# def success_view(request):
#     return render(request, 'success.html')


# from .models import history

# def success_view(request):
#     historys = history.objects.all()  # Get all products from MongoDB
#     return render(request, 'success.html', {'historys': historys})

# def index(request):
#     return render(request, 'index.html')

# def home(request):
#     return render(request, 'home.html')




# chat/views.py

from django.shortcuts import render
from .forms import UserInputForm
from .models import ChatHistory
import requests
import os
from dotenv import load_dotenv
from better_profanity import profanity
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv('OPENROUTER_API_KEY')
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Load profanity words
profanity.load_censor_words()

def contains_bad_words(text):
    return profanity.contains_profanity(text)

def home(request):
    response_message = ''

    if request.method == 'POST':
        form = UserInputForm(request.POST)
        
        if form.is_valid():
            user_input = form.cleaned_data['content']

            headers = {
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            }

            prompt = (
                "You are a video script generator bot. "
                "Only generate detailed, structured scripts for video content. "
                "Use many emojis in the script. "
                "If user input contains any inappropriate content, bad words, or negative content, "
                "just give a warning and do not generate a script. Use emojis to indicate the warning. "
                "If user sends any apology message or only a greeting, just reply normally.\n"
                f"User Input: {user_input}"
            )

            data = {
                "model": "deepseek/deepseek-chat:free",
                "messages": [{"role": "user", "content": prompt}]
            }

            try:
                response = requests.post(API_URL, json=data, headers=headers, timeout=5)
                
                if response.status_code == 200:
                    res = response.json()
                    response_message = res['choices'][0]['message']['content']

                    if contains_bad_words(response_message):
                        response_message = "⚠️ Inappropriate content detected. Please try again. ⚠️"

                    # ✅ Save to MongoDB using Django ORM
                    ChatHistory.objects.create(
                        input=user_input,
                        response=response_message
                    )

                else:
                    response_message = f"API error. Status: {response.status_code}"

            except requests.exceptions.RequestException:
                response_message = "Error connecting to AI service. Please try again."

    else:
        form = UserInputForm()

    # Parse response message to handle any special characters or formatting
    response_message = response_message.strip()
    
    return render(request, 'chat/home.html', {
        'form': form,
        'response_message': response_message
    })

def index(request):
    return render(request, 'chat/index.html')


from .models import ChatHistory

def history_view(request):
    history_entries = ChatHistory.objects.all().order_by('-date_time')  # Latest first
    return render(request, 'chat/history.html', {'history_entries': history_entries})
