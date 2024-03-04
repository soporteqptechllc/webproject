#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
# C:\QPTECH\aalvarado\django_sap\VisualizacionReporteCremas.py
#from django.db import models
import os
import django
import datetime
import pandas as pd
# project_name nombre del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
django.setup()
from applications.api.models import operaciones, em_sp
from web.components.models import producciondiaria
# Function for clear 
def Limpiar():
    producciondiaria.objects.all().update(
        setpoint = 0,
        fecha = '',
        ho1 = '',
        op1  = 0,
        ho2 = '',
        op2 =  0,
        ho3 = '',
        op3 =  0,
        ho4 = '',
        op4 =  0,
        ho5 = '',
        op5 =  0,
        ho6 = '',
        op6 =  0,
        ho7 = '',
        op7 =  0,
        ho8 = '',
        op8 =  0,
        ho9 = '',
        op9 =  0,
        ho10 = '',
        op10 =  0,
        ho11 = '',
        op11 =  0,
        ho12 = '',
        op12 =  0,
        ho13 = '',
        op13 =  0,
        ho14 = '',
        op14 =  0,
        ho15 = '',
        op15 =  0,
        ho16 = '',
        op16 =  0,
        ho17 = '',
        op17 =  0,
        ho18 = '',
        op18 =  0,
        ho19 = '',
        op19 =  0,
        ho20 = '',
        op20 =  0,
        total =  0,
    )
def ActualizaReporte(fecha,id):       
    # Lee la base de datos de reportes de batchs 
    #print("fecha2 input: ",fecha)
    ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso','em16','humedad','ph']
    hor = ['hora']
    #fecha = '20230803'
    if operaciones.objects.filter(hora__contains = fecha,idlote__gt = 0,idlote = id).exists():

        viewOper = operaciones.objects.filter(hora__contains = fecha,idlote__gt = 0,idlote = id).order_by('id')
        listViewOper = list(viewOper.values())
        Limpiar()
        produccionDia = producciondiaria.objects.all().order_by('id')
        #print(len(produccionDia), len(listViewOper))
        #print(produccionDia)
        #print(listViewOper)
        romper = len(listViewOper)
        totalGeneral = 0
        k = 0

        totop1 = totop2 = totop3 = totop4 = totop5 = totop6 =0
        totop7 = totop8 = totop9 = totop10 = totop11 = totop12 =0
        totop13 = totop14 = totop15 = totop16 = totop17 = totop18 =0
        totop19 = totop20 =0
        

        for i in produccionDia:
            #print(i.Nombre)
            i.fecha = fecha
            x = 0
            if k<=16:
                #print(k)
                if romper >= 1 :
                    i.ho1 = listViewOper[0][hor[0]]
                    if listViewOper[0][ems[k]]:
                        i.op1 = round(listViewOper[0][ems[k]],1)
                        totop1 += listViewOper[0][ems[k]]
                        x += 1
                if romper >= 2 :
                    i.ho2 = listViewOper[1][hor[0]]
                    if listViewOper[1][ems[k]]:
                        i.op2 = round(listViewOper[1][ems[k]],1)
                        totop2 += listViewOper[1][ems[k]]
                        x += 1
                if romper >= 3 :
                    i.ho3 = listViewOper[2][hor[0]]
                    if listViewOper[2][ems[k]]:
                        i.op3 = round(listViewOper[2][ems[k]],1)
                        totop3 += listViewOper[2][ems[k]]
                        x += 1
                if romper >= 4 :
                    i.ho4 = listViewOper[3][hor[0]]
                    if listViewOper[3][ems[k]]:
                        i.op4 = round(listViewOper[3][ems[k]],1)
                        totop4 += listViewOper[3][ems[k]]
                        x += 1
                if romper >= 5 :
                    i.ho5 = listViewOper[4][hor[0]]
                    if listViewOper[4][ems[k]]:
                        i.op5 = round(listViewOper[4][ems[k]],1)
                        totop5 += listViewOper[4][ems[k]]
                        x += 1
                if romper >= 6 :
                    i.ho6 = listViewOper[5][hor[0]]
                    if listViewOper[5][ems[k]]:
                        i.op6 = round(listViewOper[5][ems[k]],1)
                        totop6 += listViewOper[5][ems[k]]
                        x += 1
                if romper >= 7 :
                    i.ho7 = listViewOper[6][hor[0]]
                    if listViewOper[6][ems[k]]:
                        i.op7 = round(listViewOper[6][ems[k]],1)
                        totop7 += listViewOper[6][ems[k]]
                        x += 1
                if romper >= 8 :
                    i.ho8 = listViewOper[7][hor[0]]
                    if listViewOper[7][ems[k]]:
                        i.op8 = round(listViewOper[7][ems[k]],1)
                        totop8 += listViewOper[7][ems[k]]
                        x += 1
                if romper >= 9 :
                    i.ho9 = listViewOper[8][hor[0]]
                    if listViewOper[8][ems[k]]:
                        i.op9 = round(listViewOper[8][ems[k]],1)
                        totop9 += listViewOper[8][ems[k]]
                        x += 1
                if romper >= 10 :
                    i.ho10 = listViewOper[9][hor[0]]
                    if listViewOper[9][ems[k]]:
                        i.op10 = round(listViewOper[9][ems[k]],1)
                        totop10 += listViewOper[9][ems[k]]
                        x += 1
                if romper == 11 :
                    i.ho11 = listViewOper[10][hor[0]]
                    if listViewOper[10][ems[k]]:
                        i.op11 = round(listViewOper[10][ems[k]],1)
                        totop11 += listViewOper[10][ems[k]]
                        x += 1
                if romper >= 12 :
                    i.ho12 = listViewOper[11][hor[0]]
                    if listViewOper[11][ems[k]]:
                        i.op12 = round(listViewOper[11][ems[k]],1)
                        totop12 += listViewOper[11][ems[k]]
                        x += 1
                if romper >= 13 :
                    i.ho13 = listViewOper[12][hor[0]]
                    if listViewOper[12][ems[k]]:
                        i.op13 = round(listViewOper[12][ems[k]],1)
                        totop13 += listViewOper[12][ems[k]]
                        x += 1
                if romper >= 14 :
                    i.ho14 = listViewOper[13][hor[0]]
                    if listViewOper[13][ems[k]]:
                        i.op14 = round(listViewOper[13][ems[k]],1)
                        totop14 += listViewOper[13][ems[k]]
                        x += 1
                if romper >= 15 :
                    i.ho15 = listViewOper[14][hor[0]]
                    if listViewOper[14][ems[k]]:
                        i.op15 = round(listViewOper[14][ems[k]],1)
                        totop15 += listViewOper[14][ems[k]]
                        x += 1
                if romper >= 16 :
                    i.ho16 = listViewOper[15][hor[0]]
                    if listViewOper[15][ems[k]]:
                        i.op16 = round(listViewOper[15][ems[k]],1)
                        totop16 += listViewOper[15][ems[k]]
                        x += 1
                if romper >= 17 :
                    i.ho17 = listViewOper[16][hor[0]]
                    if listViewOper[16][ems[k]]:
                        i.op17 = round(listViewOper[16][ems[k]],1)
                        totop17 += listViewOper[16][ems[k]]
                        x += 1
                if romper >= 18 :
                    i.ho18 = listViewOper[17][hor[0]]
                    if listViewOper[17][ems[k]]:
                        i.op18 = round(listViewOper[17][ems[k]],1)
                        totop18 += listViewOper[17][ems[k]]
                        x += 1
                if romper >= 19 :
                    i.ho19 = listViewOper[18][hor[0]]
                    if listViewOper[18][ems[k]]:
                        i.op19 = round(listViewOper[18][ems[k]],1)
                        totop19 += listViewOper[18][ems[k]]
                        x += 1
                if romper >= 20 :
                    i.ho20 = listViewOper[19][hor[0]]
                    if listViewOper[19][ems[k]]:
                        i.op20 = round(listViewOper[19][ems[k]],1)
                        totop20 += listViewOper[19][ems[k]]
                        x += 1

                if k < 15:
                    i.total = i.op1+i.op2+i.op3+i.op4+i.op5+i.op6+i.op7+i.op8+i.op9+i.op10+i.op11+i.op12+i.op13+i.op14+i.op15+i.op16+i.op17+i.op18+i.op19+i.op20
                if x > 0 and k > 14:
                    i.total = (i.op1+i.op2+i.op3+i.op4+i.op5+i.op6+i.op7+i.op8+i.op9+i.op10+i.op11+i.op12+i.op13+i.op14+i.op15+i.op16+i.op17+i.op18+i.op19+i.op20)/x
                
                #totalGeneral = totalGeneral + i.total
                totalGeneral = totop1+totop2+totop3+totop4+totop5+totop6+totop7+totop8+totop9+totop10+totop11+totop12+totop13+totop14+totop15+totop16+totop17+totop18+totop19+totop20
                

            i.save()
            #totop1 = totop2 = totop3 = totop4 = totop5 = totop6 =0
            #totop7 = totop8 = totop9 = totop10 = totop11 = totop12 =0
            #totop13 = totop14 = totop15 = totop16 = totop17 = totop18 =0
            #totop19 = totop20 =0
            k= k+1
            
        filaTotales = producciondiaria.objects.get(pk =15)
        filaTotales.op1 = round(totop1,1)
        filaTotales.op2 = round(totop2,1)
        filaTotales.op3 = round(totop3,1)
        filaTotales.op4 = round(totop4,1)
        filaTotales.op5 = round(totop5,1)
        filaTotales.op6 = round(totop6,1)
        filaTotales.op7 = round(totop7,1)
        filaTotales.op8 = round(totop8,1)
        filaTotales.op9 = round(totop9,1)
        filaTotales.op10 = round(totop10,1)
        filaTotales.op11 = round(totop11,1)
        filaTotales.op12 = round(totop12,1)
        filaTotales.op13 = round(totop13,1)
        filaTotales.op14 = round(totop14,1)
        filaTotales.op15 = round(totop15,1)
        filaTotales.op16 = round(totop16,1)
        filaTotales.op17 = round(totop17,1)
        filaTotales.op18 = round(totop18,1)
        filaTotales.op19 = round(totop19,1)
        filaTotales.op20 = round(totop20,1)
        filaTotales.total = round(totalGeneral,1)

        filaTotales.save()
    else:
        Limpiar()
        filaTotales = producciondiaria.objects.get(pk =15)
        filaTotales.op1 = 0
        filaTotales.op2 = 0
        filaTotales.op3 = 0
        filaTotales.op4 = 0
        filaTotales.op5 = 0
        filaTotales.op6 = 0
        filaTotales.op7 = 0
        filaTotales.op8 = 0
        filaTotales.op9 = 0
        filaTotales.op10 = 0
        filaTotales.op11 = 0
        filaTotales.op12 = 0
        filaTotales.op13 = 0
        filaTotales.op14 = 0
        filaTotales.op15 = 0
        filaTotales.op16 = 0
        filaTotales.op17 = 0
        filaTotales.op18 = 0
        filaTotales.op19 = 0
        filaTotales.op20 = 0
        filaTotales.total = 0

        filaTotales.save()

