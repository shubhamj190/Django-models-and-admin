from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .models import User, ProductInCart,Product,Cart, Order, Deals
from django.contrib.auth.models import Permission, User
# Register your models here.


admin.site.register(Product)
admin.site.register(ProductInCart)
# admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Deals)

class prodeuctInline(admin.TabularInline):
    model=ProductInCart

class DealInline(admin.TabularInline):
    model=Deals.user.through #hrough is used for ManyToManyfield

# class cartInline(admin.TabularInline):
    # model=Cart
    pass

class CustomUserAdmin(UserAdmin):
    model=User
    list_display=('username','email', 'is_active', 'is_staff', 'is_superuser',)
    list_filter=('username', 'is_active','is_staff','is_superuser')
    fieldsets=(
        (None,{'fields':('username','password',)}),
        ('Permission',{'fields':('is_staff',('is_active','is_superuser') )}),
        ('Important dates',{'fields':('date_joined','last_login')}),
        ('Advance options',{
            'classes':('collapse',),
            'fields':('groups','user_permissions')
        }),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('username', 'password1','password2','is_active', 'is_staff','groups',)
        }),
    )
    # inlines=[cartInline,DealInline]
    def get_cart(self, obj):
        return obj.cart
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class dealAdmin(admin.ModelAdmin):
    inlines=[DealInline,]
    exclude='user'

@admin.register(Cart) #through register decorator
class CartAdmin(admin.ModelAdmin):
    model=Cart
    list_display=('staff','user',) 
    list_filter=['user',]
    search_fields=['user__username'] # "__" means refering to foreignkey or onetoonefiled
    fieldsets=(
        ("None",{'fields':('user',),}),
    )
    inlines=[prodeuctInline]

    def staff(self, obj):
        return obj.user.is_staff  #here user__is_staff will not work   
    staff.admin_order_user='user__is_staff'
    staff.short_description='staff user'
    list_filter=('user','user__is_staff',)

