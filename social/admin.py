# -*- coding: utf-8 -*-
from django.contrib import admin
from social.models import FacebookAccessToken, VkontakteAccessToken
from social.wall_post import vk_wall_post, facebook_wall_post
from social.forms import SocialForm


class FacebookAccessTokenAdmin(admin.ModelAdmin):
    list_display = ('facebook_group_id', 'facebook_access_token')
    fieldsets = (
        ('Facebook',  
            {'fields' : ('facebook_group_id', 'facebook_access_token', )}),
        )
    def save_model(self, request, obj, form, change):
        FacebookAccessToken.objects.all().delete()
        obj.save()

class VkontakteAccessTokenAdmin(admin.ModelAdmin):
    list_display = ('vkontakte_group_id','vkontakte_access_token')
    fieldsets = (
        ('Vkontakte',  
            {'fields' : ('vkontakte_group_id', 'vkontakte_access_token', )}),
        )
    def save_model(self, request, obj, form, change):
        VkontakteAccessToken.objects.all().delete()
        obj.save()


admin.site.register(FacebookAccessToken, FacebookAccessTokenAdmin)
admin.site.register(VkontakteAccessToken, VkontakteAccessTokenAdmin)


class SocialAdminModel(admin.ModelAdmin):
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(SocialAdminModel, self).get_form(request, obj, **kwargs)
        form.base_fields.update(SocialForm.base_fields)
        return form

    def save_model(self, request, obj, form, change):
        obj.save()
        if form.cleaned_data.get('facebook_wall', None):
            picture = None
            if form.cleaned_data.get('image', None):
                picture = "http://www.greenparty.ru/media/%s" % form.cleaned_data['image']
            facebook_wall_post(
                name = form.cleaned_data.get('name', None),
                message = form.cleaned_data.get('description', None), 
                picture = picture,
                link='http://'+request.META['HTTP_HOST']+'/news/'+str(obj.id)
                # Todo: replace to get_obscure_url
                # link = 'http://www.example.com/news/'+str(obj.id),
                )
        if form.cleaned_data.get('vk_wall', None):
            vk_wall_post(
                message = form.cleaned_data.get('description', None), 
                link='http://'+request.META['HTTP_HOST']+'/news/'+str(obj.id)
                # link = 'http://www.greenparty.ru/news/'+str(obj.id)
                # Todo: replace to get_obscure_url
                )