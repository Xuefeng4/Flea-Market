from django.urls import path
from market.views import (
    HouseList,
    HouseDetail,
    HouseCreate,
    HouseUpdate,
    HouseDelete,
    MyHouse,

    BookList,
    BookDetail,
    BookCreate,
    BookUpdate,
    BookDelete,
    MyBook,

    ClothingList,
    ClothingDetail,
    ClothingCreate,
    ClothingUpdate,
    ClothingDelete,
    MyClothing,

    OtherList,
    OtherDetail,
    OtherCreate,
    OtherUpdate,
    OtherDelete,
    MyOther,

    CarList,
    CarDetail,
    CarCreate,
    CarUpdate,
    CarDelete,
    MyCar,

)

from . import views

urlpatterns = [
    path('house/', HouseList.as_view(), name='HouseList'),
    path('house/<int:pk>/', HouseDetail.as_view(), name='HouseDetail'),
    path('house/create/', HouseCreate.as_view(), name='HouseCreate'),
    path('house/<int:pk>/update/', HouseUpdate.as_view(), name='HouseUpdate'),
    path('house/delete/<int:pk>', HouseDelete.as_view(), name='HouseDelete'),
    path('myHouse/<int:pk>/', MyHouse.as_view(), name='MyHouse'),


    path('book/', BookList.as_view(), name='BookList'),
    path('book/<int:pk>/', BookDetail.as_view(), name='BookDetail'),
    path('book/create/', BookCreate.as_view(), name='BookCreate'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='BookUpdate'),
    path('book/delete/<int:pk>', BookDelete.as_view(), name='BookDelete'),
    path('myBook/<int:pk>/', MyBook.as_view(), name='MyBook'),

    path('clothing/', ClothingList.as_view(), name='ClothingList'),
    path('clothing/<int:pk>/', ClothingDetail.as_view(), name='ClothingDetail'),
    path('clothing/create/', ClothingCreate.as_view(), name='ClothingCreate'),
    path('clothing/<int:pk>/update/', ClothingUpdate.as_view(), name='ClothingUpdate'),
    path('clothing/delete/<int:pk>', ClothingDelete.as_view(), name='ClothingDelete'),
    path('myClothing/<int:pk>/', MyClothing.as_view(), name='MyClothing'),

    path('other/', OtherList.as_view(), name='OtherList'),
    path('other/<int:pk>/', OtherDetail.as_view(), name='OtherDetail'),
    path('other/create/', OtherCreate.as_view(), name='OtherCreate'),
    path('other/<int:pk>/update/', OtherUpdate.as_view(), name='OtherUpdate'),
    path('other/delete/<int:pk>', OtherDelete.as_view(), name='OtherDelete'),
    path('myOther/<int:pk>/', MyOther.as_view(), name='MyOther'),

    path('car/', CarList.as_view(), name='CarList'),
    path('car/<int:pk>/', CarDetail.as_view(), name='CarDetail'),
    path('car/create/', CarCreate.as_view(), name='CarCreate'),
    path('car/<int:pk>/update/', CarUpdate.as_view(), name='CarUpdate'),
    path('car/delete/<int:pk>', CarDelete.as_view(), name='CarDelete'),
    path('myCar/<int:pk>/', MyCar.as_view(), name='MyCar'),



]
