# from django.urls import include, path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'employees', views.EmployeeViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
# ---------------------------------------
# ----------------------------------------------------------
from django.urls import path
from . import views

urlpatterns = [
	# path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

    path('', views.index, name = "index"),
    path('add', views.add, name = "add"),
    path('show', views.show, name = "show"),    
    path('preview/<int:id>', views.preview, name = "preview"),    
    path('delete/<int:id>', views.delete, name = "delete"),
    path('update/<int:id>', views.update, name = "update"),
]