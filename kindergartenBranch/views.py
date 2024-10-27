from django.shortcuts import render
from .models import KindergartenBranch

def branches_overview(request):
    branches = KindergartenBranch.objects.all()
    return render(request, 'branches_overview.html', {'branches': branches})




def branches_view(request):
    branches = KindergartenBranch.objects.all()
    return render(request, "branches.html", {"branches": branches})