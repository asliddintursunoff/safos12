from django.db import models

class Mahsulotlar(models.Model):
    mahsulot_nomi=models.CharField(max_length=500)
    narx = models.IntegerField(help_text="so'm")
    rasm = models.ImageField(upload_to="img", null=True,blank=True)
    def __str__(self) -> str:
        return self.mahsulot_nomi
    class Meta:
        verbose_name="Mahsulot"
        verbose_name_plural="Mahsulotlar"
    
   
    
    

class Magazinlar (models.Model):

    magazin = models.CharField(max_length=500)
   
    tarif = models.TextField(help_text="locatsiya , ism va boshqa izohlar", null=True,blank=True)

    def __str__(self) -> str:
        return self.magazin
    class Meta:
        verbose_name="Magazin"
        verbose_name_plural="Magazinlar"




class Savdo(models.Model):
    dukon=models.ForeignKey(Magazinlar, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
    mahsulot_soni=models.IntegerField(help_text="dona",default=0)
    chegirma_narxi=models.IntegerField(help_text="agar chegirma narx bo'lsa",default=0)
    sana = models.DateField( null=True,blank=True)
    
    qarz_tulandi = models.BooleanField() 
    olingan_pul=models.IntegerField(help_text="so'm",default=0)
    class Meta:
        verbose_name="Savdo"
        verbose_name_plural="Savdo"
        ordering = ['-sana']
    
    def magazin1 (self):
        return self.dukon.magazin
    def mahsulot_nomi(self):
        return self.mahsulot.mahsulot_nomi
    def mahsulot_narxi(self):
        return self.mahsulot.narx
    @property

    def umumiy_narx(self):
        if self.mahsulot_soni==0:
            if self.chegirma_narxi==0:
               a= 0
            else:    
               a= 0
        else:    
            if self.chegirma_narxi==0:
               a= self.mahsulot.narx*self.mahsulot_soni
            else:    
               a= self.chegirma_narxi*self.mahsulot_soni
        return a   

    def qarz_olindi(self):
        if self.qarz_tulandi==False:
            a="❌"
        else:
            a="✅"
        return a

        
    def qarzdorlik(self):
        
        
        b=self.umumiy_narx-self.olingan_pul
        return b
    
    
    




class Xarajat(models.Model):
    Sana = models.DateField()
    sababi = models.CharField(max_length=500)
    narxi = models.IntegerField(null=True,blank=True)
    class Meta:
        verbose_name="Xarajat "
        verbose_name_plural="Xarajatlar "
        ordering = ['-Sana']
    
    def __str__(self) -> str:
        return f"{self.Sana}"

    def kun(self):
        return self.Sana

    def sabab(self):
        return self.sababi

    def narx(self):
        return self.narxi
