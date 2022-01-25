from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from events.models import EventInfo,EventRegistration

from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
class Staff:
    def get(request):
        try:
            user_data = request.session['user_data']
        except (KeyError, NameError) as e:
            print(e)
            return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
        if not request.session['user_type'] == 'staff':  
            return redirect(reverse('logout'))
        events_list = list(EventInfo.objects.filter(organised_by = user_data['dept']).values())
        reg_event = list(EventRegistration.objects.filter(student_id=user_data['id']).values_list('event_id',flat=True))
        return render(request, 'staffs/staff.html', context={'user_data': user_data,'event':events_list,'reg_event':reg_event})



def getRegisteredstudents(request):
    try:
        user_data = request.session['user_data']
    except (KeyError, NameError) as e:
        print(e)
        return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
    try:
        department = request.POST['dept']
    except Exception as e:
        return redirect(reverse('staffs'))
    eventId = request.POST['event_id']
    event_name = EventInfo.objects.get(id=eventId).event_name       
    studentsList = list(EventRegistration.objects.filter(event_id = eventId,department = department))
    return render(request,'staffs/registered_students.html',context={'eventName':event_name,'user_data':user_data,'res_stds':studentsList})