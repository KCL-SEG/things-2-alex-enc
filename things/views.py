from django.shortcuts import render
from things.forms import ThingForm
def home(request):
    if request.method=='POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            quantity = form.cleaned_data.get('quantity')
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
