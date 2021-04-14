from django.shortcuts import render


async def index(request):
    return render(request, 'index.html', {})


async def room(request, room_name,user_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name,
        'user_name':user_name
    })

