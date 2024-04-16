from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.views.generic.base import TemplateView
from site_setting.models import Slider, FoterGaley, MiddleBaner, KindergartenClasses, PopularTeachers
from .forms import AppointmentRequestForm





def appointment(request):
    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'فرم با موفقیت ذخیره شد.')
        else:
            messages.error(request, 'خطا! لطفاً اطلاعات ورودی را بررسی کنید.')
    else:
        form = AppointmentRequestForm()
    return render(request, 'home/index.html', {'form': form})
 





def get_context_data(request):

    template_name = 'home/index.html'
    
    sliders = Slider.objects.filter(is_active=True)
    banners = MiddleBaner.objects.all()
    classes = KindergartenClasses.objects.all()
    popular = PopularTeachers.objects.all()


    context = {
        
    'sliders': sliders,
    'banners': banners,
    'classes': classes,
    'popular': popular    
        
    }
        
    
    return render(request, template_name, context)

