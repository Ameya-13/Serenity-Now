# from django.shortcuts import render

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello World!")

# # Create your views here.
#name it mind-mate
#vm ip --> 34.70.142.218
#gpt
import openai
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

API_KEY = "you api key"
openai.api_key = API_KEY

@csrf_exempt
def chatbot_view(request):
    print("Chatbot view called")
    if request.method == 'POST':
        # Get user input from the POST request
        user_input = request.POST.get('message')

        # Call GPT-3 API with user_input
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a therapist, trying to help your client's mental health."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=128,
            n=1,
            stop=None,
            temperature=0.7,
        )
        response=response['choices'][0]["message"]["content"]

        # Create response JSON object
        data = {
            'user_input': user_input,
            'bot_response': response,
        }

        return JsonResponse(data)
    else:
        # Render chatbot UI template on GET request
        return render(request, 'chatbot.html')
