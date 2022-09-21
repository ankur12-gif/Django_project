from django.shortcuts import render
import mysql.connector as sql
fnm=''
lnm=''
ag=''
em=''
cg=''
pwd=''


# Create your views here.
def signaction(request) :
    global fnm,lnm,ag,em,cg,pwd
    if request.method =="POST" :
        m=sql.connect(host="localhost",user="root",password="Ankur",database="website")
        cursor=m.cursor()
        d= request.POST
        for key,value in d.items():
            if key=="first_name" :
                fnm=value
            if key=="last_name" :
                lnm=value
            if key=="age" :
                ag=value
            if key=="email" :
                em=value
            if key=="college_name" :
                cg=value
            if key=="password" :
                pwd=value
        
        c= "insert into student Values('{}','{}','{}','{}','{}','{}')".format(fnm,lnm,ag,em,cg,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'student_signup.html')
            