# ****************************************************
# ****************************************************     
# funcion para listar operaciones de prod. en una tabla
def ListarDataTabla(idlote):        
        # ********************************************    
        # Inicio de la creacion de las lista que van
        # en el cuerpo de la tabla
        # *********************************************               
        col1 = list()
        col2 = list()
        col3 = list()
        col4 = list()

        ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','em16','humedad','ph']
        k = 0
        totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0.0
        totem15 = totem14 = tothum = totph = totrep = 0.0
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        #print(nolista1)
        #print(lista1)
        #print(lista2)
        x = 0
        for i in lista1:
            if x == 14:
                col1.append('')
                col2.append("TOTALES")
                col3.append("SUMATORIA")
                col4.append(0.0)
                col1.append(x)
                col2.append(i.ID)
                col3.append(i.Ingrediente)
                col4.append(i.SP)
            else:
                col1.append(x)
                col2.append(i.ID)
                col3.append(i.Ingrediente)
                col4.append(i.SP)
            x += 1

        if lista2:
                x = 1
                y = 0
                z = 0
                total = 0.0
                totaly = 0.0
                totalz = 0.0
                
                colt = list()

                for i in lista2:
                    
                    totem1 += i.em1
                    totem2 += i.em2
                    totem3 += i.em3
                    totem4 += i.em4
                    totem5 += i.em5
                    totem6 += i.em6
                    totem7 += i.em7
                    totem8 += i.em8
                    totem9 += i.em9
                    totem10 += i.em10
                    totem11 += i.em11
                    totem14 += i.em14
                    totem15 += i.em15
                    if i.humedad and i.humedad > 0:
                        tothum += i.humedad
                        y += 1
                    if i.ph and i.ph > 0:
                        totph += i.ph
                        z += 1
                    if i.reproceso and i.reproceso > 0:
                        totrep += i.reproceso

                    if x == 1:
                        col5 = list()
                        col5.append(round(i.em1,1))
                        col5.append(round(i.em2,1))
                        col5.append(round(i.em3,1))
                        col5.append(round(i.em4,1))
                        col5.append(round(i.em5,1))
                        col5.append(round(i.em6,1))
                        col5.append(round(i.em7,1))
                        col5.append(round(i.em8,1))
                        col5.append(round(i.em9,1))
                        col5.append(round(i.em10,1))
                        col5.append(round(i.em11,1))
                        col5.append(round(i.em15,1))
                        col5.append(round(i.em14,1))
                        if i.reproceso:
                            col5.append(round(i.reproceso,1))
                        else:
                            col5.append(0.0)
                        col5.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col5.append(round(i.humedad,1))
                        else:
                            col5.append(0.0)
                        if i.ph:
                            col5.append(round(i.ph,1))
                        else:
                            col5.append(0.0)
                    if x == 2:
                        col6 = list()
                        col6.append(round(i.em1,1))
                        col6.append(round(i.em2,1))
                        col6.append(round(i.em3,1))
                        col6.append(round(i.em4,1))
                        col6.append(round(i.em5,1))
                        col6.append(round(i.em6,1))
                        col6.append(round(i.em7,1))
                        col6.append(round(i.em8,1))
                        col6.append(round(i.em9,1))
                        col6.append(round(i.em10,1))
                        col6.append(round(i.em11,1))
                        col6.append(round(i.em15,1))
                        col6.append(round(i.em14,1))
                        if i.reproceso:
                            col6.append(round(i.reproceso,1))
                        else:
                            col6.append(0.0)
                        col6.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col6.append(round(i.humedad,1))
                        else:
                            col6.append(0.0)
                        if i.ph:
                            col6.append(round(i.ph,1))
                        else:
                            col6.append(0.0)
                    if x == 3:
                        col7 = list()
                        col7.append(round(i.em1,1))
                        col7.append(round(i.em2,1))
                        col7.append(round(i.em3,1))
                        col7.append(round(i.em4,1))
                        col7.append(round(i.em5,1))
                        col7.append(round(i.em6,1))
                        col7.append(round(i.em7,1))
                        col7.append(round(i.em8,1))
                        col7.append(round(i.em9,1))
                        col7.append(round(i.em10,1))
                        col7.append(round(i.em11,1))
                        col7.append(round(i.em15,1))
                        col7.append(round(i.em14,1))
                        if i.reproceso:
                            col7.append(round(i.reproceso,1))
                        else:
                            col7.append(0.0)
                        col7.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col7.append(round(i.humedad,1))
                        else:
                            col7.append(0.0)
                        if i.ph:
                            col7.append(round(i.ph,1))
                        else:
                            col7.append(0.0)
                    if x == 4:
                        col8 = list()
                        col8.append(round(i.em1,1))
                        col8.append(round(i.em2,1))
                        col8.append(round(i.em3,1))
                        col8.append(round(i.em4,1))
                        col8.append(round(i.em5,1))
                        col8.append(round(i.em6,1))
                        col8.append(round(i.em7,1))
                        col8.append(round(i.em8,1))
                        col8.append(round(i.em9,1))
                        col8.append(round(i.em10,1))
                        col8.append(round(i.em11,1))
                        col8.append(round(i.em15,1))
                        col8.append(round(i.em14,1))
                        if i.reproceso:
                            col8.append(round(i.reproceso,1))
                        else:
                            col8.append(0.0)
                        col8.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col8.append(round(i.humedad,1))
                        else:
                            col8.append(0.0)
                        if i.ph:
                            col8.append(round(i.ph,1))
                        else:
                            col8.append(0.0)
                    if x == 5:
                        col9 = list()
                        col9.append(round(i.em1,1))
                        col9.append(round(i.em2,1))
                        col9.append(round(i.em3,1))
                        col9.append(round(i.em4,1))
                        col9.append(round(i.em5,1))
                        col9.append(round(i.em6,1))
                        col9.append(round(i.em7,1))
                        col9.append(round(i.em8,1))
                        col9.append(round(i.em9,1))
                        col9.append(round(i.em10,1))
                        col9.append(round(i.em11,1))
                        col9.append(round(i.em15,1))
                        col9.append(round(i.em14,1))
                        if i.reproceso:
                            col9.append(round(i.reproceso,1))
                        else:
                            col9.append(0.0)
                        col9.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col9.append(round(i.humedad,1))
                        else:
                            col9.append(0.0)
                        if i.ph:
                            col9.append(round(i.ph,1))
                        else:
                            col9.append(0.0)
                    if x == 6:
                        col10 = list()
                        col10.append(round(i.em1,1))
                        col10.append(round(i.em2,1))
                        col10.append(round(i.em3,1))
                        col10.append(round(i.em4,1))
                        col10.append(round(i.em5,1))
                        col10.append(round(i.em6,1))
                        col10.append(round(i.em7,1))
                        col10.append(round(i.em8,1))
                        col10.append(round(i.em9,1))
                        col10.append(round(i.em10,1))
                        col10.append(round(i.em11,1))
                        col10.append(round(i.em15,1))
                        col10.append(round(i.em14,1))
                        if i.reproceso:
                            col10.append(round(i.reproceso,1))
                        else:
                            col10.append(0.0)
                        col10.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col10.append(round(i.humedad,1))
                        else:
                            col10.append(0.0)
                        if i.ph:
                            col10.append(round(i.ph,1))
                        else:
                            col10.append(0.0)
                    if x == 7:
                        col11 = list()
                        col11.append(round(i.em1,1))
                        col11.append(round(i.em2,1))
                        col11.append(round(i.em3,1))
                        col11.append(round(i.em4,1))
                        col11.append(round(i.em5,1))
                        col11.append(round(i.em6,1))
                        col11.append(round(i.em7,1))
                        col11.append(round(i.em8,1))
                        col11.append(round(i.em9,1))
                        col11.append(round(i.em10,1))
                        col11.append(round(i.em11,1))
                        col11.append(round(i.em15,1))
                        col11.append(round(i.em14,1))
                        if i.reproceso:
                            col11.append(round(i.reproceso,1))
                        else:
                            col11.append(0.0)
                        col11.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col11.append(round(i.humedad,1))
                        else:
                            col11.append(0.0)
                        if i.ph:
                            col11.append(round(i.ph,1))
                        else:
                            col11.append(0.0)
                    if x == 8:
                        col12 = list()
                        col12.append(round(i.em1,1))
                        col12.append(round(i.em2,1))
                        col12.append(round(i.em3,1))
                        col12.append(round(i.em4,1))
                        col12.append(round(i.em5,1))
                        col12.append(round(i.em6,1))
                        col12.append(round(i.em7,1))
                        col12.append(round(i.em8,1))
                        col12.append(round(i.em9,1))
                        col12.append(round(i.em10,1))
                        col12.append(round(i.em11,1))
                        col12.append(round(i.em15,1))
                        col12.append(round(i.em14,1))
                        if i.reproceso:
                            col12.append(round(i.reproceso,1))
                        else:
                            col12.append(0.0)
                        col12.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col12.append(round(i.humedad,1))
                        else:
                            col12.append(0.0)
                        if i.ph:
                            col12.append(round(i.ph,1))
                        else:
                            col12.append(0.0)
                    if x == 9:
                        col13 = list()
                        col13.append(round(i.em1,1))
                        col13.append(round(i.em2,1))
                        col13.append(round(i.em3,1))
                        col13.append(round(i.em4,1))
                        col13.append(round(i.em5,1))
                        col13.append(round(i.em6,1))
                        col13.append(round(i.em7,1))
                        col13.append(round(i.em8,1))
                        col13.append(round(i.em9,1))
                        col13.append(round(i.em10,1))
                        col13.append(round(i.em11,1))
                        col13.append(round(i.em15,1))
                        col13.append(round(i.em14,1))
                        if i.reproceso:
                            col13.append(round(i.reproceso,1))
                        else:
                            col13.append(0.0)
                        col13.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col13.append(round(i.humedad,1))
                        else:
                            col13.append(0.0)
                        if i.ph:
                            col13.append(round(i.ph,1))
                        else:
                            col13.append(0.0)
                    if x == 10:
                        col14 = list()
                        col14.append(round(i.em1,1))
                        col14.append(round(i.em2,1))
                        col14.append(round(i.em3,1))
                        col14.append(round(i.em4,1))
                        col14.append(round(i.em5,1))
                        col14.append(round(i.em6,1))
                        col14.append(round(i.em7,1))
                        col14.append(round(i.em8,1))
                        col14.append(round(i.em9,1))
                        col14.append(round(i.em10,1))
                        col14.append(round(i.em11,1))
                        col14.append(round(i.em15,1))
                        col14.append(round(i.em14,1))
                        if i.reproceso:
                            col14.append(round(i.reproceso,1))
                        else:
                            col14.append(0.0)
                        col14.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col14.append(round(i.humedad,1))
                        else:
                            col14.append(0.0)
                        if i.ph:
                            col14.append(round(i.ph,1))
                        else:
                            col14.append(0.0)
                    if x == 11:
                        col15 = list()
                        col15.append(round(i.em1,1))
                        col15.append(round(i.em2,1))
                        col15.append(round(i.em3,1))
                        col15.append(round(i.em4,1))
                        col15.append(round(i.em5,1))
                        col15.append(round(i.em6,1))
                        col15.append(round(i.em7,1))
                        col15.append(round(i.em8,1))
                        col15.append(round(i.em9,1))
                        col15.append(round(i.em10,1))
                        col15.append(round(i.em11,1))
                        col15.append(round(i.em15,1))
                        col15.append(round(i.em14,1))
                        if i.reproceso:
                            col15.append(round(i.reproceso,1))
                        else:
                            col15.append(0.0)
                        col15.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col15.append(round(i.humedad,1))
                        else:
                            col15.append(0.0)
                        if i.ph:
                            col15.append(round(i.ph,1))
                        else:
                            col15.append(0.0)
                    if x == 12:
                        col16 = list()
                        col16.append(round(i.em1,1))
                        col16.append(round(i.em2,1))
                        col16.append(round(i.em3,1))
                        col16.append(round(i.em4,1))
                        col16.append(round(i.em5,1))
                        col16.append(round(i.em6,1))
                        col16.append(round(i.em7,1))
                        col16.append(round(i.em8,1))
                        col16.append(round(i.em9,1))
                        col16.append(round(i.em10,1))
                        col16.append(round(i.em11,1))
                        col16.append(round(i.em15,1))
                        col16.append(round(i.em14,1))
                        if i.reproceso:
                            col16.append(round(i.reproceso,1))
                        else:
                            col16.append(0.0)
                        col16.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col16.append(round(i.humedad,1))
                        else:
                            col16.append(0.0)
                        if i.ph:
                            col16.append(round(i.ph,1))
                        else:
                            col16.append(0.0)
                    if x == 13:
                        col17 = list()
                        col17.append(round(i.em1,1))
                        col17.append(round(i.em2,1))
                        col17.append(round(i.em3,1))
                        col17.append(round(i.em4,1))
                        col17.append(round(i.em5,1))
                        col17.append(round(i.em6,1))
                        col17.append(round(i.em7,1))
                        col17.append(round(i.em8,1))
                        col17.append(round(i.em9,1))
                        col17.append(round(i.em10,1))
                        col17.append(round(i.em11,1))
                        col17.append(round(i.em15,1))
                        col17.append(round(i.em14,1))
                        if i.reproceso:
                            col17.append(round(i.reproceso,1))
                        else:
                            col17.append(0.0)
                        col17.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col17.append(round(i.humedad,1))
                        else:
                            col17.append(0.0)
                        if i.ph:
                            col17.append(round(i.ph,1))
                        else:
                            col17.append(0.0)
                    if x == 14:
                        col18 = list()
                        col18.append(round(i.em1,1))
                        col18.append(round(i.em2,1))
                        col18.append(round(i.em3,1))
                        col18.append(round(i.em4,1))
                        col18.append(round(i.em5,1))
                        col18.append(round(i.em6,1))
                        col18.append(round(i.em7,1))
                        col18.append(round(i.em8,1))
                        col18.append(round(i.em9,1))
                        col18.append(round(i.em10,1))
                        col18.append(round(i.em11,1))
                        col18.append(round(i.em15,1))
                        col18.append(round(i.em14,1))
                        if i.reproceso:
                            col18.append(round(i.reproceso,1))
                        else:
                            col18.append(0.0)
                        col18.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col18.append(round(i.humedad,1))
                        else:
                            col18.append(0.0)
                        if i.ph:
                            col18.append(round(i.ph,1))
                        else:
                            col18.append(0.0)
                    if x == 15:
                        col19 = list()
                        col19.append(round(i.em1,1))
                        col19.append(round(i.em2,1))
                        col19.append(round(i.em3,1))
                        col19.append(round(i.em4,1))
                        col19.append(round(i.em5,1))
                        col19.append(round(i.em6,1))
                        col19.append(round(i.em7,1))
                        col19.append(round(i.em8,1))
                        col19.append(round(i.em9,1))
                        col19.append(round(i.em10,1))
                        col19.append(round(i.em11,1))
                        col19.append(round(i.em15,1))
                        col19.append(round(i.em14,1))
                        if i.reproceso:
                            col19.append(round(i.reproceso,1))
                        else:
                            col19.append(0.0)
                        col19.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col19.append(round(i.humedad,1))
                        else:
                            col19.append(0.0)
                        if i.ph:
                            col19.append(round(i.ph,1))
                        else:
                            col19.append(0.0)
                    if x == 16:
                        col20 = list()
                        col20.append(round(i.em1,1))
                        col20.append(round(i.em2,1))
                        col20.append(round(i.em3,1))
                        col20.append(round(i.em4,1))
                        col20.append(round(i.em5,1))
                        col20.append(round(i.em6,1))
                        col20.append(round(i.em7,1))
                        col20.append(round(i.em8,1))
                        col20.append(round(i.em9,1))
                        col20.append(round(i.em10,1))
                        col20.append(round(i.em11,1))
                        col20.append(round(i.em15,1))
                        col20.append(round(i.em14,1))
                        if i.reproceso:
                            col20.append(round(i.reproceso,1))
                        else:
                            col20.append(0.0)
                        col20.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col20.append(round(i.humedad,1))
                        else:
                            col20.append(0.0)
                        if i.ph:
                            col20.append(round(i.ph,1))
                        else:
                            col20.append(0.0)
                    if x == 17:
                        col21 = list()
                        col21.append(round(i.em1,1))
                        col21.append(round(i.em2,1))
                        col21.append(round(i.em3,1))
                        col21.append(round(i.em4,1))
                        col21.append(round(i.em5,1))
                        col21.append(round(i.em6,1))
                        col21.append(round(i.em7,1))
                        col21.append(round(i.em8,1))
                        col21.append(round(i.em9,1))
                        col21.append(round(i.em10,1))
                        col21.append(round(i.em11,1))
                        col21.append(round(i.em15,1))
                        col21.append(round(i.em14,1))
                        if i.reproceso:
                            col21.append(round(i.reproceso,1))
                        else:
                            col21.append(0.0)
                        col21.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col21.append(round(i.humedad,1))
                        else:
                            col21.append(0.0)
                        if i.ph:
                            col21.append(round(i.ph,1))
                        else:
                            col21.append(0.0)
                    if x == 18:
                        col22 = list()
                        col22.append(round(i.em1,1))
                        col22.append(round(i.em2,1))
                        col22.append(round(i.em3,1))
                        col22.append(round(i.em4,1))
                        col22.append(round(i.em5,1))
                        col22.append(round(i.em6,1))
                        col22.append(round(i.em7,1))
                        col22.append(round(i.em8,1))
                        col22.append(round(i.em9,1))
                        col22.append(round(i.em10,1))
                        col22.append(round(i.em11,1))
                        col22.append(round(i.em15,1))
                        col22.append(round(i.em14,1))
                        if i.reproceso:
                            col22.append(round(i.reproceso,1))
                        else:
                            col22.append(0.0)
                        col22.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col22.append(round(i.humedad,1))
                        else:
                            col22.append(0.0)
                        if i.ph:
                            col22.append(round(i.ph,1))
                        else:
                            col22.append(0.0)
                    if x == 19:
                        col23 = list()
                        col23.append(round(i.em1,1))
                        col23.append(round(i.em2,1))
                        col23.append(round(i.em3,1))
                        col23.append(round(i.em4,1))
                        col23.append(round(i.em5,1))
                        col23.append(round(i.em6,1))
                        col23.append(round(i.em7,1))
                        col23.append(round(i.em8,1))
                        col23.append(round(i.em9,1))
                        col23.append(round(i.em10,1))
                        col23.append(round(i.em11,1))
                        col23.append(round(i.em15,1))
                        col23.append(round(i.em14,1))
                        if i.reproceso:
                            col23.append(round(i.reproceso,1))
                        else:
                            col23.append(0.0)
                        col23.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col23.append(round(i.humedad,1))
                        else:
                            col23.append(0.0)
                        if i.ph:
                            col23.append(round(i.ph,1))
                        else:
                            col23.append(0.0)
                    if x == 20:
                        col24 = list()
                        col24.append(round(i.em1,1))
                        col24.append(round(i.em2,1))
                        col24.append(round(i.em3,1))
                        col24.append(round(i.em4,1))
                        col24.append(round(i.em5,1))
                        col24.append(round(i.em6,1))
                        col24.append(round(i.em7,1))
                        col24.append(round(i.em8,1))
                        col24.append(round(i.em9,1))
                        col24.append(round(i.em10,1))
                        col24.append(round(i.em11,1))
                        col24.append(round(i.em15,1))
                        col24.append(round(i.em14,1))
                        if i.reproceso:
                            col24.append(round(i.reproceso,1))
                        else:
                            col24.append(0.0)
                        col24.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col24.append(round(i.humedad,1))
                        else:
                            col24.append(0.0)
                        if i.ph:
                            col24.append(round(i.ph,1))
                        else:
                            col24.append(0.0)

                    x += 1

                colt.append(round(totem1,1))
                colt.append(round(totem2,1))
                colt.append(round(totem3,1))
                colt.append(round(totem4,1))
                colt.append(round(totem5,1))
                colt.append(round(totem6,1))
                colt.append(round(totem7,1))
                colt.append(round(totem8,1))
                colt.append(round(totem9,1))
                colt.append(round(totem10,1))
                colt.append(round(totem11,1))
                colt.append(round(totem15,1))
                colt.append(round(totem14,1))
                colt.append(round(totrep,1))
                total = totem1+totem2+totem3+totem4+totem5+totem6+totem7+totem8+totem9+totem10+totem11+totem14+totem15+totrep                
                colt.append(round(total,1))
                if y > 0:
                    totaly = tothum/y
                else:
                    totaly = 0.0
                if z > 0:
                    totalz = totph/z
                else:
                    totalz = 0.0
                colt.append(round(totaly,1))
                colt.append(round(totalz,1))
        else:
            nolista2 = 0

        if nolista2 == 0:
            #print("No hay datos")
            resultado = zip(col1,col2,col3,col4)
        elif nolista2 == 1:    
            resultado = zip(col1,col2,col3,col4,col5,colt)
        elif nolista2 == 2:   
            resultado = zip(col1,col2,col3,col4,col5,col6,colt)
        elif nolista2 == 3:   
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,colt)
        elif nolista2 == 4:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,colt)
        elif nolista2 == 5:    
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,colt)
        elif nolista2 == 6:          
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,colt)
        elif nolista2 == 7:        
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,colt)
        elif nolista2 == 8:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,colt)        
        elif nolista2 == 9:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,colt)
        elif nolista2 == 10:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,colt)
        elif nolista2 == 11:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,colt)
        elif nolista2 == 12:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,colt)            
        elif nolista2 == 13:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,colt)
        elif nolista2 == 14:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,colt)
        elif nolista2 == 15:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,colt)
        elif nolista2 == 16:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,colt)
        elif nolista2 == 17:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,colt)
        elif nolista2 == 18:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,colt)
        elif nolista2 == 19:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,colt)
        elif nolista2 >= 20:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,colt)

        return resultado                                                                                     
        # ********************************************    
        # Fin de la creacion de las lista del curpo de
        # la tabla
        # ********************************************  

