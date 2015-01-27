__author__ = 'mbamiguel'

from django.apps import AppConfig
from django.conf import settings
from views import MyAccountView

class YawadminAppConfig(AppConfig):
    name = "yawdadmin"
    verbose_name = "Yawd Admin"

    def ready(self):
        #load the modelform if it's a string
        ADMIN_USER_MODELFORM = getattr(settings, 'ADMIN_USER_MODELFORM',
                'yawdadmin.admin_forms.AdminUserModelForm')

        if isinstance(ADMIN_USER_MODELFORM, str):
            from django.utils.importlib import import_module
            _user_modelform_split = ADMIN_USER_MODELFORM.split('.')
            _user_modelform_module = import_module('.'.join(_user_modelform_split[:-1]))
            ADMIN_USER_MODELFORM = getattr(_user_modelform_module, _user_modelform_split[-1])
            MyAccountView.form_class = ADMIN_USER_MODELFORM

        #pass
            print "Ready"
