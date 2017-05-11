# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import os

import re


# Create your views here.


def index(request):
    return render(request, 'EmailControl/index.html')


def starttask(request):
    #  check if it is started
    request.session['is_start'] = 0
    is_start = request.session.get('is_start', default=None)
    if is_start is 1:
        return HttpResponse('The program is running, please wait ...')

    request.session['is_start'] = 1

    # get input
    email = request.POST['resultName']
    title = request.POST['businessName']
    return HttpResponse(0)
    # email_list = email.split(';')
    email_list = re.split(';', email)
    print email
    print email_list

    #检查群发邮件信息
    for lis in email_list:
        if lis == '':
            return HttpResponse('Please input email')
        if len(lis) < 7:
            return HttpResponse('Please input email')
        else:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", lis) == None:
                return HttpResponse('Please input email')
        # check input
    # if email == '':
    #     return HttpResponse('Please input email')
    #
    # if len(email) < 7:
    #     return HttpResponse('Please input correct email')
    # else:
    #     if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
    #         return HttpResponse('Please input correct email')

    if title == '':
        return HttpResponse('Please input email subject')

    # execute shell script
    result_code = os.system('./onePressFauxpas.sh')
    request.session['is_start'] = 0

    # check execute result
    if result_code == 0:
        # success_count = send_mail(title, 'this is a error message', 'gysxl007@didichuxing.com', [email], fail_silently=False)
        text_content = '检测完毕，具体错误详见附件'
        msg = EmailMultiAlternatives(title, text_content, 'gysxl007@126.com', email_list)
        msg.attach_file('./result.txt')
        msg.send()
    # if success_count > 0:
    #     result_code = 0
    # else:
    #     result_code = 1

    return HttpResponseRedirect(reverse('result', args=(result_code,)))


def result(request, result_code):
    content = {'result_code': result_code}
    return render(request, 'EmailControl/result.html', content)
