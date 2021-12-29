from django.http  import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request,'index.html')


def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #check checkboxes value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlinermv=request.POST.get('newlinermv','off')
    removespace=request.POST.get('removespace','off')
    capfirst=request.POST.get('capfirst','off')
    charcount=request.POST.get('charcount','off')
    fulllower=request.POST.get('fulllower','off')

    
    # check which check is on
    if removepunc == 'on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps == 'on':
        analyzed=''
        for i in djtext:
            analyzed=analyzed+i.upper()
        
        params={'purpose':'Capatilize All','analyzed_text':analyzed}
        djtext=analyzed
    
    if newlinermv=='on':
        analyzed=''
        for i in djtext:
            if i!='\n' and i!='\r':
                analyzed=analyzed+i
        params={'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext=analyzed

    if removespace== 'on':
        analyzed=''
        for i,char in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Remove Space','analyzed_text':analyzed}
        djtext=analyzed
        
    if capfirst== 'on':
        analyzed=djtext[0].upper()
        for i in range(1,len(djtext)):
            analyzed=analyzed+djtext[i]
        params={'purpose':'Caps first','analyzed_text':analyzed}
        djtext=analyzed
        
    if charcount== 'on':
        analyzed=0
        for i in djtext:
            analyzed=analyzed+1
        params={'purpose':'Count chars','analyzed_text':analyzed}
        djtext=analyzed
        
    if fulllower== 'on':
        analyzed=''
        for i in djtext:
            analyzed=analyzed+i.lower()
        params={'purpose':'Full lower','analyzed_text':analyzed}
        djtext=analyzed
        
    return render(request,'analyze.html',params)
    