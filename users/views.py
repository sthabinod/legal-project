from django.shortcuts import render
from django.views import View

class ConsumerView(View):
    template_name = 'consumer/list.html'

    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)
    
class ManageConsumerView(View):
    template_name = 'consumer/manage.html'

    def get(self, request, *args, **kwargs):
        # case_stage_list = CaseStage.objects.filter(is_deleted=False)
        # form = CaseStageForm()
        # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
        return render(request, self.template_name)