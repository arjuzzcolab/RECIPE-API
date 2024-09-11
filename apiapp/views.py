from django.shortcuts import render,redirect
from rest_framework import generics
from .models import Recipes
from .serializers import Recipeserializer
from rest_framework.permissions import AllowAny
from .forms import Recipeform 
import requests
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
class RecipeCreate(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = Recipeserializer
    permission_classes = [AllowAny]

class RecipeDetails(generics.RetrieveAPIView):
    queryset = Recipes.objects.all()
    serializer_class = Recipeserializer

class RecipeUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = Recipeserializer

class RecipeDelete(generics.DestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = Recipeserializer

class RecipeSearch(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = Recipeserializer

    def get_queryset(self):
        name = self.kwargs.get('name')
        return Recipes.objects.filter(name__icontains=name)
    

def createview(request):
    if request.method == 'POST':
        form = Recipeform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url = 'http://127.0.0.1/create/'
                data = form.cleaned_data
                response = requests.post(api_url,data=data,files={'recipe_Image':request.FILES['recipe_Image']})
                if response.status_code == 200:
                    messages.success(request,'recipe inserted successfully')
                    return redirect('/')

                else:
                    messages.error(request,f'error {response.status_code}')
            except requests.RequestException as e:
                messages.error(request,f'error  {str(e)}')
        else:
            messages.error(request,'invalid')
    else:
        form = Recipeform()
    return render(request,'create_recipe.html',{'form':form})


def update_detail(request,id):
    api_url = f'http://127.0.0.1:8000/details/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        ingrediants = data['recipe'].split('.')
        
    return render(request,'update.html',{'recipes':data,'ingrediants':ingrediants})

#for update
def recipe_update(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        preparation_Time = request.POST['preparation_Time']
        difficulty = request.POST['difficulty']
        vegetarian = request.POST.get('vegetarian','false')
        if vegetarian == 'true':
            vegetarian = True
        else:
            vegetarian = False
        print('image url',request.FILES.get('recipe_Image'))
        recipe = request.POST['recipe']

        api_url = f'http://127.0.0.1:8000/update/{id}/'

        data = {
            'name': name,
            'preparation_Time': preparation_Time,
            'difficulty': difficulty,
            'vegetarian': vegetarian,
            'recipe':recipe,
        }
        files = {'recipe_Image':request.FILES.get('recipe_Image')}
        response = requests.put(api_url,data=data,files=files)
        if response.status_code == 200:
            messages.success(request,'recipe updated successfully')
            return redirect('/')
        else:
            messages.error(request,"error submitting")
    return render(request,'update.html')

def Index(request):
    if request.method == 'POST':
        search = request.POST['search']
        api_url = f'http://127.0.0.1:8000/search/{search}'
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                paginator = Paginator(data,3)
                page_number = request.GET.get('page')
                try:
                    page = paginator.get_page(page_number)
                except EmptyPage:
                    page = paginator.page(page_number.num_pages)
            else:
                data = None
        except requests.RequestException as e:
            data = None
        return render(request,'index.html',{'data':data,'page':page})
    else:
        api_url = f'http://127.0.0.1:8000/create/'
        try:
           
            response = requests.get(api_url)
            if response.status_code == 200:
                data= response.json()
                original_data = data
                paginator = Paginator(original_data,3)
                page_number = request.GET.get('page')
                try:
                    page = paginator.get_page(page_number)
                except EmptyPage:
                    page = paginator.page(page_number.num_pages)
                return render(request,'index.html',{'original_data':original_data,'page':page})

            else:
                messages.error(request,'error')
        except requests.RequestException as e:
            messages.info(request,'error')
            return render(request,'index.html',{'error_message':f'{response.status_code}'})
    return render(request,'index.html')
    

def recipe_fetch(request,id):
    api_url = f'http://127.0.0.1:8000/details/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        ingrediants = data['recipe'].split('.')
        
        return render(request,'recipe_fetch.html',{'recipes':data,'ingrediants':ingrediants})
    else:
        return render(request,'recipe_fetch.html')

            
def recipe_delete(request,id):
    api_url = f'http://127.0.0.1:8000/delete/{id}/'
    response = requests.delete(api_url)
    if response.status_code == 200:
        print(f'item with id {id} has been deleted')
    else:
        print(f'failed to delete item , status code {response.status_code}')
    return redirect('/')
        