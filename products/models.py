from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    categories = models.ForeignKey(Category, related_name='products', blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_enable = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title


# class File(models.Model):
#     FILE_AUDIO = 1
#     FILE_VIDEO = 2
#     FILE_PDF = 3
#     FILE_TYPES = (
#         (FILE_AUDIO, _('audio')),
#         (FILE_VIDEO, _('video')),
#         (FILE_PDF, _('pdf'))
#     )
#     DoesNotExist = None
#     objects = None
#     product = models.ForeignKey('Product', verbose_name=_('product'), related_name='files', on_delete=models.CASCADE)
#     title = models.CharField(_('title'), max_length=50)
#     file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES, default=2)
#     file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
#     is_enable = models.BooleanField(_('is enable'), default=True)
#     create_time = models.DateTimeField(_('create time'), auto_now_add=True)
#     updated_time = models.DateTimeField(_('update time'), auto_now=True)

#     class Meta:
#         db_table = _('files')
#         verbose_name = _('file')
#         verbose_name_plural = _('files')

#     def __str__(self):
#         return self.title
    