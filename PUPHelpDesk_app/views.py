from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing-page.html')

def student_agent(request):
    return render(request, 'student-agent.html')
