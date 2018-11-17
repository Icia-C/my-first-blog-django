from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
]


#post/ significa que la URL debería empezar con la palabra post seguida por una /.
#<int:pk> – Significa que Django buscará un número entero y se lo pasará a la vista en una variable llamada pk.
# / – necesitamos otra / al final de la URL.
