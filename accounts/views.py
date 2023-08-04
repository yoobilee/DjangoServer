from django.shortcuts import render

# Create your views here.
def agency_signup(request):
    return render(request, 'agency_signup.html')

def influencer_signup(request):
    return render(request, 'influencer_signup.html')