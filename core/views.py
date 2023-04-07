from django.shortcuts import render

def index(request,lang):
    if lang=='javascript':
        URL=f'/static/assets/img/{lang}.jpeg'
    else:
        URL=f'/static/assets/img/{lang}.jpg'
    authenticated = {
            "language" : lang,
            'url':URL
        }
    # print("calling")
    return render(request, 'index.html', authenticated)
def home_page(request):
    return render(request,"home_page.html")