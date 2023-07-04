from django.shortcuts import render

def page_not_found(request, exception):
    return render(request, 'errors/page_404.html', status=404)

def page_forbidden(request, exception):
    return render(request, 'errors/page_403.html', status=403)

def server_error(request):
    return render(request, 'errors/page_500.html', status=500)