# ****************************************************
# ****************************************************     
# funcion para listar operaciones de prod. en una tabla
def ListarDataTabla2(idlote):        
        # ********************************************    
        # Inicio de la creacion de las lista que van
        # en el cuerpo de la tabla
        # *********************************************               
        col1 = list()
        col2 = list()
        col3 = list()
        col4 = list()

        ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','em16','humedad','ph']
        k = 0
        totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0.0
        totem15 = totem14 = tothum = totph = totrep = 0.0
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        #print(nolista1)
        #print(lista1)
        #print(lista2)
        x = 0
        for i in lista1:
            if x == 14:
                col1.append('')
                col2.append("TOTALES")
                col3.append("SUMATORIA")
                col4.append(0.0)
                col1.append(x)
                col2.append(i.ID)
                col3.append(i.Ingrediente)
                col4.append(i.SP)
            else:
                col1.append(x)
                col2.append(i.ID)
                col3.append(i.Ingrediente)
                col4.append(i.SP)
            x += 1

        if lista2:
                x = 1
                y = 0
                z = 0
                total = 0.0
                totaly = 0.0
                totalz = 0.0
                
                colt = list()

                for i in lista2:

                    totem1 += i.em1
                    totem2 += i.em2
                    totem3 += i.em3
                    totem4 += i.em4
                    totem5 += i.em5
                    totem6 += i.em6
                    totem7 += i.em7
                    totem8 += i.em8
                    totem9 += i.em9
                    totem10 += i.em10
                    totem11 += i.em11
                    totem14 += i.em14
                    totem15 += i.em15
                    if i.humedad and i.humedad > 0:
                        tothum += i.humedad
                        y += 1
                    if i.ph and i.ph > 0:
                        totph += i.ph
                        z += 1
                    if i.reproceso and i.reproceso > 0:
                        totrep += i.reproceso
                    if x == 1:
                        col5 = list()
                        col5.append(round(i.em1,1))
                        col5.append(round(i.em2,1))
                        col5.append(round(i.em3,1))
                        col5.append(round(i.em4,1))
                        col5.append(round(i.em5,1))
                        col5.append(round(i.em6,1))
                        col5.append(round(i.em7,1))
                        col5.append(round(i.em8,1))
                        col5.append(round(i.em9,1))
                        col5.append(round(i.em10,1))
                        col5.append(round(i.em11,1))
                        col5.append(round(i.em15,1))
                        col5.append(round(i.em14,1))
                        if i.reproceso:
                            col5.append(round(i.reproceso,1))
                        else:
                            col5.append(0.0)
                        col5.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col5.append(round(i.humedad,1))
                        else:
                            col5.append(0.0)
                        if i.ph:
                            col5.append(round(i.ph,1))
                        else:
                            col5.append(0.0)
                    if x == 2:
                        col6 = list()
                        col6.append(round(i.em1,1))
                        col6.append(round(i.em2,1))
                        col6.append(round(i.em3,1))
                        col6.append(round(i.em4,1))
                        col6.append(round(i.em5,1))
                        col6.append(round(i.em6,1))
                        col6.append(round(i.em7,1))
                        col6.append(round(i.em8,1))
                        col6.append(round(i.em9,1))
                        col6.append(round(i.em10,1))
                        col6.append(round(i.em11,1))
                        col6.append(round(i.em15,1))
                        col6.append(round(i.em14,1))
                        if i.reproceso:
                            col6.append(round(i.reproceso,1))
                        else:
                            col6.append(0.0)
                        col6.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col6.append(round(i.humedad,1))
                        else:
                            col6.append(0.0)
                        if i.ph:
                            col6.append(round(i.ph,1))
                        else:
                            col6.append(0.0)
                    if x == 3:
                        col7 = list()
                        col7.append(round(i.em1,1))
                        col7.append(round(i.em2,1))
                        col7.append(round(i.em3,1))
                        col7.append(round(i.em4,1))
                        col7.append(round(i.em5,1))
                        col7.append(round(i.em6,1))
                        col7.append(round(i.em7,1))
                        col7.append(round(i.em8,1))
                        col7.append(round(i.em9,1))
                        col7.append(round(i.em10,1))
                        col7.append(round(i.em11,1))
                        col7.append(round(i.em15,1))
                        col7.append(round(i.em14,1))
                        if i.reproceso:
                            col7.append(round(i.reproceso,1))
                        else:
                            col7.append(0.0)
                        col7.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col7.append(round(i.humedad,1))
                        else:
                            col7.append(0.0)
                        if i.ph:
                            col7.append(round(i.ph,1))
                        else:
                            col7.append(0.0)
                    if x == 4:
                        col8 = list()
                        col8.append(round(i.em1,1))
                        col8.append(round(i.em2,1))
                        col8.append(round(i.em3,1))
                        col8.append(round(i.em4,1))
                        col8.append(round(i.em5,1))
                        col8.append(round(i.em6,1))
                        col8.append(round(i.em7,1))
                        col8.append(round(i.em8,1))
                        col8.append(round(i.em9,1))
                        col8.append(round(i.em10,1))
                        col8.append(round(i.em11,1))
                        col8.append(round(i.em15,1))
                        col8.append(round(i.em14,1))
                        if i.reproceso:
                            col8.append(round(i.reproceso,1))
                        else:
                            col8.append(0.0)
                        col8.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col8.append(round(i.humedad,1))
                        else:
                            col8.append(0.0)
                        if i.ph:
                            col8.append(round(i.ph,1))
                        else:
                            col8.append(0.0)
                    if x == 5:
                        col9 = list()
                        col9.append(round(i.em1,1))
                        col9.append(round(i.em2,1))
                        col9.append(round(i.em3,1))
                        col9.append(round(i.em4,1))
                        col9.append(round(i.em5,1))
                        col9.append(round(i.em6,1))
                        col9.append(round(i.em7,1))
                        col9.append(round(i.em8,1))
                        col9.append(round(i.em9,1))
                        col9.append(round(i.em10,1))
                        col9.append(round(i.em11,1))
                        col9.append(round(i.em15,1))
                        col9.append(round(i.em14,1))
                        if i.reproceso:
                            col9.append(round(i.reproceso,1))
                        else:
                            col9.append(0.0)
                        col9.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col9.append(round(i.humedad,1))
                        else:
                            col9.append(0.0)
                        if i.ph:
                            col9.append(round(i.ph,1))
                        else:
                            col9.append(0.0)
                    if x == 6:
                        col10 = list()
                        col10.append(round(i.em1,1))
                        col10.append(round(i.em2,1))
                        col10.append(round(i.em3,1))
                        col10.append(round(i.em4,1))
                        col10.append(round(i.em5,1))
                        col10.append(round(i.em6,1))
                        col10.append(round(i.em7,1))
                        col10.append(round(i.em8,1))
                        col10.append(round(i.em9,1))
                        col10.append(round(i.em10,1))
                        col10.append(round(i.em11,1))
                        col10.append(round(i.em15,1))
                        col10.append(round(i.em14,1))
                        if i.reproceso:
                            col10.append(round(i.reproceso,1))
                        else:
                            col10.append(0.0)
                        col10.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col10.append(round(i.humedad,1))
                        else:
                            col10.append(0.0)
                        if i.ph:
                            col10.append(round(i.ph,1))
                        else:
                            col10.append(0.0)
                    if x == 7:
                        col11 = list()
                        col11.append(round(i.em1,1))
                        col11.append(round(i.em2,1))
                        col11.append(round(i.em3,1))
                        col11.append(round(i.em4,1))
                        col11.append(round(i.em5,1))
                        col11.append(round(i.em6,1))
                        col11.append(round(i.em7,1))
                        col11.append(round(i.em8,1))
                        col11.append(round(i.em9,1))
                        col11.append(round(i.em10,1))
                        col11.append(round(i.em11,1))
                        col11.append(round(i.em15,1))
                        col11.append(round(i.em14,1))
                        if i.reproceso:
                            col11.append(round(i.reproceso,1))
                        else:
                            col11.append(0.0)
                        col11.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col11.append(round(i.humedad,1))
                        else:
                            col11.append(0.0)
                        if i.ph:
                            col11.append(round(i.ph,1))
                        else:
                            col11.append(0.0)
                    if x == 8:
                        col12 = list()
                        col12.append(round(i.em1,1))
                        col12.append(round(i.em2,1))
                        col12.append(round(i.em3,1))
                        col12.append(round(i.em4,1))
                        col12.append(round(i.em5,1))
                        col12.append(round(i.em6,1))
                        col12.append(round(i.em7,1))
                        col12.append(round(i.em8,1))
                        col12.append(round(i.em9,1))
                        col12.append(round(i.em10,1))
                        col12.append(round(i.em11,1))
                        col12.append(round(i.em15,1))
                        col12.append(round(i.em14,1))
                        if i.reproceso:
                            col12.append(round(i.reproceso,1))
                        else:
                            col12.append(0.0)
                        col12.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col12.append(round(i.humedad,1))
                        else:
                            col12.append(0.0)
                        if i.ph:
                            col12.append(round(i.ph,1))
                        else:
                            col12.append(0.0)
                    if x == 9:
                        col13 = list()
                        col13.append(round(i.em1,1))
                        col13.append(round(i.em2,1))
                        col13.append(round(i.em3,1))
                        col13.append(round(i.em4,1))
                        col13.append(round(i.em5,1))
                        col13.append(round(i.em6,1))
                        col13.append(round(i.em7,1))
                        col13.append(round(i.em8,1))
                        col13.append(round(i.em9,1))
                        col13.append(round(i.em10,1))
                        col13.append(round(i.em11,1))
                        col13.append(round(i.em15,1))
                        col13.append(round(i.em14,1))
                        if i.reproceso:
                            col13.append(round(i.reproceso,1))
                        else:
                            col13.append(0.0)
                        col13.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col13.append(round(i.humedad,1))
                        else:
                            col13.append(0.0)
                        if i.ph:
                            col13.append(round(i.ph,1))
                        else:
                            col13.append(0.0)
                    if x == 10:
                        col14 = list()
                        col14.append(round(i.em1,1))
                        col14.append(round(i.em2,1))
                        col14.append(round(i.em3,1))
                        col14.append(round(i.em4,1))
                        col14.append(round(i.em5,1))
                        col14.append(round(i.em6,1))
                        col14.append(round(i.em7,1))
                        col14.append(round(i.em8,1))
                        col14.append(round(i.em9,1))
                        col14.append(round(i.em10,1))
                        col14.append(round(i.em11,1))
                        col14.append(round(i.em15,1))
                        col14.append(round(i.em14,1))
                        if i.reproceso:
                            col14.append(round(i.reproceso,1))
                        else:
                            col14.append(0.0)
                        col14.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col14.append(round(i.humedad,1))
                        else:
                            col14.append(0.0)
                        if i.ph:
                            col14.append(round(i.ph,1))
                        else:
                            col14.append(0.0)
                    if x == 11:
                        col15 = list()
                        col15.append(round(i.em1,1))
                        col15.append(round(i.em2,1))
                        col15.append(round(i.em3,1))
                        col15.append(round(i.em4,1))
                        col15.append(round(i.em5,1))
                        col15.append(round(i.em6,1))
                        col15.append(round(i.em7,1))
                        col15.append(round(i.em8,1))
                        col15.append(round(i.em9,1))
                        col15.append(round(i.em10,1))
                        col15.append(round(i.em11,1))
                        col15.append(round(i.em15,1))
                        col15.append(round(i.em14,1))
                        if i.reproceso:
                            col15.append(round(i.reproceso,1))
                        else:
                            col15.append(0.0)
                        col15.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col15.append(round(i.humedad,1))
                        else:
                            col15.append(0.0)
                        if i.ph:
                            col15.append(round(i.ph,1))
                        else:
                            col15.append(0.0)
                    if x == 12:
                        col16 = list()
                        col16.append(round(i.em1,1))
                        col16.append(round(i.em2,1))
                        col16.append(round(i.em3,1))
                        col16.append(round(i.em4,1))
                        col16.append(round(i.em5,1))
                        col16.append(round(i.em6,1))
                        col16.append(round(i.em7,1))
                        col16.append(round(i.em8,1))
                        col16.append(round(i.em9,1))
                        col16.append(round(i.em10,1))
                        col16.append(round(i.em11,1))
                        col16.append(round(i.em15,1))
                        col16.append(round(i.em14,1))
                        if i.reproceso:
                            col16.append(round(i.reproceso,1))
                        else:
                            col16.append(0.0)
                        col16.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col16.append(round(i.humedad,1))
                        else:
                            col16.append(0.0)
                        if i.ph:
                            col16.append(round(i.ph,1))
                        else:
                            col16.append(0.0)
                    if x == 13:
                        col17 = list()
                        col17.append(round(i.em1,1))
                        col17.append(round(i.em2,1))
                        col17.append(round(i.em3,1))
                        col17.append(round(i.em4,1))
                        col17.append(round(i.em5,1))
                        col17.append(round(i.em6,1))
                        col17.append(round(i.em7,1))
                        col17.append(round(i.em8,1))
                        col17.append(round(i.em9,1))
                        col17.append(round(i.em10,1))
                        col17.append(round(i.em11,1))
                        col17.append(round(i.em15,1))
                        col17.append(round(i.em14,1))
                        if i.reproceso:
                            col17.append(round(i.reproceso,1))
                        else:
                            col17.append(0.0)
                        col17.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col17.append(round(i.humedad,1))
                        else:
                            col17.append(0.0)
                        if i.ph:
                            col17.append(round(i.ph,1))
                        else:
                            col17.append(0.0)
                    if x == 14:
                        col18 = list()
                        col18.append(round(i.em1,1))
                        col18.append(round(i.em2,1))
                        col18.append(round(i.em3,1))
                        col18.append(round(i.em4,1))
                        col18.append(round(i.em5,1))
                        col18.append(round(i.em6,1))
                        col18.append(round(i.em7,1))
                        col18.append(round(i.em8,1))
                        col18.append(round(i.em9,1))
                        col18.append(round(i.em10,1))
                        col18.append(round(i.em11,1))
                        col18.append(round(i.em15,1))
                        col18.append(round(i.em14,1))
                        if i.reproceso:
                            col18.append(round(i.reproceso,1))
                        else:
                            col18.append(0.0)
                        col18.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col18.append(round(i.humedad,1))
                        else:
                            col18.append(0.0)
                        if i.ph:
                            col18.append(round(i.ph,1))
                        else:
                            col18.append(0.0)
                    if x == 15:
                        col19 = list()
                        col19.append(round(i.em1,1))
                        col19.append(round(i.em2,1))
                        col19.append(round(i.em3,1))
                        col19.append(round(i.em4,1))
                        col19.append(round(i.em5,1))
                        col19.append(round(i.em6,1))
                        col19.append(round(i.em7,1))
                        col19.append(round(i.em8,1))
                        col19.append(round(i.em9,1))
                        col19.append(round(i.em10,1))
                        col19.append(round(i.em11,1))
                        col19.append(round(i.em15,1))
                        col19.append(round(i.em14,1))
                        if i.reproceso:
                            col19.append(round(i.reproceso,1))
                        else:
                            col19.append(0.0)
                        col19.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col19.append(round(i.humedad,1))
                        else:
                            col19.append(0.0)
                        if i.ph:
                            col19.append(round(i.ph,1))
                        else:
                            col19.append(0.0)
                    if x == 16:
                        col20 = list()
                        col20.append(round(i.em1,1))
                        col20.append(round(i.em2,1))
                        col20.append(round(i.em3,1))
                        col20.append(round(i.em4,1))
                        col20.append(round(i.em5,1))
                        col20.append(round(i.em6,1))
                        col20.append(round(i.em7,1))
                        col20.append(round(i.em8,1))
                        col20.append(round(i.em9,1))
                        col20.append(round(i.em10,1))
                        col20.append(round(i.em11,1))
                        col20.append(round(i.em15,1))
                        col20.append(round(i.em14,1))
                        if i.reproceso:
                            col20.append(round(i.reproceso,1))
                        else:
                            col20.append(0.0)
                        col20.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col20.append(round(i.humedad,1))
                        else:
                            col20.append(0.0)
                        if i.ph:
                            col20.append(round(i.ph,1))
                        else:
                            col20.append(0.0)
                    if x == 17:
                        col21 = list()
                        col21.append(round(i.em1,1))
                        col21.append(round(i.em2,1))
                        col21.append(round(i.em3,1))
                        col21.append(round(i.em4,1))
                        col21.append(round(i.em5,1))
                        col21.append(round(i.em6,1))
                        col21.append(round(i.em7,1))
                        col21.append(round(i.em8,1))
                        col21.append(round(i.em9,1))
                        col21.append(round(i.em10,1))
                        col21.append(round(i.em11,1))
                        col21.append(round(i.em15,1))
                        col21.append(round(i.em14,1))
                        if i.reproceso:
                            col21.append(round(i.reproceso,1))
                        else:
                            col21.append(0.0)
                        col21.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col21.append(round(i.humedad,1))
                        else:
                            col21.append(0.0)
                        if i.ph:
                            col21.append(round(i.ph,1))
                        else:
                            col21.append(0.0)
                    if x == 18:
                        col22 = list()
                        col22.append(round(i.em1,1))
                        col22.append(round(i.em2,1))
                        col22.append(round(i.em3,1))
                        col22.append(round(i.em4,1))
                        col22.append(round(i.em5,1))
                        col22.append(round(i.em6,1))
                        col22.append(round(i.em7,1))
                        col22.append(round(i.em8,1))
                        col22.append(round(i.em9,1))
                        col22.append(round(i.em10,1))
                        col22.append(round(i.em11,1))
                        col22.append(round(i.em15,1))
                        col22.append(round(i.em14,1))
                        if i.reproceso:
                            col22.append(round(i.reproceso,1))
                        else:
                            col22.append(0.0)
                        col22.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col22.append(round(i.humedad,1))
                        else:
                            col22.append(0.0)
                        if i.ph:
                            col22.append(round(i.ph,1))
                        else:
                            col22.append(0.0)
                    if x == 19:
                        col23 = list()
                        col23.append(round(i.em1,1))
                        col23.append(round(i.em2,1))
                        col23.append(round(i.em3,1))
                        col23.append(round(i.em4,1))
                        col23.append(round(i.em5,1))
                        col23.append(round(i.em6,1))
                        col23.append(round(i.em7,1))
                        col23.append(round(i.em8,1))
                        col23.append(round(i.em9,1))
                        col23.append(round(i.em10,1))
                        col23.append(round(i.em11,1))
                        col23.append(round(i.em15,1))
                        col23.append(round(i.em14,1))
                        if i.reproceso:
                            col23.append(round(i.reproceso,1))
                        else:
                            col23.append(0.0)
                        col23.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col23.append(round(i.humedad,1))
                        else:
                            col23.append(0.0)
                        if i.ph:
                            col23.append(round(i.ph,1))
                        else:
                            col23.append(0.0)
                    if x == 20:
                        col24 = list()
                        col24.append(round(i.em1,1))
                        col24.append(round(i.em2,1))
                        col24.append(round(i.em3,1))
                        col24.append(round(i.em4,1))
                        col24.append(round(i.em5,1))
                        col24.append(round(i.em6,1))
                        col24.append(round(i.em7,1))
                        col24.append(round(i.em8,1))
                        col24.append(round(i.em9,1))
                        col24.append(round(i.em10,1))
                        col24.append(round(i.em11,1))
                        col24.append(round(i.em15,1))
                        col24.append(round(i.em14,1))
                        if i.reproceso:
                            col24.append(round(i.reproceso,1))
                        else:
                            col24.append(0.0)
                        col24.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col24.append(round(i.humedad,1))
                        else:
                            col24.append(0.0)
                        if i.ph:
                            col24.append(round(i.ph,1))
                        else:
                            col24.append(0.0)

                    x += 1

                colt.append(round(totem1,1))
                colt.append(round(totem2,1))
                colt.append(round(totem3,1))
                colt.append(round(totem4,1))
                colt.append(round(totem5,1))
                colt.append(round(totem6,1))
                colt.append(round(totem7,1))
                colt.append(round(totem8,1))
                colt.append(round(totem9,1))
                colt.append(round(totem10,1))
                colt.append(round(totem11,1))
                colt.append(round(totem15,1))
                colt.append(round(totem14,1))
                colt.append(round(totrep,1))
                total = totem1+totem2+totem3+totem4+totem5+totem6+totem7+totem8+totem9+totem10+totem11+totem14+totem15+totrep               
                colt.append(round(total,1))
                if y > 0:
                    totaly = tothum/y
                else:
                    totaly = 0.0
                if z > 0:
                    totalz = totph/z
                else:
                    totalz = 0.0
                colt.append(round(totaly,1))
                colt.append(round(totalz,1))
        else:
            nolista2 = 0

        if nolista2 == 0:
            #print("No hay datos")
            resultado = zip(col1,col2,col3,col4)
        elif nolista2 == 1:    
            resultado = zip(col1,col2,col3,col4,col5,colt)
        elif nolista2 == 2:   
            resultado = zip(col1,col2,col3,col4,col5,col6,colt)
        elif nolista2 == 3:   
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,colt)
        elif nolista2 == 4:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,colt)
        elif nolista2 == 5:    
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,colt)
        elif nolista2 == 6:          
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,colt)
        elif nolista2 == 7:        
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,colt)
        elif nolista2 == 8:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,colt)        
        elif nolista2 == 9:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,colt)
        elif nolista2 == 10:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,colt)
        elif nolista2 == 11:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,colt)
        elif nolista2 == 12:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,colt)            
        elif nolista2 == 13:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,colt)
        elif nolista2 == 14:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,colt)
        elif nolista2 == 15:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,colt)
        elif nolista2 == 16:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,colt)
        elif nolista2 == 17:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,colt)
        elif nolista2 == 18:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,colt)
        elif nolista2 == 19:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,colt)
        elif nolista2 >= 20:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,colt)

        return resultado                                                                                     
        # ********************************************    
        # Fin de la creacion de las lista del curpo de
        # la tabla
        # ********************************************  
