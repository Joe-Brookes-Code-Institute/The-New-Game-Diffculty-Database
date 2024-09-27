from django.urls import reverse

def home_url(request):
    return {'home_url': reverse('game_list')}