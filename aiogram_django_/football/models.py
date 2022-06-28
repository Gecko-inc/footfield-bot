from django.db import models


class Config(models.Model):
    title = models.CharField("Наименование", max_length=130)
    description = models.TextField("Описание", blank=True)
    key = models.CharField("Ключ", max_length=130, unique=True)
    value = models.CharField("Значение", blank=True, max_length=210)
    is_private = models.BooleanField("Приватная настройка", default=False)

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.title

    @classmethod
    def get_cfg(cls) -> dict:
        """
          returns a dict of text settings
        """
        context = dict((cfg.key, cfg.value) for cfg in cls.objects.filter(is_private=False))

        return context


class FootballField(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название поля")
    address = models.CharField(max_length=256, verbose_name="Адрес поля")
    size = models.CharField(max_length=256, verbose_name="Размеры поля")
    gate = models.PositiveIntegerField(verbose_name="Количество ворот")
    conditions = models.TextField(verbose_name="Условия")
    location = models.TextField(verbose_name="Локация")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Футбольное поле"
        verbose_name_plural = "Футболные поля"


class ImageForFootballField(models.Model):
    football_field = models.ForeignKey(FootballField, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.football_field.name}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
