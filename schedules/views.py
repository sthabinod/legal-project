# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
# from .forms import 
# from .models import

class ScheduleFourView(View):
    template_name = 'schedules/scheduleFour.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleFourAView(View):
    template_name = 'schedules/scheduleFourA.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleFiveView(View):
    template_name = 'schedules/scheduleFive.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleSixView(View):
    template_name = 'schedules/scheduleSix.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleSevenView(View):
    template_name = 'schedules/scheduleSeven.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleEightView(View):
    template_name = 'schedules/scheduleEight.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleNineAView(View):
    template_name = 'schedules/scheduleNineA.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleNineBView(View):
    template_name = 'schedules/scheduleNineB.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleTenView(View):
    template_name = 'schedules/scheduleTen.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleElevenView(View):
    template_name = 'schedules/scheduleEleven.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleTwelveView(View):
    template_name = 'schedules/scheduleTwelve.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleThirteenView(View):
    template_name = 'schedules/scheduleThirteen.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleFourteenView(View):
    template_name = 'schedules/scheduleFourteen.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)

class ScheduleNineteenView(View):
    template_name = 'schedules/scheduleNineteen.html'
                                            
    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)