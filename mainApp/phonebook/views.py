from django.shortcuts import render, redirect
from phonebook.models import PhoneBook
from lib2to3.fixes.fix_input import context

# Create your views here.
def test(request):
    return render(request, "phonebook/test.html")

def index(request):
    alluser= PhoneBook.objects.values('id', '이름', '전화번호')
    context= {"info":alluser}
    print ('==== alluser: ', alluser)
    return render(request, "phonebook/index.html", context)

def add(request):
    if request.method == 'POST':
        table = PhoneBook()
        table.이름 = request.POST.get('name')
        table.전화번호 = request.POST.get('phNum')
        table.이메일 = request.POST.get('email')
        table.주소 = request.POST.get('address')
        table.생년월일 = request.POST.get('bir')
        table.save()
        return redirect("PB:index")
        #return render(request,'phonebook/index.html') --> 상황에 따라서 적합한 것 판단
    else:
        return render(request, "phonebook/add.html")

def delete(request):
    return render(request, "phonebook/delete.html")

def detail(request, userId):
    UserInfo= PhoneBook.objects.values(
        'id', '이름', '전화번호', '주소', '생년월일', '이메일').get(id=userId)
    context= {"UserInfo": UserInfo}
    print (UserInfo)
    return render(request, "phonebook/detail.html", context)

def update(request, userId):
    
    UserInfo= PhoneBook.objects.values(
    'id', '이름', '전화번호', '주소', '생년월일', '이메일').get(id=userId)
    context= {"UserInfo": UserInfo}
    
    if request.method == 'POST':

        table = PhoneBook()
        table.이름 = request.POST.get('name')
        table.전화번호 = request.POST.get('phNum')
        table.이메일 = request.POST.get('email')
        table.주소 = request.POST.get('address')
        table.생년월일 = request.POST.get('bir')           
        table.save()    
        return redirect("PB:index")
    else:
        return render(request, "phonebook/update.html", context)        
