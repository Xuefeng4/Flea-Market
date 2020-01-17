from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class House(models.Model):
    houseId = models.AutoField(primary_key=True)
    houseName = models.CharField(max_length=50)
    houseAuthor = models.ForeignKey(User,on_delete=models.CASCADE)


    houseDescription = models.CharField(max_length=1000)
    housePostDate = models.DateField(default=datetime.date.today)
    housePrice = models.DecimalField(max_digits=20, decimal_places=2)
    housePicUrl = models.URLField(max_length=200, blank=True)

    HouseStartDate = models.DateField(default=datetime.date.today)
    HouseEndDate = models.DateField(default=datetime.date.today)
    houseLocation = models.CharField(max_length=100,default="Champaign")

    def get_absolute_url(self):
        return reverse('HouseDetail',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('HouseUpdate', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('HouseDelete', kwargs={'pk': self.pk})


class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=50)
    bookAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    bookDescription = models.CharField(max_length=1000)
    bookPostDate = models.DateField(default=datetime.date.today)
    bookPrice = models.DecimalField(max_digits=20, decimal_places=2)
    bookPicUrl = models.URLField(max_length=200, blank=True)

    bookTitle = models.CharField(max_length=500)
    bookPublishedAuthor = models.CharField(max_length=50)
    bookPublishedDate = models.DateField(default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('BookDetail',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('BookUpdate', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('BookDelete', kwargs={'pk': self.pk})



class Clothing(models.Model):

    clothingId = models.AutoField(primary_key=True)
    clothingName = models.CharField(max_length=50)
    clothingAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    clothingDescription = models.CharField(max_length=1000)
    clothingPostDate = models.DateField(default=datetime.date.today)
    clothingPrice = models.DecimalField(max_digits=20, decimal_places=2)
    clothingPicUrl = models.URLField(max_length=200, blank=True)

    clothingType = models.CharField(max_length=50)
    clothingSize = models.CharField(max_length=50)
    clothingColor = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ClothingDetail',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('ClothingUpdate', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('ClothingDelete', kwargs={'pk': self.pk})

class Other(models.Model):
    otherId = models.AutoField(primary_key=True)
    otherName = models.CharField(max_length=50)
    otherAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    otherDescription = models.CharField(max_length=1000)
    otherPostDate = models.DateField(default=datetime.date.today)
    otherPrice = models.DecimalField(max_digits=20, decimal_places=2)
    otherPicUrl = models.URLField(max_length=200, blank=True)

    otherCategory = models.CharField(max_length=50)
    otherDetail = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('OtherDetail',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('OtherUpdate', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('OtherDelete', kwargs={'pk': self.pk})

class Car(models.Model):
    carId = models.AutoField(primary_key=True)
    carName = models.CharField(max_length=50)
    carAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    carDescription = models.CharField(max_length=1000)
    carPostDate = models.DateField(default=datetime.date.today)
    carPrice = models.DecimalField(max_digits=20, decimal_places=2)
    carPicUrl = models.URLField(max_length=200, blank=True)

    carBrand = models.CharField(max_length=500)
    carMillege = models.CharField(max_length=50)
    carYears = models.DecimalField(max_digits=20, decimal_places=0)

    def get_absolute_url(self):
        return reverse('CarDetail',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('CarUpdate', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('CarDelete', kwargs={'pk': self.pk})

