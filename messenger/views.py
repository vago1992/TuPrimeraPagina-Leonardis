from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def inbox(request):
    mensajes = Message.objects.filter(receiver=request.user).order_by("-created_at")
    return render(request, "messenger/inbox.html", {"mensajes": mensajes})

@login_required
def message_detail(request, pk):
    mensaje = get_object_or_404(Message, pk=pk, receiver=request.user)
    mensaje.is_read = True
    mensaje.save()
    return render(request, "messenger/message_detail.html", {"mensaje": mensaje})

@login_required
def send_message(request):
    users = User.objects.exclude(id=request.user.id)

    if request.method == "POST":
        receiver_id = request.POST.get("receiver")
        subject = request.POST.get("subject")
        body = request.POST.get("body")

        receiver = User.objects.get(id=receiver_id)

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            subject=subject,
            body=body
        )
        return redirect("inbox")

    return render(request, "messenger/send_message.html", {"users": users})