from django.db import models

NULLABLE = {"null": True, "blank": True}


class NetworkNode(models.TextChoices):
    FACTORY = 'factory', 'Завод'
    IE = 'individual_entrepreneur', 'ИП'
    RETAIL_NETWORK = 'retail_network', 'Розничная сеть'


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name="Компания")
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL,
                                 verbose_name="Поставщик",
                                 related_name='provider',
                                 **NULLABLE)
    debt = models.DecimalField(max_digits=15, decimal_places=2,
                               verbose_name="Задолженность перед поставщиком",
                               **NULLABLE)
    created_at = models.DateTimeField(verbose_name="Время создания",
                                      auto_now_add=True)

    company_type = models.CharField(max_length=50, choices=NetworkNode.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Contact(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Email",
                              unique=True)
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    building = models.CharField(max_length=10, verbose_name="Номер дома")

    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name="Компания",
                                related_name="contacts")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(verbose_name="Название")
    model = models.CharField(verbose_name="Модель")
    launch_date = models.DateField(
        verbose_name="Дата выхода продукта на рынок")

    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name="Компания",
                                related_name="products")

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
