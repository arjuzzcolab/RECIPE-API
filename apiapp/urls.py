
from django.urls import path
from . import views

urlpatterns = [
 
    path('create/',views.RecipeCreate.as_view(),name='create'),
    path('details/<int:pk>/',views.RecipeDetails.as_view(),name='details'),
     path('update/<int:pk>/',views.RecipeUpdate.as_view(),name='update'),
      path('delete/<int:pk>/',views.RecipeDelete.as_view(),name='delete'),
       path('search/<str:name>/',views.RecipeSearch.as_view(),name='search'),
       path('create_recipe/',views.createview,name='create_recipe'),
       path('update_detail/<int:id>',views.update_detail,name='update_detail'),
          path('recipe_update/<int:id>',views.recipe_update,name='recipe_update'),
          path('',views.Index,name='index'),
          path('recipe_fetch/<int:id>/',views.recipe_fetch,name='recipe_fetch'),
          path('recipe_delete/<int:id>',views.recipe_delete,name='recipe_delete')

]