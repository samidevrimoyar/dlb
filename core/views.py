from django.http import JsonResponse

def index(request):
    return JsonResponse({
        "message": "Digital Logbook API is running",
        "docs": "/api/docs/",
        "version": "1.0.0"
    })
