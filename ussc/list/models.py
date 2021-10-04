from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
from django.core.validators import RegexValidator

# Create your models here.
class ListItem(MPTTModel):
    ROOT = 0
    END_ITEM = 1
    SEARCH_AND_FILTER = 2
    ITEM_TYPE_CHOICES = [
        (ROOT, 'Root'),
        (END_ITEM, 'End item'),
        (SEARCH_AND_FILTER, 'Search and filter')
    ]

    name = models.CharField(
        max_length=255, 
        blank=False,    
        validators=[
            RegexValidator(
                    regex=r'[А-Яа-я _]+',
                    message='''Наименование элемента не должно быть пустым, состоять или начинаться с пробела или
                        нечитаемого символа, в качестве разделителя между словами может быть только
                        одиночный пробел, исключены знаки препинания, возможно использование русских букв
                        и латиницы;'''
            )
        ]
    )
    item_type = models.CharField(
        max_length=50, 
        default=END_ITEM,
        choices=ITEM_TYPE_CHOICES)
    parent = TreeForeignKey(
        'self', 
        blank=True, 
        null=True,  
        on_delete=models.CASCADE,
        related_name='children')

    def __str__(self):
        return self.name

