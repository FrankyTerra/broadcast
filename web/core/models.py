from django.db import models

from user.models import User


class AbstractNameDescriptionModel(models.Model):
    """
    Абстрактная модель Наименования и Описания сущности
    """

    name = models.CharField('Наименование', max_length=1000)
    description = models.TextField('Описание')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractTimeStampedModel(models.Model):
    """
    Абстрактная модель Даты создания
    """

    date_created = models.DateTimeField('Дата и время создания', auto_now_add=True)

    class Meta:
        abstract = True


class EventType(AbstractNameDescriptionModel):
    """
    Тип события
    """

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'


class Broadcast(AbstractNameDescriptionModel):
    """
    Трансляция
    """

    date_start = models.DateTimeField('Дата и время начала')
    original_link = models.URLField('Ссылка на оригинал трансляции')
    event_type = models.ForeignKey(
        EventType, verbose_name='Тип спортивного события', related_name='broadcasts', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Трансляция'
        verbose_name_plural = 'Трансляции'


class Event(AbstractTimeStampedModel):
    """
    Событие
    """

    broadcast = models.ForeignKey(Broadcast, verbose_name='Трансляция', related_name='events', on_delete=models.CASCADE)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.text[:200]


class Comment(AbstractTimeStampedModel):
    """
    Комментарий
    """

    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='comments', on_delete=models.CASCADE)
    broadcast = models.ForeignKey(Broadcast, verbose_name='Трансляция', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:200]






