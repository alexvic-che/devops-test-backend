from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "ok"})


def hello(request):
    return JsonResponse({
        "message": "Hello from Django backend",
        "service": "backend",
    })