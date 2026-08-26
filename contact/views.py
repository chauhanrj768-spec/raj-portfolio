import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage, Profile


def portfolio(request):
    """Serve the main portfolio page."""
    photo_url = Profile.get_photo_url()
    return render(request, 'index.html', {'profile_photo': photo_url})


@csrf_exempt
def contact_api(request):
    """POST /api/contact/ — save a contact message to PostgreSQL."""
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Method not allowed.'}, status=405)
    try:
        data = json.loads(request.body)
    except Exception:
        data = request.POST

    name    = str(data.get('name',    '')).strip()
    email   = str(data.get('email',   '')).strip()
    subject = str(data.get('subject', '')).strip()
    message = str(data.get('message', '')).strip()

    if not name or not email or not message:
        return JsonResponse({'ok': False, 'error': 'Name, email and message are required.'}, status=400)

    msg = ContactMessage.objects.create(
        name=name, email=email, subject=subject, message=message
    )
    return JsonResponse({
        'ok': True,
        'message': f'Thank you {name}! Your message has been received.',
        'id': msg.id
    }, status=201)


def messages_dashboard(request):
    """Custom messages dashboard at /messages/"""
    msgs   = ContactMessage.objects.all()
    unread = msgs.filter(is_read=False).count()
    return render(request, 'messages_dashboard.html', {
        'messages_list': msgs,
        'total':  msgs.count(),
        'unread': unread,
    })


def mark_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_read = True
    msg.save()
    return redirect('messages_dashboard')


def delete_message(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    return redirect('messages_dashboard')
