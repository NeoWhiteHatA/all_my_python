from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
class OnePageView(TemplateView):
    template_name = 'one_page.html'
class SecondPageView(TemplateView):
    template_name = 'second_page.html'
class ThreePageView(TemplateView):
    template_name = 'three_page.html'
class SixPageView(TemplateView):
    template_name = 'six_page.html'

# Create your views here.
