#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
#from django.db import models
import os
import django
import datetime
import pandas as pd

# project_name nombre del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
django.setup()
from applications.api.models import operaciones, em_sp
#batchs=operaciones.objects.filter(receta_id="SE-CRAMERICANOVERDE0").update(receta_id='SE-CRAMERICANOVERDE003')
operaciones.objects.filter(receta_id="SE-CRAMERICANOVERDE003").update(receta_nombre='SEMIELABORADO CREMA AMERICANO LIMON')
#batchs = operaciones.objects.filter(receta_id='SE-CRAMERICANOVERDE003')




