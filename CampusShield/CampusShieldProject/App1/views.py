from django.shortcuts import render,redirect
from .models import report,Suggestion
# Create your views here.
def home(request):
    if request.method=='POST':
        t=request.POST['title']
        d=request.POST['desc']
        Suggestion.objects.create(title=t,description=d)
        return render(request,'Suggestion.html')
        

    return render(request,'home.html')


def submit(request):
    if request.method=='POST':
        c=request.POST['category']
        d=request.POST['description']
        report.objects.create(category=c,description=d)
        return redirect('thanks')

    return render(request,'submit.html')

def thanks(request):
    r=report.objects.last()
    return render(request,'Thankyou.html',{'id':r.reportid})
    

def track(request):
    if request.method=='POST':
        r=request.POST['rid']

        c=1
        try:
            c=0
            report_id=report.objects.get(reportid=r)
            return render(request,'track.html',{'rpid':report_id})

        except report.DoesNotExist:
            return render(request,'track.html',{'error':"'Invalid Report ID. Please try again.'"})
    
    return render(request,'track.html')
    
    
def faculty(request):
    return render(request,'FacultySupport.html')

def about(request):
    return render(request,'About.html')