from django.db import models

# Create your models here.

 
class InfoUser(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя"
    )
    image = models.ImageField(
        upload_to = "info_user/",
        verbose_name = "Фотография пользователя"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = "Профессия пользователя"
    )
    
    skills = models.CharField(
        max_length = 255,
        verbose_name = "Каким образом пользователь делает работу"
    )
    
    email = models.EmailField(
        max_length = 255,
        verbose_name = "Почта пользователя"
    )
    
    phone_number = models.CharField(
        max_length = 255,
        verbose_name = "Номер телефона"
    )
    
    adress = models.CharField(
        max_length = 255,
        verbose_name = "Адрес"
    )
    
     
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"
        
        
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
             

class MyService(models.Model):
    type_job = models.CharField(
        max_length = 255,
        verbose_name = "Тип работы"
    )
    
    number_service = models.IntegerField(
        verbose_name = "Номер работы (порядок)"
    )
    
    aboutproj = models.CharField(
        max_length = 255,
        verbose_name = "Коротко как он делает роботу"
    )
    
    def __str__(self):
        return self.type_job
    
    class Meta:
        verbose_name = "Сервис пользователя"
        verbose_name_plural = "Сервисы пользоватлей"
      
        
class Skills(models.Model):
    
    typedevelop = models.CharField(
        max_length = 255,
        verbose_name = "Какой разработчик"
    )
    
    time = models.CharField(
        max_length = 255,
        verbose_name = "В каком году начал и закончил"
    )
    
    location = models.CharField(
        max_length = 255,
        verbose_name = "Где работал"
    )
    
    
    def __str__(self):
        return self.typedevelop
    
    class Meta:
        verbose_name = "Опыт пользователя"
        verbose_name_plural = "Опыт пользователей"
        
        
        
class Education(models.Model):
    when_course = models.CharField(
        max_length =255 ,
        verbose_name = "Когда обучался"
    )
    
    where_study = models.CharField(
        max_length = 255, 
        verbose_name = "Где учился"
    )
    
    course_name = models.CharField(
        max_length = 255,
        verbose_name = "В каком курсе или университе училя"
    )

    def __str__(self):
        return self.where_study
    
    class Meta:
        verbose_name = "Обучение пользователя"
        verbose_name_plural = "Обучение пользователей"

            
         
   
   
class PersentShow(models.Model):
    name_thing = models.CharField(
        max_length = 255,
        verbose_name = "Какие библиотеки или фреймфорки он знает"
    )
    
    persent = models.CharField(
        max_length = 255,
        verbose_name = "На сколько процентов знает"
    )
    
    logo = models.ImageField(
        upload_to= "persent_show/",
        verbose_name= "Логотип фреймфорка"
    )
    
    
    def __str__(self):
        return self.name_thing 
    
    class Meta:
        verbose_name = "Фреймфорки и скилы пользователя"
        verbose_name_plural = "Фреймфорки и скилы пользователей"
        
        

class Blogs(models.Model):
    name_blog= models.CharField(
        max_length = 255,
        verbose_name = "Имя вашего блога"    
    )

    description = models.TextField(
        verbose_name = "Описание"
    )
    
    
    image = models.ImageField(
        upload_to = "blogs/",
        verbose_name = "Фото блога" 
    )
    
    created_at = models.DateField(
        auto_now_add = True,
        blank = True, null = True
    )
    
    def __str__(self):
        return self.name_blog 
    
    class Meta:
        verbose_name = "Блоги пользователя"
        verbose_name_plural = "Блоги пользователей"
    
    
   
        
        
 