import json
import random
import request
from django.shortcuts import render
from manager.models import Person, Manager, Worker
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

get_object_or_404(Person, id=20)

# Create your views here.



class WorkerListView(TemplateView):
    template_name = "worker_list.html"
    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all()
        context['workers'] = workers
        return render(self.request, self.template_name, context)

class WorkerListView2(TemplateView):
    template_name = "worker_list.html"
    def get(self, request, *args, **kwargs):
        context = super(WorkerListView2, self).get_context_data(**kwargs)

        workers = Worker.objects.filter(person__current_address=Person.SHIGA)
        context['workers'] = workers
        return render(self.request, self.template_name, context)

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']
        message_type = e['message']['type']

        if message_type == 'text':
            text = e['message']['text']
            reply += reply_text(reply_token, text)
    return HttpResponse(reply)