from django.db import models

# Create your models here.        
class Secondary(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    yearsexper = models.IntegerField(
        verbose_name = "Опыт работы пользователя"
    )
    
    projectfinish = models.IntegerField(
        verbose_name = "Проекты завершенный"
    )
    
    happyclients = models.IntegerField(
        verbose_name = "Счастливые клиенты"
    )
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Доп информации пользователя"
        verbose_name_plural = "Доп информации пользователей"
   
   
   
        
class Backend(models.Model):
    type_dev = models.CharField(
        max_length = 255,
        verbose_name = "Тип разработки"
    )
    
    name_project = models.CharField(
        max_length = 255,
        verbose_name = "Имя проекта" 
    )

    about_project = models.CharField(
        max_length = 255,
        verbose_name = "Коротко о проекте"
    )
    
    image_project = models.ImageField(
        upload_to= "backend/",
        verbose_name= "Фотография проекта"
    )
    

    def __str__(self):
        return self.type_dev
    
    class Meta:
        verbose_name = "Backend проект пользователя"
        verbose_name_plural = "Backend проекты пользователей"
   

        
        
class Frontend(models.Model):
    
    type_dev = models.CharField(
        max_length = 255,
        verbose_name = "Тип разработки"
    )
    name_project = models.CharField(
        max_length = 255,
        verbose_name = "Имя проекта" 
    )

    about_project = models.CharField(
        max_length = 255,
        verbose_name = "Коротко о проекте"
    )
    
    image_project = models.ImageField(
        upload_to= "frontend/",
        verbose_name= "Фотография проекта"
    )
    

    def __str__(self):
        return self.type_dev
    
    class Meta:
        verbose_name = "Frontend проект пользователя"
        verbose_name_plural = "Frontend проекты пользователей"
   

class Desinger(models.Model):
    
    type_dev = models.CharField(
        max_length = 255,
        verbose_name = "Тип разработки"
    )
    
    name_project = models.CharField(
        max_length = 255,
        verbose_name = "Имя проекта" 
    )

    about_project = models.CharField(
        max_length = 255,
        verbose_name = "Коротко о проекте"
    )
    
    image_project = models.ImageField(
        upload_to= "desinger/",
        verbose_name= "Фотография проекта"
    )
    

    def __str__(self):
        return self.type_dev
    
    class Meta:
        verbose_name = "Desinger проект пользователя"
        verbose_name_plural = "Desinger проекты пользователей"
   

        
class Android(models.Model):
    type_dev = models.CharField(
        max_length = 255,
        verbose_name = "Тип разработки"
    )
    
    name_project = models.CharField(
        max_length = 255,
        verbose_name = "Имя проекта" 
    )

    about_project = models.CharField(
        max_length = 255,
        verbose_name = "Коротко о проекте"
    )
    
    image_project = models.ImageField(
        upload_to= "android/",
        verbose_name= "Фотография проекта"
    )
    

    def __str__(self):
        return self.type_dev
    
    class Meta:
        verbose_name = "Android проект пользователя"
        verbose_name_plural = "Android проекты пользователей"



       
class Colleagues(models.Model):
    full_name = models.CharField(
        max_length = 255,
        verbose_name = "Имя коллеги"
    )
    
    
    degree = models.CharField(
        max_length = 255, 
        verbose_name = "Должность"
    )
    
    company = models.CharField(
        max_length = 255,
        verbose_name = "В каком компании работает"
    )
    
    photo = models.ImageField(
        upload_to = "colleagues/",
        verbose_name = "Фото коллеги"
    )
    
    description = models.CharField(
        max_length = 255, 
        verbose_name = "О коллеге Как он помогает?"
    )
    
    
    def __str__(self):
        return self.full_name
    
    
    class Meta:
        verbose_name = "Информация о коллег"
        verbose_name_plural = "Информация о коллег" 
