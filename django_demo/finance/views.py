import json
from django.shortcuts import render
import yfinance
from datetime import datetime


# Create your views here.
def index(request):
    msft = yfinance.Ticker("MSFT")
    hist = msft.history(period="1y").to_json()
    data = json.loads(hist)

    data_formatted = [{**{"Date": datetime.fromtimestamp(int(dt) / 1000).strftime('%Y-%m-%d %H:%M:%S')},
      **{fd: data.get(fd).get(dt) for fd in data.keys()}} for dt in data.get(list(data.keys())[0]).keys()]

    return render(request, 'finance/index.html', {'title': 'Finance', 'data': data_formatted})


def timeseries(request):
    ric = request.GET['ric']
    startdate = request.GET['startdate']
    enddate = request.GET['enddate']
    ticker = yfinance.Ticker(ric)
    if startdate is None or enddate is None:
        hist = ticker.history(period="1y").to_json()
    else:
        startdate = datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')
        enddate = datetime.strptime(enddate, '%m/%d/%Y').strftime('%Y-%m-%d')
        hist = ticker.history(period="1y", start=startdate, end=enddate).to_json()
    data = json.loads(hist)

    data_formatted = [{**{"Date": datetime.fromtimestamp(int(dt) / 1000).strftime('%Y-%m-%d %H:%M:%S')},
      **{fd: data.get(fd).get(dt) for fd in data.keys()}} for dt in data.get(list(data.keys())[0]).keys()]

    return render(request, 'finance/timeseries.html', {'title': 'Finance', 'data': data_formatted, 'ric': ric, 'startdate': startdate, 'enddate': enddate})
    #http://127.0.0.1:8000/finance/ticker?ric=AMZN&startdate=2019-04-09&enddate=2019-12-12


def form(request):

    return render(request, 'finance/form.html', {'title': 'Finance'})

"""
Convert from
============
{
   "Open":{
      "1585699200000":153.0,
      "1585785600000":151.86,
      "1585872000000":155.1,
      "1586131200000":160.32,
      "1586217600000":169.59
   },
   "High":{
      "1585699200000":157.75,
      "1585785600000":155.48,
      "1585872000000":157.38,
      "1586131200000":166.5,
      "1586217600000":170.0
   },
   "Low":{
      "1585699200000":150.82,
      "1585785600000":150.36,
      "1585872000000":152.19,
      "1586131200000":157.58,
      "1586217600000":163.26
   },
   "Close":{
      "1585699200000":152.11,
      "1585785600000":155.26,
      "1585872000000":153.83,
      "1586131200000":165.27,
      "1586217600000":163.49
   },
   "Volume":{
      "1585699200000":57969900,
      "1585785600000":49630700,
      "1585872000000":41243300,
      "1586131200000":67021300,
      "1586217600000":62769038
   },
   "Dividends":{
      "1585699200000":0,
      "1585785600000":0,
      "1585872000000":0,
      "1586131200000":0,
      "1586217600000":0
   },
   "Stock Splits":{
      "1585699200000":0,
      "1585785600000":0,
      "1585872000000":0,
      "1586131200000":0,
      "1586217600000":0
   }
}

To
==

[
   {
      "Date":"2020-04-01 11:00:00",
      "Open":153.0,
      "High":157.75,
      "Low":150.82,
      "Close":152.11,
      "Volume":57969900,
      "Dividends":0,
      "Stock Splits":0
   },
   {
      "Date":"2020-04-02 11:00:00",
      "Open":151.86,
      "High":155.48,
      "Low":150.36,
      "Close":155.26,
      "Volume":49630700,
      "Dividends":0,
      "Stock Splits":0
   },
   {
      "Date":"2020-04-03 11:00:00",
      "Open":155.1,
      "High":157.38,
      "Low":152.19,
      "Close":153.83,
      "Volume":41243300,
      "Dividends":0,
      "Stock Splits":0
   },
   {
      "Date":"2020-04-06 10:00:00",
      "Open":160.32,
      "High":166.5,
      "Low":157.58,
      "Close":165.27,
      "Volume":67021300,
      "Dividends":0,
      "Stock Splits":0
   },
   {
      "Date":"2020-04-07 10:00:00",
      "Open":169.59,
      "High":170.0,
      "Low":163.26,
      "Close":163.49,
      "Volume":62769038,
      "Dividends":0,
      "Stock Splits":0
   }
]


"""