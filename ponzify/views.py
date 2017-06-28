from django.shortcuts import render
from ponzify.models import Plans
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def select_plan(request):
    plans = Plans.objects.all()
    return render(request, 'ponzify/pick_a_plan.html', {'plans': plans})


#@login_required
#def selected_plan(request, plan):




