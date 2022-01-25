from functools import reduce
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect

User = get_user_model()

# Create your views here.
def login_check(req):
    username = req.POST.get('email')
    password = req.POST.get('password')

    user = User.objects.filter(email = username).first()
    if not user:
        messages.warning(req,'user does not exist')
        return {'status':False}
    else:
        if not user.check_password(password):
            messages.error(req,'your password was incorrect')
            return {'status':False}
    return {'status':True,'data':user}
def Login(req):
    context = {}
    path ='includes/login.html'
    if req.method == 'POST':
        res = login_check(req)
        if res['status']:
           user = res['data']
           user_data = {'dept':user.department,'id':user.id ,'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
           if user.is_student:
               user_type = "student"
               req.session['user_data'] = user_data
               req.session['user_type'] = user_type
               return redirect(reverse('student'))

           elif user.is_staff and not user.is_admin:
               user_type = 'staff'
               req.session['user_data'] = user_data
               req.session['user_type'] = user_type
               return redirect(reverse('staffs'))

           elif user.is_admin and user.is_staff:
               user_type = 'admin'
               req.session['user_data'] = user_data
               req.session['user_type'] = user_type
               return redirect(reverse('admin'))

    return render(req,'includes/login.html')

def logout(request):
    try:
        del request.session['user_data']
        del request.session['user_type']
    except Exception as e:
        print(e)
    return redirect(reverse('login'))


# def Admin(request):
#     try:
#         data = request.session['user_data']
#     except KeyError as e:
#         print(e)
#         return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")

#     if not request.session['user_type'] == 'admin':
#         return redirect(reverse('login'))
#     return render(request,'admin/admin.html',context=data)




# def Staffs(request):
#     try:
#             data = request.session['user_data']
#     except KeyError as e:
#         print(e)
#         return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")

#     return render(request,'staffs/staff.html')
