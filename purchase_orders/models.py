from django.utils.translation import gettext_lazy as _
from django.db import models
from user.models import User



class PurchaseOrder(models.Model):
    class PurchaseStatus(models.TextChoices):
        EM_VALIDACAO = 'EM_VALIDACAO', _('EM_VALIDACAO')
        APROVADO = 'APROVADO', _('APROVADO')

    code = models.IntegerField(unique=True, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    status = models.CharField(null=False, blank=False, choices=PurchaseStatus.choices,
                              default=PurchaseStatus.EM_VALIDACAO, max_length=15)
    user = models.ForeignKey(to=User, on_delete=models.deletion.CASCADE)
    date = models.DateTimeField(null=False, blank=False)

    class Meta:
        db_table = 'purchase_orders'