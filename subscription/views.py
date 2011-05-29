# -*- coding: utf-8 -*-

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)
    
    subscription = form.save()
    print subscription
    send_mail(
              subject=u'Inscrição no EventeX',
              message=u'Obrigado por se inscrever no EventeX!',
              from_email='contato@eventex.com',
              recipient_list=[subscription.email],
    )
    
    return HttpResponseRedirect(reverse('subscription:success', args=[subscription.pk]))

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
