from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import get_object_or_404 , redirect, render
from .models import Guide, MapData
from django.utils import timezone
import json, requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def guide_list (request) :
    lists = Guide.objects.all()
    return render(request,'guide_list.html',{'guide_list':lists})

def guide_detail(request,id) :
    guide_detail = get_object_or_404(Guide,pk=id)
    map_data = get_object_or_404(MapData,pk=id)
    map_title = map_data.keys.replace("[",'').replace("]",'').replace("'",'')
    
    map_latlng = str(eval(map_data.keysvalues).values())[14:-3].replace("'",'')
    
    
    content = {
        'guide_detail' : guide_detail,
        'map_title' : map_title,
        'map_latlng' : map_latlng,
        'cnt' : map_data.cnt,
    }
    return render (request,'guide_detail.html',{'content':content})


def guide_new (request) :
   
    if (request.method == 'POST') :
        newGuide = Guide.objects.create(title = request.POST['title'],
                                        content = request.POST['content'],
                                        writer = request.user,
                                        date = timezone.localtime(),
                                        location = request.POST['location'],
                                        price = request.POST['price'],
                                    )
        if (request.FILES.get('image') is not None) :
            newGuide.image = request.FILES['image']
            newGuide.save()
    
        return guide_list(request)
    
    if (request.method == 'GET') :
        return render(request,'guide_new.html')

def guide_update (request, id) :
    if (request.method == 'GET') :
        update_guide = get_object_or_404(Guide,pk=id)
        
        return render (request,'guide_update.html',{'guide_update':update_guide})

    elif (request.method == 'POST') :
        update_guide = Guide.objects.get(pk=id)
        update_guide.title= request.POST['title']
        update_guide.content= request.POST['content']
        update_guide.location= request.POST['location']
        update_guide.price= request.POST['price']
        update_guide.image= request.FILES['image']
        update_guide.save() 
        
        return guide_list(request)

def guide_delete (request, id) :
    if (request.method == 'GET') :
        guide = get_object_or_404(Guide,pk=id)
        map = get_object_or_404(MapData,pk=id)
        guide.delete()
        map.delete()
        return guide_list(request)

def guide_search_by_location (request) :
    search_key = request.GET['location']
    # search_list = Guide.objects.all()
    
    search_list = Guide.objects.filter(location=search_key)
    
    
    return render(request,'guide_list.html',{'guide_list':search_list})

def kakaopay_index (request) :
    if request.method=="GET" :
        return render(request,'kakaopay/index.html')
 
def kakaopay_process (request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "68a707d09ab3ccb120449c0bbcb3beaf",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "kekim20",    # 유저 아이디
            "item_name": "트래토 가이드",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "12000",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/guide/kakaopay_success",
            "cancel_url": "http://127.0.0.1:8000/guide/kakaopay_cancel",
            "fail_url": "http://127.0.0.1:8000/guide/kakaopay_fail",
        }

        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

def kakaopay_success (request) :
     _url = 'https://kapi.kakao.com/v1/payment/approve'
     _admin_key = '68a707d09ab3ccb120449c0bbcb3beaf' # 입력필요
     _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
     _data = {
        'cid':'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id':'1001',
        'partner_user_id':'kekim20',
        'pg_token': request.GET['pg_token'],
        'item_name': '트래토 가이드',
        "total_amount": "12000",
    }
     _res = requests.post(_url, data=_data, headers=_headers)

    # _amount = _res.json()['total_amount']
     _res = _res.json()
     context = {
        'res': _res,
        'amount': _res.get('total_amount'),
    }
     return render(request, 'kakaopay/success.html', context)

    #  _result = _res.json()


    # #  if _result.get('msg'):
    # #     return redirect('kakaopay_fail')
    # #  else:
    # #     # * 사용하는 프레임워크별 코드를 수정하여 배포하는 방법도 있지만
    # #     #   Req Header를 통해 분기하는 것을 추천
    # #     # - Django 등 적용 시
    # #     return render(request, 'kakaopay/success.html')
        

def kakaopay_fail (request):
    return render(request, 'kakaopay/fail.html')
def kakaopay_cancel (request):
    return render(request, 'kakaopay/cancel.html')
 

@csrf_exempt
def save_map_data (request) :
    dict = json.loads(request.body)
    MapData.objects.create(keys = dict['keys'], keysvalues = dict['keysvalues'], cnt= dict['cnt'])
    return HttpResponse('kkk')