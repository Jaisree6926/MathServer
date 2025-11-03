from django.shortcuts import render

def powerlamp(request):
    context = {}
    context['Power'] = ""
    context['I'] = ""
    context['R'] = ""
    if request.method == 'POST':
        I = request.POST.get('Intensity', '')
        R = request.POST.get('Resistence', '')
        Power = int(I) * int(I) * int(R) if I and R else ""
        context['Power'] = Power
        context['I'] = I
        context['R'] = R
    return render(request, 'mathapp/power.html', context)   # <-- THIS LINE
