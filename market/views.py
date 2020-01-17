
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group,User

from market.models import(
    House,
    Book,
    Clothing,
    Other,
Car,
)

# House List
class HouseList(ListView):
    model = House
    context_object_name = 'HouseList'
    template_name = 'market/HouseList.html'

class HouseDetail(View):

    def get(self,request,pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk=request.user.pk)[0]
        admin_user = user_object in admin_group
        houseItem = get_object_or_404(House, pk=pk)
        return render(request, 'market/HouseDetail.html', context={'HouseItem': houseItem,'admin_user':admin_user})

class HouseCreate(LoginRequiredMixin,CreateView):

    model = House
    fields = ("houseName","houseDescription","housePrice","housePicUrl","HouseStartDate","HouseEndDate","houseLocation")
    template_name = 'market/HouseForm.html'

    def form_valid(self, form):
        form.instance.houseAuthor = self.request.user
        return super().form_valid(form)


class HouseUpdate(LoginRequiredMixin,UpdateView):
    model = House
    template_name = 'market/HouseFormUpdate.html'
    fields = (
    "houseName", "houseDescription", "housePrice", "housePicUrl", "HouseStartDate", "HouseEndDate", "houseLocation")

class HouseDelete(LoginRequiredMixin,View):
    def get(self, request, pk):
        houseItem = self.get_object(pk)
        return render(
            request,
            'market/HouseConfirmDelete.html',
            {'house': houseItem}
        )

    def get_object(self, pk):
        return get_object_or_404(
            House,
            pk=pk
        )

    def post(self,request,pk):
        houseItem = self.get_object(pk)
        authorPk = houseItem.houseAuthor
        houseItem.delete()
        return redirect('MyHouse', pk=authorPk.pk)

class MyHouse(LoginRequiredMixin,View):

    def get(self, request, pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk = request.user.pk)[0]
        admin_user = user_object in admin_group
        houseItems = House.objects.filter(houseAuthor=pk).order_by('housePostDate')
        return render(request, 'market/MyHouse.html', context={'HouseItems': houseItems, 'author_pk': pk, 'admin_user':admin_user})

# Book
class BookList(ListView):
    model = Book
    context_object_name = 'BookList'
    template_name = 'market/BookList.html'

class BookDetail(View):

    def get(self,request,pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk=request.user.pk)[0]
        admin_user = user_object in admin_group
        bookItem = get_object_or_404(Book, pk=pk)
        return render(request, 'market/BookDetail.html', context={'BookItem': bookItem,'admin_user':admin_user})

class BookCreate(LoginRequiredMixin,CreateView):
    # bookId = models.AutoField(primary_key=True)
    # bookName = models.CharField(max_length=50)
    # bookAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    # bookDescription = models.CharField(max_length=1000)
    # bookPostDate = models.DateField(default=datetime.date.today)
    # bookPrice = models.DecimalField(max_digits=20, decimal_places=2)
    # bookPicUrl = models.URLField(max_length=200, blank=True)
    #
    # bookTitle = models.CharField(max_length=500)
    # bookPublishedAuthor = models.CharField(max_length=50)
    # bookPublishedDate = models.DateField(default=datetime.date.today)
    model = Book
    fields = ("bookName","bookDescription","bookPrice","bookPicUrl","bookTitle","bookPublishedAuthor","bookPublishedDate")
    template_name = 'market/BookForm.html'

    def form_valid(self, form):
        form.instance.bookAuthor = self.request.user
        return super().form_valid(form)


class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    template_name = 'market/BookFormUpdate.html'
    fields = (
    "bookName","bookDescription","bookPrice","bookPicUrl","bookTitle","bookPublishedAuthor","bookPublishedDate")

class BookDelete(LoginRequiredMixin,View):
    def get(self, request, pk):
        bookItem = self.get_object(pk)
        return render(
            request,
            'market/BookConfirmDelete.html',
            {'book': bookItem}
        )

    def get_object(self, pk):
        return get_object_or_404(
            Book,
            pk=pk
        )

    def post(self,request,pk):
        bookItem = self.get_object(pk)
        authorPk = bookItem.bookAuthor
        bookItem.delete()
        return redirect('MyBook', pk=authorPk.pk)

class MyBook(LoginRequiredMixin,View):

    def get(self, request, pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk = request.user.pk)[0]
        admin_user = user_object in admin_group
        bookItems = Book.objects.filter(bookAuthor=pk).order_by('bookPostDate')
        return render(request, 'market/MyBook.html', context={'BookItems': bookItems, 'author_pk': pk, 'admin_user':admin_user})

# Clothing
class ClothingList(ListView):
    model = Clothing
    context_object_name = 'ClothingList'
    template_name = 'market/ClothingList.html'


class ClothingDetail(View):

    def get(self, request, pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk=request.user.pk)[0]
        admin_user = user_object in admin_group
        clothingItem = get_object_or_404(Clothing, pk=pk)
        return render(request, 'market/ClothingDetail.html',
                      context={'ClothingItem': clothingItem, 'admin_user': admin_user})


