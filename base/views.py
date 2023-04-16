from django.shortcuts import render
import openai, os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY")

def bot(request): 
    bot_response = None 
    if api_key is not None and request.method=="POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = (f"Critique this section from my resume; what else can I do to stand out: {user_input}")
        response = openai.Completion.create(
            model = 'text-davinci-003', 
            prompt = prompt, 
            max_tokens = 256, 
            temperature = 0.5
        )
        print(response)
        bot_response = response["choices"][0]["text"]
    return render(request, 'base/main.html', {
        "response": bot_response
    })

def home(request): 
    return render(request, "base/landing.html")