from django.urls import path,include
from Food import views
from django.contrib.auth import views as g

urlpatterns=[
path('',views.home,name="hm"),
path('abt/',views.about,name="ab"),
path('cnt/',views.contact,name="ct"),
path('reg/',views.regis,name="regi"),
path('ds/',views.dashboard,name="dsh"),
path('pf/',views.prfle,name="pfe"),
path('upf/',views.updf,name="upfe"),
path('cha/',views.chani,name="chane"),
path('sou/',views.south,name="south"),
path('hyd/',views.hyde,name="hyd"),
path('so/',views.southw,name="southw"),
path('sos/',views.southwa,name="southwa"),
path('no/',views.northw,name="northw"),
path('non/',views.northwa,name="northwa"),
path('ke/',views.wrklg,name="wk"),
path('crwrk/',views.creationwrk,name="crk"),
# path('fdlt/',views.food,name="fd"),
# path('del/',views.delet,name="det"),
# path('pd/',views.produ,name="po"),
path('lg/',g.LoginView.as_view(template_name="sa/login.html"),name="lgn"), 
path('lgg/',g.LogoutView.as_view(template_name="sa/logout.html"),name="lgo"),
]