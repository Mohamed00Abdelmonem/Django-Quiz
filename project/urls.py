"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quiz.views import quiz_list,quiz_detail,submit_quiz,quiz_result

urlpatterns = [
    path('admin/', admin.site.urls),
     path('quizzes/', quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', submit_quiz, name='submit_quiz'),
    path('quiz/<int:quiz_id>/result/', quiz_result, name='quiz_result'),

]


