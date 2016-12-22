from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views import View

# def function_view(request):
#     return HttpResponse ('response from function view')

# class ExampleClassBased(View):
#     def get(selfsekf, request):
#         return HttpResponse('response from class based view')
#
# class ExampleView(View):
#     def get(self, request):
#         return render (request, 'example.html', {'my_variable' : 'Этот текст подставится вместо переменной'})
#
# class Basee(View):
#     def get(self, request):
#         return render(request, 'bootstrap.html')

class OrdersView(View):
    orders = [
        {'title': 'title1', 'id': 1,'text': 'text1'},
        {'title': 'title2', 'id': 2, 'text': 'text2'},
        {'title': 'title3', 'id': 3, 'text': 'text3'},
        {'title': 'title4', 'id': 4, 'text': 'text4'},
        {'title': 'title5', 'id': 5, 'text': 'text5'},
        {'title': 'title6', 'id': 6, 'text': 'text6'},
        {'title': 'title7', 'id': 7, 'text': 'text7'},
        {'title': 'title8', 'id': 8, 'text': 'text8'},
        {'title': 'title9', 'id': 9, 'text': 'text9'},
        {'title': 'title10', 'id': 10, 'text': 'text10'},
        {'title': 'title11', 'id': 11, 'text': 'text12'},
    ]
    def get(self, request):
        data = {
            'orders': OrdersView.orders,
            'count' : len(OrdersView.orders),
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {

            'order': {
                'id': id,
                'title': OrdersView.orders[int(id)-1].get('title'),
                'text': OrdersView.orders[int(id)-1].get('text'),
            }
        }
        return render(request, 'order.html', data)