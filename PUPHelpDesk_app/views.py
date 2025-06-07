from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

STUDENT_DIRECT_LINE_SECRET = 'CBH50qf9QrRaAU41qBNIVIxqizRDnmCs8Dfw8leBWqGMxkQFcBuIJQQJ99BFACZoyfiAArohAAABAZBS1F35.BeqxxSC9hYSUF4PNzA6zm3eLIO7gyVcOkgOp5bOdLdUi0BcOlis7JQQJ99BFACZoyfiAArohAAABAZBS0WGE'
APPLICANT_DIRECT_LINE_SECRET = 'BNDo7jtYnFq3bSBRHTl5UOaQvyHB1zMKadDLUpMdyJEX6rbPJ0ieJQQJ99BEACYeBjFAArohAAABAZBS1UTf.B88ee093QKUfCrFWPYBRvvjFqHnxF2vFWddJ0eMvFUJRhl4mUdk4JQQJ99BEACYeBjFAArohAAABAZBSIPlc'

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
        print('student')
        direct_line_secret = STUDENT_DIRECT_LINE_SECRET
    else:
        print('applicant')
        direct_line_secret = APPLICANT_DIRECT_LINE_SECRET
    
    headers = {
        'Authorization': f'Bearer {direct_line_secret}'
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    
    return JsonResponse({'error': 'Failed to generate token'}, status=500)
