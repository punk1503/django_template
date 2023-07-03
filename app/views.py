from django.shortcuts import render

# Create your views here.
def hello_world_page(request):
    return render(request=request, template_name='hello_world_page.html')
