from collections import UserString
from django.shortcuts import redirect, render
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    '''
    Render to home page of project.

    Keyword Argument:
    request: to create a HttpRequest object.
    '''
    return render(request, 'home.html')





@login_required(login_url='/login')
def add(request):
    """
    Renders the Add book and add user page while getting the get request.
    there are two conditions, one to add new user and one to add new book.

    Keyword Argument:
    request: to create a HttpRequest object.
    
    Return:
    Returns the different type of context dictionary for different blocks of code.
    
    Example:
    If user added succesfully then message is 'User has been added succesfully'
    If book added succesfully then message is 'Book has been added succesfully'
    """

    if request.method == 'POST':
        button_value = request.POST['add']
        # this block is to check the button_value is 'Add Book'.
        if button_value == 'Add Book':
            try:
                name = request.POST['book_name']
                serial = request.POST['book_sn']

                book_row = Book(book_name=name, book_sn=serial,author=request.user)
                book_row.save()
                book_message = 'Book has been added Succesfully'
                return render(
                    request, 'add_user_book.html', {
                        'book_message_green': book_message})
            except BaseException:
                book_message = 'Sorry, Something went Wrong'
                return render(
                    request, 'add_user_book.html', {
                        'book_message_red': book_message})
    return render(request, 'add_user_book.html', {})

def signup(request):
    if request.method=='POST':
        username=request.POST['user_name']
        name=str(username).split()
        print(name)
        email=request.POST['user_email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html',{'user_message_red':'Username already exists.'})
            elif User.objects.filter(email=email).exists():
                return render(request,'signup.html',{'user_message_red':'Email already exists.'})
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.firstname=name[0]
                user.lastname=name[1]
                user.save()
                return redirect('login')
        else:
            return render(request,'signup.html',{'user_message_red': 'Your password doesn\'t match.'})
    
    return render(request,'signup.html')   

def user_login(request):
    if request.method=='POST':
        user_email=request.POST['user_email']
        password=request.POST['password']
        # print(user_email,password)
        member=User.objects.get(email=user_email)
        # print(member)
        username=member.username
        # print(username)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            context={"user_message_red": 'Invalid Credential'}
            return render(request,'login.html',context)
    return render(request,'login.html')

def user_logout(request):
    logout(request)  
    return redirect('Home')

@login_required(login_url='login')
def update_book(request):
    books=Book.objects.all()
    if request.method=="POST":
        select_option=request.POST['select_option']
        select_book=request.POST['select_book']
        update=request.POST['update']

        try:
            if select_option=='book_sn':
                book_row=Book.objects.get(book_name=select_book)
                book_row.book_sn=update
                book_row.save()
                return redirect('Home')
            elif select_option=='book_name':
                book_row=Book.objects.get(book_name=select_book)
                book_row.book_name=update
                book_row.save()    
                return redirect('Home')
        except:
            context={"user_message_red": 'Something went Wrong!'}
            return render(request,'update.html',context)     
    return render(request,"update.html",{'books':books})

@login_required(login_url='login')
def delete_object(request):
    books=Book.objects.all()
    if request.method=="POST":
        select_book=request.POST['select_book']
        book_row=Book.objects.get(book_name=select_book)
        book_row.delete()
        return redirect('Home')
    return render(request,'delete.html',{'books':books})

def list_book(request):
    books=Book.objects.all()
    return render(request,'student_view.html',{'books':books})





