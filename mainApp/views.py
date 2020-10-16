from django.shortcuts import render
from django.views.generic.base import View
from usersApp.models import Images
from django.contrib.auth.models import User


class mainPage(View):
    def get(self, request):
        pictures = Images.objects.all()
        return render(request, 'Main.html', {'pic_list': pictures})


def my_picture(request):
    current_user = request.user
    pictures = Images.objects.filter(user__username=current_user)

    return render(request, 'UserPhoto.html', {'pic_list': pictures, 'current_user': current_user})
