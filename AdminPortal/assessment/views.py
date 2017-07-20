from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import JsonResponse
from .models import Question
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView


def home(request):


    return render(request,'home.html')



def home1(request):

    if request.method == 'POST':

             #POST goes here . is_ajax is must to capture ajax requests. Beginners pit.
        if request.is_ajax():
            Profile = request.POST.get('Profile')
            Primary_category= request.POST.get('Primary_category')
            assessment_name = request.POST.get('assessment_name')
            qid = request.POST.get('qid')
            #qtype = request.POST.get('qtype')
            text_question = request.POST.get('text_question')
            ans_detail1= request.POST.get('ans_detail1')
            ans_detail2= request.POST.get('ans_detail2')
            ans_detail3= request.POST.get('ans_detail3')
            ans_detail4= request.POST.get('ans_detail4')
            ans_detail5= request.POST.get('ans_detail5')
            ans_detail6= request.POST.get('ans_detail6')
            data1={
            "Profile":Profile,
            "Primary_category":Primary_category,
            "assessment_name":assessment_name,
            "qid" : qid,
            #"qtype":qtype,
            "text_question" : text_question,
            "ans_detail1":ans_detail1,
            "ans_detail2":ans_detail2,
            "ans_detail3":ans_detail3,
            "ans_detail4":ans_detail4,
            "ans_detail5":ans_detail5,
            "ans_detail6":ans_detail6,
            }

            q= Question(**data1)
            q.save()

            return JsonResponse(data1)

        return HttpResponseRedirect(reverse('assessment-list'))

    return render(request,'blank-page.html')


# Create your views here.
class AssessmentList(ListView):
    model = Question
    #template_name = 'BASE_DIR' + '/templates/question_list.html'
class DeleteAssessment(DeleteView):
    model = Question
    success_url = reverse_lazy('assessment-list')


class QuestionUpdate(UpdateView):
    model = Question
    fields = ["assessment_name","text_question","ans_detail1","qid",
          "ans_detail2","ans_detail3","ans_detail4","ans_detail5","ans_detail6",]
    template_name = 'Create_Assessment0.html'
    success_url = '/'
class DetailAssessment(DetailView):
    model = Question
