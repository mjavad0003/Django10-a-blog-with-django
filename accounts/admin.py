from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostomUserChangeForm,CostomUserCreationForm
from .models import CostomUser

class CostomUserAdmin(UserAdmin):
    add_form = CostomUserCreationForm
    form= CostomUserChangeForm
    model = CostomUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
        'about',
        'photo',
    ]

    fieldsets = UserAdmin.fieldsets + ((None,{"fields":('age','about','photo',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields":('age','about','photo',)}),)

admin.site.register(CostomUser,CostomUserAdmin)