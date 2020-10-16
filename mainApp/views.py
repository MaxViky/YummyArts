from django.shortcuts import render
from django.views.generic.base import View
from usersApp.models import Images
from django.contrib.auth.models import User


class all_photo(View):
    def get(self, request):
        pictures = Images.objects.all()
        return render(request, 'AllPhoto.html', {'pic_list': pictures})


class image_views(View):
    def get(self, request, pk):
        image = Images.objects.get(id=pk)
        image.view += 1
        Images.save(image)
        return render(request, 'PhotoView.html', {'pic': image})


def main_page(request):
    current_user = request.user
    pictures = Images.objects.order_by('view')
    return render(request, 'Main.html', {'pic_list': pictures, 'current_user': current_user})


def my_picture(request):
    current_user = request.user
    pictures = Images.objects.filter(user__username=current_user)
    return render(request, 'UserPhoto.html', {'pic_list': pictures, 'current_user': current_user})
