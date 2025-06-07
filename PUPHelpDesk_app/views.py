from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

STUDENT_DIRECT_LINE_SECRET = settings.STUDENT_DIRECT_LINE_SECRET
APPLICANT_DIRECT_LINE_SECRET = settings.APPLICANT_DIRECT_LINE_SECRET

def landing_page(request):
    return render(request, 'landing-page.html')

def student_agent(request):
    return render(request, 'student-agent.html')

def applicant_agent(request):
    return render(request, 'applicant-agent.html')

@csrf_exempt
def get_token(request, user_type):

    url = 'https://directline.botframework.com/v3/directline/tokens/generate'

    if user_type == 'student':
        direct_line_secret = STUDENT_DIRECT_LINE_SECRET
    else:
        direct_line_secret = APPLICANT_DIRECT_LINE_SECRET
    
    headers = {
        'Authorization': f'Bearer {direct_line_secret}'
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    
    return JsonResponse({'error': 'Failed to generate token'}, status=500)
