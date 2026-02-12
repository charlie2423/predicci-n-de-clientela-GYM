# prediccion-de-clientela-GYM
Una cadena de gimnasios Model Fitness está desarrollando una estrategia de interacción con clientes basada en datos analíticos.
<img width="743" height="546" alt="Captura de pantalla 2026-02-12 011008" src="https://github.com/user-attachments/assets/8d3222c9-8f12-4a67-96a4-1bb980512955" />
<img width="758" height="733" alt="Captura de pantalla 2026-02-12 011217" src="https://github.com/user-attachments/assets/3e038837-ac61-42b2-9502-5d6e295f61ee" />

# modelo de clasificación binaria para clientes donde la característica objetivo es la marcha del usuario o la usuaria el mes siguiente.
Exactitud: 0.94
Precisión: 0.89
Recall: 0.87

Exactitud: 0.93
Precisión: 0.88
Recall: 0.84

el modelo LogisticRegression dio mejores resultados

<img width="998" height="1004" alt="Captura de pantalla 2026-02-12 011233" src="https://github.com/user-attachments/assets/45b0faf1-e438-4a2a-84c6-01c3add0aa00" />

# predicion de clustering de los clientes 

0     3
1     1
2     0
3     1
4     0
5     2
6     3
7     4
8     0
9     0
10    3
11    4
12    2
13    4
14    0
15    1
16    2
17    0
18    0
19    1
# valores medios de característica para los clústeres
              gender  Near_Location   Partner  Promo_friends     Phone  \
cluster_km                                                               
0           0.475638       0.827146  0.447796       0.254060  1.000000   
1           0.503106       0.938923  0.768116       0.564182  1.000000   
2           0.550059       0.840989  0.374558       0.215548  0.998822   
3           0.524804       0.866841  0.469974       0.308094  0.000000   
4           0.507447       0.760638  0.341489       0.179787  0.997872   

            Contract_period  Group_visits        Age  \
cluster_km                                             
0                  2.647332      0.381671  30.010441   
1                 11.173913      0.557971  29.899586   
2                  2.750294      0.441696  29.984688   
3                  4.806789      0.428198  29.331593   
4                  1.567021      0.257447  26.908511   

            Avg_additional_charges_total  Month_to_end_contract  Lifetime  \
cluster_km                                                                  
0                             153.532535               2.464037  4.674014   
1                             161.514913              10.223602  4.704969   
2                             160.178822               2.528857  4.588928   
3                             144.156967               4.493473  3.945170   
4                             115.109065               1.513830  0.976596   

            Avg_class_frequency_total  Avg_class_frequency_current_month  \
cluster_km                                                                 
0                            1.180614                           1.179787   
1                            2.006679                           2.001081   
2                            2.930098                           2.936773   
3                            1.855107                           1.723740   
4                            1.448700                           1.026250   

               Churn  
cluster_km            
0           0.001160  
1           0.015528  
2           0.007067  
3           0.263708  
4           0.997872  
pude notar que en near location del numero de 0 a 3 esta muy cerca de el 1 suponiendo que la gente que va vive cerca del gym.


<img width="1058" height="961" alt="Captura de pantalla 2026-02-12 011244" src="https://github.com/user-attachments/assets/14761d7b-23c2-4651-8f2d-bf6c29838832" />
se puede ver que la gente de entre 20 y casi 40 son los que frecuentan mas el gym



<img width="1017" height="955" alt="Captura de pantalla 2026-02-12 011255" src="https://github.com/user-attachments/assets/c317b55c-75e5-48c1-9d92-ed7390352457" />
la mayoria de grupos se mantienen muchos meses en el gym los del grupo 4 no duran ni el año

<img width="1043" height="967" alt="Captura de pantalla 2026-02-12 011302" src="https://github.com/user-attachments/assets/962fd83c-5863-4dd5-98bf-2aa0f8861416" />

<img width="1031" height="987" alt="Captura de pantalla 2026-02-12 011317" src="https://github.com/user-attachments/assets/7c751b14-76f0-41f2-ac74-f54b413b681d" />

<img width="985" height="984" alt="Captura de pantalla 2026-02-12 011324" src="https://github.com/user-attachments/assets/2dc0a03b-afb3-43b6-bb49-9b076c9f9060" />

# Tasa de cancelación para cada clúste

  cluster_km     Churn
           0  0.001160

           1  0.015528

           2  0.007067

          3  0.263708

         4  0.997872


e podria decir que si difieren los grupos ya que el grupo 0 tiene una taza del 0% sinedo los menos propensos a irse los de grupo 4 tiene una taza de casi el 100% siendo los mas propensos a irse

# conclucion
podriamos priorisar la publicidad cerca del gym ya que los que mas van y se quedan son los que viven mas cerca del gym, asi como poner promociones para estudiantes y colaborar con mas empresas para llegar a mas personas. Tambien se podria poner promosiones para personas con mayoria de edad e insitar que vengan ya que las mayoria de personas que van son de entre 20 y 40 años. asi como tambien dar promosiones en los sevicios a la gente que lleve tiempo en el gym para insitar a que se queden mas tiempo


