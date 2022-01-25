from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from events.models import EventInfo,EventRegistration
from django.db import connection
import sys

sys.path.append("..")

# Create your views here.


class Students():
    
    def get(request):
        try:
            user_data = request.session['user_data']
        except (KeyError, NameError) as e:
            print(e)
            return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
        if not request.session['user_type'] == 'student':
            if request.session['user_type'] == 'admin':
                return redirect(reverse('admin'))  
            return redirect(reverse('logout'))
        events_list = list(EventInfo.objects.all().values())
        reg_event = list(EventRegistration.objects.filter(student_id=user_data['id']).values_list('event_id',flat=True))
        return render(request, 'students/student.html', context={'user_data': user_data,'event':events_list,'reg_event':reg_event})


    def viewStatus(request):
        try:
            user_data = request.session['user_data']
        except KeyError as e:
            print(e)
            return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
        if not request.session['user_type'] == 'student':
            return redirect(reverse('login'))        
        id = user_data['id']
        cur = connection.cursor()
        cur.execute(f'SELECT `event_name`,`description`,`event_id`,`reg_date`,`start_date`,`end_date`,eer.id FROM `events_eventinfo` as ee,`events_eventregistration` as eer where ee.id=eer.event_id and eer.student_id = {id}')
        
        eve = cur.fetchall()
        # eveRegd = EventRegistration.objects.filter(student_id=user_data['id']).select_related('EventInfo').values('event_id')
        
        return render(request,'students/viewStatus.html',context={'regEventList':eve})


    def profile(request):
        try:
            user_data = request.session['user_data']
        except KeyError as e:
            print(e)
            return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
        if not request.session['user_type'] == 'student':
            return redirect(reverse('login'))
        return render(request,'students/profile.html',  context={'user_data': user_data})
    

    def eventRegistrations(request):
        try:
            user_data = request.session['user_data']
        except KeyError as e:
            print(e)
            return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
        if not request.session['user_type'] == 'student':
            return redirect(reverse('login'))
        post = request.POST
        event_info = EventInfo.objects.get(id=post['event_id'])
        print(post)
        try:
            eveReg = EventRegistration(event=event_info,
                                        student_id = user_data['id'],
                                        first_name = user_data['first_name'],
                                        last_name = user_data['last_name'],
                                        department = post['dept']
                                        )
            eveReg.save()
            
        except Exception as e:
            print(e)
        return HttpResponse("<script>alert('Registerd SuccessFully');document.location='../view_status';</script>")
    
    def deleteRegistration(request,id):
        try:
            EventRegistration.objects.get(id=id).delete()

        except Exception as e:
            print(e)
        return HttpResponse("<script>alert('Deleted Successfully');document.location='../view_status'</script>")
    
