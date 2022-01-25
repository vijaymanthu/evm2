from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from events.models import EventInfo

import sys
sys.path.append("..")


# Create your views here.
def Admin(request):
    try:
        user_data = request.session['user_data']
    except KeyError as e:
        print(e)
        return HttpResponse("<script>alert('Not Authorised to this page');document.location='../login'</script>")
    if not request.session['user_type'] == 'admin':
        return redirect(reverse('login'))
    return render(request, 'admin/admin.html', context={'user_data': user_data})


class Events:
    def get(request):
        user_data = request.session['user_data']
        events_list = list(EventInfo.objects.all().values())

        return render(request, 'admin/event_list.html', context={'user_data': user_data, 'event_list': events_list})
        
    def add(request):
        post = request.POST

        try:
            eve = EventInfo(event_name=post['event_name'],
                            organised_by=post['organised_by'],
                            start_date=post['start_date'],
                            end_date=post['end_date'],
                            description = post['description']
                            )
            eve.save()
            return redirect(reverse('events'))
        except Exception as e:
            print(e)

    def update(request, id):
        edit_event = EventInfo.objects.get(id=id)
        if request.method == "POST":
            post = request.POST
            print(post)
            edit_event.event_name = post['event_name']
            edit_event.organised_by = post['organised_by']
            edit_event.start_date = post['start_date']
            edit_event.end_date = post['end_date']
            edit_event.description = post['description']

            edit_event.save()
            return HttpResponse("<script>alert('updated Successfully');document.location='./../events'</script>")
        try:
            return render(request, 'admin/update_event.html', context={'data': edit_event})
        except Exception as e:
            print(e)
            return HttpResponse(e)

    def delete(request, id):
        try:
            del_event = EventInfo.objects.get(id=id)
            del_event.delete()
            return HttpResponse("<script>alert('deleted Successfully');document.location=''</script>")
        except Exception as e:
            print(e)
            return redirect(reverse('events'))
