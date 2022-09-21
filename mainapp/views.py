from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.

def index(request) :
    item_list=Books.objects.all()
    context={
        'item_list':item_list
    }
    return render(request,'index.html',context)

def add_book(request) :
    if request.method=="POST" :
        book =request.POST['book']
        author =request.POST['author']
        year =request.POST['year']
        type =request.POST['type']
        item=Books(book=book,author=author,year=year,type=type)
        item.save()
        messages.info(request,"ITEM ADDED SUCCESSFULLY!!")
    else :
        pass

    item_list=Books.objects.all()
    context={
        'item_list':item_list
    }
    return render(request,'index.html',context)

def delete_book(request,myid) :
    item=Books.objects.get(id=myid)
    item.delete()
    messages.info(request,"ITEM DELETED SUCCESSFULLY")
    return redirect(index)

def edit_book(request,myid):
    sel_book= Books.objects.get(id=myid)
    item_list=Books.objects.all()

    context={
        'sel_book':sel_book,
        'item_list':item_list

    }
    return render(request,'index.html',context)

def update_book(request,myid):
    item=Books.objects.get(id=myid)
    item.book= request.POST['book']
    item.author= request.POST['author']
    item.year= request.POST['year']
    item.type= request.POST['type']
    item.save()
    messages.info(request," YOUR ITEM UPDATED SUCCESSFULLY!!")
    return redirect(index)
