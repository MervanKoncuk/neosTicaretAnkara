from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
class AltKategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
            return self.isim
class Tek(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
            return self.isim

class Urun(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null = True) # SET_NULL
    sub_category = models.ManyToManyField(AltKategori)
    tek = models.OneToOneField(Tek, on_delete=models.SET_NULL, null=True, blank=True)
    isim = models.CharField(max_length=200)
    aciklama = models.TextField(max_length=500)
    fiyat = models.IntegerField()
    resim = models.FileField(upload_to='urunler/', null=True, blank=True)

    def __str__(self):
        return self.isim


# foreignkey = manytoOne
# manytomany
# onetoone