from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
from .forms import Assessment_Form
from django.contrib import messages

def home(request):
    form=Assessment_Form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            instance=form.save(commit=False)

            instance.save()
            messages.success(request,"SUCESSFULLY CREATED")
        else:
            print(messages.error(request,"NOT CREATED"))


        context ={
                  "form":form,


        }
             #POST goes here . is_ajax is must to capture ajax requests. Beginners pit.
        if request.is_ajax():
            qid = request.POST.get('qid')
            text_question = request.POST.get('text_question')
            ans_detail1= request.POST.get('ans_detail1')
            ans_detail2= request.POST.get('ans_detail2')
            ans_detail3= request.POST.get('ans_detail3')
            ans_detail4= request.POST.get('ans_detail4')
            ans_detail5= request.POST.get('ans_detail5')
            ans_detail6= request.POST.get('ans_detail6')
            data1={
            "qid" : qid,
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

    #Get goes here
    context ={ "form":form, }
    return render(request,'base1.html',context)

# Create your views here.
