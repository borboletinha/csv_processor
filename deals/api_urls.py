from django.urls import path

from deals.views import DealView

app_name = 'api'
urlpatterns = [
    path('upload-file/', DealView.as_view({'post': 'create'}), name='upload_file'),
    path('get-processed-data/', DealView.as_view({'get': 'list'}), name='get_processed_data')
]
