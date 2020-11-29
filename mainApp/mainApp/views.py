from django.shortcuts import render

def test(request):
    print('GET userID :', request.GET.get("userId"))
    print('GET userPW :', request.GET.get("userpw"))
    print('-------------------------------')
    print('POST userID:', request.POST.get("userId"))
    print('POST userPW:', request.POST.get("userpw"))
    return render(request, 'test/test.html')
