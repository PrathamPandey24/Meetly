from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from .forms import MeetForm
from .models import Meet
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


# Create your views here.
class DeleteMeetView(DeleteView):
    model = Meet
    template_name = "meets/Dltmeet.html"
    success_url=reverse_lazy("allmeet")



class AddMeetView(CreateView): 
    template_name = 'meets/AddMeet.html'
    model = Meet
    fields = "__all__"
    success_url = reverse_lazy('allmeet')

    def add_meet(request):
        if request.method=="POST":
            form=MeetForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("success_url")
            else:
                form=MeetForm()
            return render(request, "AllMeets.html",{"form":form})
            


class MainPage(ListView):
    template_name = 'meets/MainPage.html'
    model = Meet
    ordering = ['date']
    context_object_name = 'meets'

    def get_queryset(self):
        queryset=Meet.objects.order_by('date')[:3]
        print(queryset.query)
        return queryset

class AllMeets(ListView):
    template_name = 'meets/AllMeets.html'
    model = Meet
    ordering = ['date']
    context_object_name = 'meets'


class MeetDetail(DetailView):
    template_name = 'meets/MeetDetail.html'
    model = Meet
    context_object_name = 'meet'
    
    def meet(request, pk):
        meet = Meet.objects.get(pk=pk)
        return render(request, 'meets/MeetDetail.html', {'meet': meet})