from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Finch, Sighting, Feather
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feathers"] = Feather.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object 
        name = self.request.GET.get('name')
        # If a query exists we will filter by name 
        if name != None:
                # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
                context["finches"] = Finch.objects.filter(name__icontains=name, user=self.request.user)
                # We add a header context that includes the search param
                context["header"] = f"Searching for {name}"
        else:
                context["finches"] = Finch.objects.filter(user=self.request.user) # this is where we add the key into our context object for the view to use
                # default header for not searching 
                context["header"] = "Trending Small Fries"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FinchCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['feathers'] = Feather.objects.all()
      return context

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_update.html"
    
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finches/"

class SightingCreate(View):
  def post(self, request, pk):
    name = request.POST.get('name')
    location = request.POST.get('location')
    finches = Finch.objects.get(pk=pk)
    Sighting.objects.create(name=name, location=location, finch=finches)
    return redirect('finch_detail', pk=pk)

class FeathersAssoc(View):
  def get(self, request, pk, finches_pk):
    assoc = request.GET.get("assoc")
    if assoc == 'remove':
      Feather.objects.get(pk=pk).finch.remove(finches_pk)
    if assoc == "add":
      Feather.objects.get(pk=pk).finch.add(finches_pk)
    
    return redirect('home')

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("finch_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)