from django.shortcuts import render
from django.db.models import Q
from chat.models import Room

def room_view(request, room_name):
    try:
        chat_room = Room.objects.get(
            Q(name=f"{room_name}_{request.user.username}")
            | Q(name=f"{request.user.username}_{room_name}")
        )
    except Room.DoesNotExist:
        chat_room = Room.objects.create(name=f"{request.user.username}_{room_name}")

    return render(
        request,
        "chat/room.html",
        {
            "room": chat_room,
        },
    )
