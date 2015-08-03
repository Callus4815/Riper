from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View
from .models import Fruit


class IndexView(ListView):
	model = Fruit
	template_name = "fruits/index.html"
	context_object_name = "list_of_fruits"


	def get_queryset(self):
		return Fruit.objects.all()


def search_bar(request):
    query = request.GET.get('q')
    if query:
        results = Fruit.objects.filter(name__icontains=request.GET['q'])
    else:
        results = Fruit.objects.all()
    return render(request, 'fruits/search_results.html' , {'results': results})