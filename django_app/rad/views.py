from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import calendar

from .forms import TradersForm
from .forms import DistrosForm
from .forms import TraderToDistrosForm
from .models import Distros, DistroCurrentData
from .utils import send_mqtt_message

# This is what appears when the user navigates to the corresponding webpage

def index(request):
    distros = {}
    distroData = {}

    for distro in Distros.objects.order_by('id'):
        distros[distro.id] = distro
        socketDatas = {}
        for socketNo in range(1, distro.socket_count+1):
            dataTemp = DistroCurrentData.objects.filter(distroID=distro.id,socketNum=socketNo).order_by('-timestamp')
            if dataTemp.count() > 0:
                socketDatas[socketNo] = DistroCurrentData.objects.filter(distroID=distro.id,socketNum=socketNo).order_by('-timestamp').first()
            else:
                socketDatas[socketNo]=None

        distroData[distro.id] = socketDatas

    data1 = []
    data2 = []
    data3 = []
    data4 = []
    timelist = []
    
    x=0
    for item in DistroCurrentData.objects.filter(distroID=1,socketNum=1):
        data1.append(item.currentValue)
        timelist.append(calendar.timegm(item.timestamp.timetuple())*1000)
    for item in DistroCurrentData.objects.filter(distroID=1,socketNum=2):
        data2.append(item.currentValue)
        timelist.append(calendar.timegm(item.timestamp.timetuple())*1000)
    for item in DistroCurrentData.objects.filter(distroID=1,socketNum=3):
        data3.append(item.currentValue)
        timelist.append(calendar.timegm(item.timestamp.timetuple())*1000)
    for item in DistroCurrentData.objects.filter(distroID=1,socketNum=4):
        data4.append(item.currentValue)
        timelist.append(calendar.timegm(item.timestamp.timetuple())*1000)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    kwargs2 = {'color': 'red'}
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal", },"date_format": tooltip_date,}
    chartdata1 = {'x': timelist, 'name1': 'Socket 1', 'y1': data1, 'extra1': extra_serie, 'kwargs1': { 'color': '#28a148' }}
    chartdata2 = {'x': timelist, 'name1': 'Socket 2', 'y1': data2, 'extra1': extra_serie, 'kwargs1': { 'color': '#28a148' }}
    chartdata3 = {'x': timelist, 'name1': 'Socket 3', 'y1': data3, 'extra1': extra_serie, 'kwargs1': { 'color': '#28a148' }}
    chartdata4 = {'x': timelist, 'name1': 'Socket 4', 'y1': data4, 'extra1': extra_serie, 'kwargs1': { 'color': '#28a148' }}
    charttype = "lineChart"
    charttype2 = "lineChart"
    chartcontainer1 = 'socket_1_container'
    chartcontainer2 = 'socket_2_container'
    chartcontainer3 = 'socket_3_container'
    chartcontainer4 = 'socket_4_container'

    data = {
        'distros': distros,
        'distroData': distroData,
        'charttype': charttype,
        'charttype2' :charttype2,
        'chartdata1': chartdata1,
        'chartdata2': chartdata2,
        'chartdata3': chartdata3,
        'chartdata4': chartdata4,
        'chartcontainer1': chartcontainer1,
        'chartcontainer2': chartcontainer2,
        'chartcontainer3': chartcontainer3,
        'chartcontainer4': chartcontainer4,
        'extra': {
            'x_is_date': True,
            'x_axis_format': tooltip_date
        }
    }    
    return render(request, 'index.html', data)

def traders(request):
    form = TradersForm()
    
    context = {'form' : form}
    return render(request, 'traders_form.html', context)

def distros(request):
    form = DistrosForm()
    
    context = {'form' : form}
    return render(request, 'distros_form.html', context)

def distroDisplay(request):    
    return render(request, 'distroDisplay.html')

def traderDistro(request):
    form = TraderToDistrosForm()
    
    context = {'form' : form}
    return render(request, 'trader_distro_form.html', context)

@require_POST
def traderRequest(request):
    form = TradersForm(request.POST)

    if form.is_valid():
       formData = form.save()

    return redirect('traders')

@require_POST
def distroRequest(request):
    form = DistrosForm(request.POST)

    if form.is_valid():
       formData = form.save()

    return redirect('distros')

@require_POST
def traderDistroRequest(request):
    form = TraderToDistrosForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect('trader_distros')

@require_POST
@csrf_exempt
def distroChangeStateRequest(request):
   distro = request.POST.get('distro')
   socket = int(request.POST.get('socket'))
   state = False if request.POST.get('state') == "False" else True
   send_mqtt_message(distro, socket, state)
   return redirect('index')
