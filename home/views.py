from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpRequest
from django.views.generic.base import TemplateView
from site_setting.models import Slider, FoterGaley, MiddleBaner, KindergartenClasses, PopularTeachers






def get_context_data(request):
    
    sliders = Slider.objects.filter(is_active=True)
    banners = MiddleBaner.objects.all()


    context = {
        
        'sliders': sliders,
        'banners': banners    
        
        }
    
    template_name = 'home/index.html'

    return render(request, template_name, context)

