from django.shortcuts import render
from django.views import View

# class ConsumerView(View):
#     template_name = 'consumer/list.html'

#     def get(self, request, *args, **kwargs):
#         # case_stage_list = CaseStage.objects.filter(is_deleted=False)
#         # form = CaseStageForm()
#         # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
#         return render(request, self.template_name)
    
# class ManageConsumerView(View):
#     template_name = 'consumer/manage.html'

#     def get(self, request, *args, **kwargs):
#         # case_stage_list = CaseStage.objects.filter(is_deleted=False)
#         # form = CaseStageForm()
#         # return render(request, self.template_name, {"case_stage_list": case_stage_list,'form': form})
#         return render(request, self.template_name)

class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class LogoutView(View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class OfficeUserView(View):
    template_name = 'users/office-setup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class OfficeUserCreateView(View):
    template_name = 'users/manage-office.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class OfficeUserUpdateView(View):
    template_name = 'users/manage-office.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class OfficerUserView(View):
    template_name = 'users/section-setup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class OfficerUserCreateView(View):
    template_name = 'users/manage-section.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class OfficerUserUpdateView(View):
    template_name = 'users/manage-section.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SubHeadUserView(View):
    template_name = 'users/sub-head-setup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SubHeadUserCreateView(View):
    template_name = 'users/manage-sub-head.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SubHeadUserUpdateView(View):
    template_name = 'users/manage-sub-head.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)