from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
from django.utils.safestring import mark_safe

class CustomAccountAdapter(DefaultAccountAdapter):
    def render_content(self, template_name, context):
        content = super().render_content(template_name, context)
        home_url = reverse('game_list')  # Assuming 'game_list' is your home page
        home_button = f'<a href="{home_url}" class="home-button">Home</a>'
        return mark_safe(home_button + content)