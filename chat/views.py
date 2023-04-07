from django.shortcuts import render

def room(request, room_name):
    user=request.user
    URL=f'user.profile.image.url'
    return render(request, 'chatroom.html', {
        'room_name': room_name,
        'url':URL
        
    })

