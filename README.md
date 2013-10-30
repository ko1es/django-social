django-social
===================

Django social plugin made for simple integration ur django admin app with Vkontakte and Facebook

Installation
============

    
    pip install git+git://github.com/ko1es/django-social.git
    

Add 'social' to your INSTALLED_APPS in settigs.py

    python ./manage.py migrate

After that you can see two new sections in your admin app. Add there VKontakte and Facebook access tokens of your group.

Basic usage
===========

Use it like a regular admin model class :
    
    from social.admin import SocialAdminModel

    class FooAdmin(SocialAdminModel):
        list_display = ('name',)

    admin.site.register(Foo)

After that during create or update your Foo object u can see Checkboxes for import in Vkontakte and Facebook.    
