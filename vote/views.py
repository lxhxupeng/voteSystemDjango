from django.shortcuts import render
from vote.models import Subject
# Create your views here.


def show_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})


def show_teachers(request):
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except (KeyError, ValueError, Subject.DoesNotExist):
        return
