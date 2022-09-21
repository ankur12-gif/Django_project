from django.shortcuts import render
import mysql.connector as sql
fn=''
em=''
us=''
pwd=''


# Create your views here.
def signaction(request) :
    global fn,em,us,pwd
    if request.method =="POST" :
        m=sql.connect(host="localhost",user="root",password="Ankur",database="website")
        cursor=m.cursor()
        d= request.POST
        for key,value in d.items():
            if key=="full_name" :
                fn=value
            if key=="email" :
                em=value
            if key=="user_name" :
                us=value
            if key=="password" :
                pwd=value
        
        c= "insert into users Values('{}','{}','{}','{}')".format(fn,em,us,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
            