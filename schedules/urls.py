# urls.py
from django.urls import path
from .views import (
    ScheduleFourView,
    ScheduleFourAView,
    ScheduleFiveView,
    ScheduleSixView,
    ScheduleSevenView,
    ScheduleEightView,
    ScheduleNineAView,
    ScheduleNineBView,
    ScheduleTenView,
    ScheduleElevenView,
    ScheduleTwelveView,
    ScheduleThirteenView,
    ScheduleFourteenView,
    ScheduleNineteenView
)

urlpatterns = [
    path('schedule_four/', ScheduleFourView.as_view(), name='schedule_four'),
    path('schedule_fourA/', ScheduleFourAView.as_view(), name='schedule_fourA'),
    path('schedule_five/', ScheduleFiveView.as_view(), name='schedule_five'),
    path('schedule_six/', ScheduleSixView.as_view(), name='schedule_six'),
    path('schedule_seven/', ScheduleSevenView.as_view(), name='schedule_seven'),
    path('schedule_eight/', ScheduleEightView.as_view(), name='schedule_eight'),
    path('schedule_nineA/', ScheduleNineAView.as_view(), name='schedule_nineA'),
    path('schedule_nineB/', ScheduleNineBView.as_view(), name='schedule_nineB'),
    path('schedule_Ten/', ScheduleTenView.as_view(), name='schedule_ten'),
    path('schedule_eleven/', ScheduleElevenView.as_view(), name='schedule_eleven'),
    path('schedule_twelve/', ScheduleTwelveView.as_view(), name='schedule_twelve'),
    path('schedule_thirteen/', ScheduleThirteenView.as_view(), name='schedule_thirteen'),
    path('schedule_fourteen/', ScheduleFourteenView.as_view(), name='schedule_fourteen'),
    path('schedule_nineteen/', ScheduleNineteenView.as_view(), name='schedule_nineteen'),
]
