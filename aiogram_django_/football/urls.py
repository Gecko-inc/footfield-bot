from django.urls import path

from football.views import FootballFieldView, FilterAreaAPI, FilterSizeAPI, GetConfigView, ImageView

app_name = "football_fields"

urlpatterns = [
    path("get_config/", GetConfigView.as_view(), name="config"),
    path("images/", ImageView.as_view(), name="images"),
    path("all_fields/", FootballFieldView.as_view(), name="all_football_fields"),
    path("filter_area/<str:area>/", FilterAreaAPI.as_view(), name="filter_area"),
    path("filter_size/<str:size>/", FilterSizeAPI.as_view(), name="filter_size")
]
