from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuestionView

question_list = QuestionView.as_view({
    'post': 'create',
    'get': 'list'
})

question_detail = QuestionView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('question/', question_list, name='question_list'),
    path('question/<int:pk>/', question_detail, name='question_detail'),
])
