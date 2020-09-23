from django.shortcuts import render
from .models import TdsModel

from django_user_agents.utils import get_user_agent

from django.db.models import Count, Min


# Create your views here.

def index(request):
    user_agent = get_user_agent(request)
    target_data = TdsModel.objects.all()
    object = list(target_data.values('area').annotate(total=Count('area')).order_by('jis'))
    #接続時、機種ごとに表示するページを変える
    if user_agent.is_pc and "param" in request.GET==False:
        return render(request, 'index_map.html', { 'object': object })
    elif user_agent.is_pc and "param" in request.GET:
        return render(request, 'index.html', { 'object': object })
    else:
        if user_agent.is_pc:
            return render(request, 'index_map.html', { 'object': object })
        else:
            return render(request, 'index.html', { 'object': object })

def index_map(request):
    user_agent = get_user_agent(request)
    target_data = TdsModel.objects.all()
    object = list(target_data.values('area').annotate(total=Count('area')).order_by('jis'))
    #万が一PC以外からindex_map.htmlに接続した場合、index.htmlに接続
    if user_agent.is_pc:
        return render(request, 'index_map.html', { 'object': object })
    else:
        return render(request, 'index.html', { 'object': object })

def tdslist(request):
    #タイプ選択時(m=selectedのとき)
    if "m" in request.GET:
        area_param = request.GET.get("area")
        type_param = request.GET.get("type")
        mode_param = request.GET.get("m")
        object = TdsModel.objects.filter(area=area_param,type__contains=type_param)
        area_dict = {
            'area_name': area_param,
            'type_name': type_param,
            'mode': mode_param,
            'object_list': object,
        }
        return render(request, 'list.html', area_dict)
    #タイプ未選択(m=" "のとき)
    else:
        if "area" in request.GET:
            area_param = request.GET.get("area")
            object = TdsModel.objects.filter(area=area_param)
            area_dict = {
                'area_name': area_param,
                'object_list': object,
            }
            return render(request, 'list.html', area_dict)
        else:
            object = TdsModel.objects.all()
            area_dict = {
                'area_name': "東京都",
                'object_list': object,
            }
            return render(request, 'list.html', area_dict)

def listdetail(request):
    if "facility" in request.GET:
        facility_param = request.GET.get("facility")
        type_param = request.GET.get("type")
        mode_param = request.GET.get("m")
        object = TdsModel.objects.filter(facility=facility_param)
        area_dict = {
            'type': type_param,
            'mode': mode_param,
            'object': object,
        }
        return render(request, 'detail.html', area_dict)

def type(request):
    if "type" in request.GET:
        type_param = request.GET.get("type")
        type_data = TdsModel.objects.filter(type__contains=type_param)
        object = list(type_data.values('area').annotate(area_total=Count('area'),type_total=Count('type')).order_by('jis'))
        area_dict = {
            'type_name': type_param,
            'object': object,
        }
        return render(request, 'type_area.html', area_dict)

def menu(request):
    p_param = request.GET.get("p")
    if p_param == "1":
        return render(request, 'tdsinfo.html')
    elif p_param == "2":
        return render(request, 'about.html')
    elif p_param == "3":
        return render(request, 'contact.html')
    else:
        return render(request, 'another.html')