class ClothingCreate(LoginRequiredMixin, CreateView):
    model = Clothing
    fields = ("clothingName", "clothingDescription", "clothingPrice", "clothingPicUrl", "clothingType", "clothingSize",
              "clothingColor")
    template_name = 'market/ClothingForm.html'

    def form_valid(self, form):
        form.instance.clothingAuthor = self.request.user
        return super().form_valid(form)


class ClothingUpdate(LoginRequiredMixin, UpdateView):
    model = Clothing
    template_name = 'market/ClothingFormUpdate.html'
    fields = (
        "clothingName", "clothingDescription", "clothingPrice", "clothingPicUrl", "clothingType", "clothingSize",
        "clothingColor")


class ClothingDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        clothingItem = self.get_object(pk)
        return render(
            request,
            'market/ClothingConfirmDelete.html',
            {'clothing': clothingItem}
        )

    def get_object(self, pk):
        return get_object_or_404(
            Clothing,
            pk=pk
        )

    def post(self, request, pk):
        clothingItem = self.get_object(pk)
        authorPk = clothingItem.clothingAuthor
        clothingItem.delete()
        return redirect('MyClothing', pk=authorPk.pk)


class MyClothing(LoginRequiredMixin, View):

    def get(self, request, pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk=request.user.pk)[0]
        admin_user = user_object in admin_group
        clothingItems = Clothing.objects.filter(clothingAuthor=pk).order_by('clothingPostDate')
        return render(request, 'market/MyClothing.html',
                      context={'ClothingItems': clothingItems, 'author_pk': pk, 'admin_user': admin_user})
#Car
class CarList(ListView):
    model = Car
    context_object_name = 'CarList'
    template_name = 'market/CarList.html'

class CarDetail(View):

    def get(self,request,pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk=request.user.pk)[0]
        admin_user = user_object in admin_group
        carItem = get_object_or_404(Car, pk=pk)
        return render(request, 'market/CarDetail.html', context={'CarItem': carItem,'admin_user':admin_user})

class CarCreate(LoginRequiredMixin,CreateView):

    model = Car
    fields = ("carName", "carDescription", "carPrice", "carPicUrl", "carBrand", "carMillege", "carYears")
    template_name = 'market/CarForm.html'

    def form_valid(self, form):
        form.instance.carAuthor = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin,UpdateView):
    model = Car
    template_name = 'market/CarFormUpdate.html'
    fields = (
    "carName", "carDescription", "carPrice", "carPicUrl", "carBrand", "carMillege", "carYears")

class CarDelete(LoginRequiredMixin,View):
    def get(self, request, pk):
        carItem = self.get_object(pk)
        return render(
            request,
            'market/CarConfirmDelete.html',
            {'car': carItem}
        )

    def get_object(self, pk):
        return get_object_or_404(
            Car,
            pk=pk
        )

    def post(self,request,pk):
        carItem = self.get_object(pk)
        authorPk = carItem.carAuthor
        carItem.delete()
        return redirect('MyCar', pk=authorPk.pk)

class MyCar(LoginRequiredMixin,View):

    def get(self, request, pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk = request.user.pk)[0]
        admin_user = user_object in admin_group
        carItems = Car.objects.filter(carAuthor=pk).order_by('carPostDate')
        return render(request, 'market/MyCar.html', context={'CarItems': carItems, 'author_pk': pk, 'admin_user':admin_user})

#Other
class OtherList(ListView):
    model = Other
    context_object_name = 'OtherList'
    template_name = 'market/OtherList.html'

class OtherDetail(View):

    def get(self,request,pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk=request.user.pk)[0]
        admin_user = user_object in admin_group
        otherItem = get_object_or_404(Other, pk=pk)
        return render(request, 'market/OtherDetail.html', context={'OtherItem': otherItem,'admin_user':admin_user})

class OtherCreate(LoginRequiredMixin,CreateView):

    model = Other
    fields = ("otherName","otherDescription","otherPrice","otherPicUrl","otherCategory","otherDetail")
    template_name = 'market/OtherForm.html'

    def form_valid(self, form):
        form.instance.otherAuthor = self.request.user
        return super().form_valid(form)


class OtherUpdate(LoginRequiredMixin,UpdateView):
    model = Other
    template_name = 'market/OtherFormUpdate.html'
    fields = (
    "otherName","otherDescription","otherPrice","otherPicUrl","otherCategory","otherDetail")

class OtherDelete(LoginRequiredMixin,View):
    def get(self, request, pk):
        otherItem = self.get_object(pk)
        return render(
            request,
            'market/OtherConfirmDelete.html',
            {'other': otherItem}
        )

    def get_object(self, pk):
        return get_object_or_404(
            Other,
            pk=pk
        )

    def post(self,request,pk):
        otherItem = self.get_object(pk)
        authorPk = otherItem.otherAuthor
        otherItem.delete()
        return redirect('MyOther', pk=authorPk.pk)

class MyOther(LoginRequiredMixin,View):

    def get(self, request, pk):
        admin_group = Group.objects.get(name="administration").user_set.all()
        user_object = User.objects.filter(pk = request.user.pk)[0]
        admin_user = user_object in admin_group
        otherItems = Other.objects.filter(otherAuthor=pk).order_by('otherPostDate')
        return render(request, 'market/MyOther.html', context={'OtherItems': otherItems, 'author_pk': pk, 'admin_user':admin_user})