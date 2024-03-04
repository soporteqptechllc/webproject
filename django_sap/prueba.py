""" from datetime import datetime
#from time import gmtime, strftime
fechatxt = '20230825'
dato = datetime.strptime(fechatxt,"%Y%m%d")
print("date:", dato)
fecha = dato.strftime("%Y-%m-%d")
print("fecha:", fecha) """


# import os
# import django
# # project_name nombre del proyecto
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
# django.setup()
# from django.db.models import Q
# # from local apps
# from applications.api.models import MaestroDeMateriales, operaciones,em_sp
# #lista1 = em_sp.objects.filter(em__gt = 0).order_by("em").exclude(em = 3).exclude(em = 4)
# lista1 = em_sp.objects.filter(Q(em__gt = 0) & ~Q(em = 3) & ~Q(em = 4)).order_by("em")
# for i in lista1:
#     print(i.em,i.ID)

#lista2 = operaciones.objects.filter(idfabricacion = None,idlote=9).order_by('id')    
#for i in lista2:
#    print(i.id,i.hora)

# Maestro = MaestroDeMateriales.objects.filter(id = "SE-CRVERDE001").values()
# print(Maestro[0]['id'])
# for i in Maestro:
#     print(i)
#     print(i['id'])



# a = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
# b = ("H","E","L","L","O",6,7,8,9)
# c = [True,False,False,True,True,True,True,False,False]
# d = [100,200,300,400,500,600,700,800,900]
# result = zip(a,b,c,d)
# for x in result:
#  print(x)


# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using enumerate()
# for row, val in enumerate(list):
#     print (row, ",",val)

nombre = "Jose"
#print(f"mi nombre es {nombre}")
id = 86
urltxt ="{% url 'components_app:tables-edittables' "+str(id)+" %}" 
#print(urltxt)

for i in range(0,21):
    print(i)