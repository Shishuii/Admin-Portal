    def update_record(request):
     if request.method == 'POST':
        if request.POST.get('pk'):
            try:
                r = Question.objects.get(id=request.POST.get('pk'))
                print('++++++++++', request.POST.get('pk'))
                r.ans_detail1 = request.POST.get('question_decription1')
                r.ans_detail2 = request.POST.get('question_decription2')
                r.ans_detail3 = request.POST.get('question_decription3')
                r.ans_detail4 = request.POST.get('question_decription4')
                r.ans_detail5 = request.POST.get('question_decription5')
                r.ans_detail6 = request.POST.get('question_decription6')
                r.text_question = request.POST.get('textarea-name1')

                r.save()
            except Question.DoesNotExist:
                pass
