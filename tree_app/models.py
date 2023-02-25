from django.db import models


class Menu(models.Model):
    name = models.CharField('Menu', max_length=50)
    slug = models.SlugField('Menu', max_length=50, unique=True)

    def __str__(self):
        return self.name


class MenuMember(models.Model):
    name = models.CharField('Element', max_length=50)
    dir = models.BooleanField('Folder?')
    menu = models.ForeignKey(
        Menu,
        models.CASCADE,
        verbose_name='Belongs to this menu',
        related_name='members'
    )
    parent = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Will go into this folder',
        related_name='childrens',
        limit_choices_to={'dir': True}
    )
    url = models.URLField('URL', blank=True, null=True)

    def __str__(self):
        return self.name
