from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    fname = models.CharField(max_length=300, verbose_name='نام')
    lname = models.CharField(max_length=300, verbose_name='نام خانوادگی')
    message = models.TextField(max_length=530, verbose_name='متن پیام')
    date = models.DateTimeField(verbose_name='تاریخ نوشته')
    readadmin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
