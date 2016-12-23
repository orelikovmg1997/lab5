from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('testApp.views')),
    # url(r'^f', function_view),
    # url(r'^c', ExampleClassBased.as_view()),
    # url(r'^e',ExampleView.as_view()),
    # url(r'^',Basee.as_view()),
]
