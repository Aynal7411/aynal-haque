import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY  # Set this in settings.py

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4"
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            reply = response['choices'][0]['message']['content']
            return JsonResponse({'reply': reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
