from django.shortcuts import render
import uuid , json , string , random, urllib, base64, os, sys, time, pickle, collections, math, arrow
from django.utils.encoding import smart_str
from ecdsa import SigningKey, SECP256k1, NIST384p, BadSignatureError, VerifyingKey
from django.http import *
from django import template
from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.conf import settings
#from cloudbank.utils import instantwallet, generate_wallet_from_pkey, generate_pubkey_from_prikey, checkreward
from django.db.models import Avg, Sum, Count
import base64, bson, websocket, hashlib
#from core.models import transaction
from django.template.defaultfilters import stringfilter
import netifaces as ni


#ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']


def landing(request):
    # try:
    #     pubkey = request.session['pubkey']
    #     prikey = request.session['prikey']
    #     print(pubkey)
    #     print(pubkey.encode('utf-8'))
    #     print(type(pubkey.encode('utf-8')))
    #     wallet_id =  generate_wallet_from_pkey(pubkey) #hashlib.sha256(pubkey.encode('utf-8')).hexdigest() #SHA256.new(pubkey).hexdigest()
    #     balance = getbalance(pubkey)
    #     if balance is None:
    #         balance = 0
    #     return render(request, "ok.html", locals())
    # except KeyError:
    #     return render(request, "index.html", locals())
    return render(request, "templates1/index.html")


def test(request):
    return render(request, "test.html")