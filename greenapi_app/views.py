import requests
from django.shortcuts import render
from .models import GreenAPIInstanceForm
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    form = GreenAPIInstanceForm()
    response_data = None

    if request.method == 'POST':
        form = GreenAPIInstanceForm(request.POST)
        if form.is_valid():
            id_instance = form.cleaned_data['id_instance']
            api_token_instance = form.cleaned_data['api_token_instance']
            action = request.POST.get('action')

            url = f'https://api.green-api.com/waInstance{id_instance}/{action}/{api_token_instance}'

            if action == 'getSettings':
                response = requests.get(url)
            elif action == 'getStateInstance':
                response = requests.get(url)
            elif action == 'sendMessage':
                chatId = request.POST.get('chatId')
                number_code = request.POST.get('code')
                message = request.POST.get('message')
                payload = {'chatId': chatId + number_code, 'message': message}
                response = requests.request("POST", url, json=payload)
            elif action == 'sendFileByUrl':
                chatId = request.POST.get('chatId')
                number_code = request.POST.get('code')
                urlFile = request.POST.get('urlFile')
                fileName = request.POST.get('fileName')
                payload = {'chatId': chatId + number_code, 'urlFile': urlFile, 'fileName': fileName}
                response = requests.post(url, json=payload)

            try:
                response_data = response.json()
                response_data = json.dumps(response_data, indent=4)
            except json.JSONDecodeError:
                response_data = response.text

    return render(request, 'greenapi_app/index.html', {'form': form, 'response_data': response_data})
