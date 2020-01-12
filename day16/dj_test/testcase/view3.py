from utils.custom_view import NbView,GetView
from .forms import ProjectForm,CaseForm,UserForm
from .models import Project,Case
from django.views import View
from .utils import Token
from utils.custom_response import NbResponse
from .const import session_pre,token_expire
from django_redis import get_redis_connection

class ProjectView(NbView):
    form_class = ProjectForm
    model_class = Project
    search_field = ['name']
    filter_field = ['id']
    # field = ['name','desc']
    # exclude = ['is_delete']


class CaseView(GetView):
    form_class = CaseForm
    model_class = Case


class LoginView(View):
    def get(self,request):
        form = UserForm(request.GET)
        if form.is_valid():
            user_id = form.cleaned_data.get('u').id
            username = form.cleaned_data.get('u').username
            data  = {"id":user_id,'username':username}
            token = Token.create_token(data)
            r = get_redis_connection()
            key = session_pre + username
            r.set(key,token,token_expire)
            return NbResponse(token=token)
        else:
            return NbResponse(-1,form.error_msg)


