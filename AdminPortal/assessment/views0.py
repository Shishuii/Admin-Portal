from django.shortcuts import render
from django.http import JsonResponse
from .models import Question

from django.contrib import messages

def home(request):


             #POST goes here . is_ajax is must to capture ajax requests. Beginners pit.
        if request.is_ajax():
            Profile = request.POST.get('Profile')
            Primary_category= request.POST.get('Primary_category')
            assessment_name = request.POST.get('assessment_name')
            qid = request.POST.get('qid')
            qtype = request.POST.get('qtype')
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
            "qtype":qtype,
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
            print(data1)

            return JsonResponse(data1)

    #Get goes here

        return render(request,'Create_Assessment.html')

# Create your views here.
