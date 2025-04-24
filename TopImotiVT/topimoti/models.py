from django.db import models

from TopImotiVT.topimoti.validators import validate_file_size


class Property(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Заглавие"
    )

    property_type = models.CharField(
        max_length=50,
        choices=[
            ('rent', 'Наем'),
            ('sale', 'Продажба'),
        ],
        verbose_name="Тип обява"
    )

    price = models.IntegerField(
        verbose_name="Цена в евро"
    )

    price_per_meter = models.IntegerField(
        verbose_name="Цена за кв.м."
    )

    location = models.CharField(
        max_length=255,
        verbose_name="Град/Село"
    )

    district = models.CharField(
        max_length=255,
        verbose_name="Квартал"
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Площ (кв.м.)"
    )

    floor = models.PositiveIntegerField(
        verbose_name="Етаж"
    )

    rooms = models.PositiveIntegerField(
        verbose_name="Брой стаи"
    )

    CONSTRUCTION_CHOICES = [
        ('Тухла', 'Тухла'),
        ('Панел', 'Панел'),
        ('Монолит', 'Монолит'),
    ]

    construction_type = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        choices=CONSTRUCTION_CHOICES,
        verbose_name="Вид строителство"
    )

    year_built = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name="Година на завършване",
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class PropertyImage(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to='images',
        validators=(validate_file_size,),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"
