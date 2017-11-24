from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import forms
from . import models


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")





def tangos(request,category_name_slug):
    #Create a context dictionary which we can pass the template rendering engine
    context_dict = {}
    try:
        #can we find a category name slug with given name?
        #If we can't , the .get() method raises a DoesNotExist exception.
        #So the .get() method returns one model instance or raises an exception.
        tango = Tango.objects.get(slug=category_name_slug)
        context_dict['tango_name']= tango.name
        
        #Retrieve all of the associated pages.
        #Note that filter returns >= 1 models instance
        location = Tango_location.objects.filter(category=tango)
        
        #Adds our result list to the tamplate,context under name pages.
        context_dict['Tango_location'] = location
        #We also add the category object from tje database to the context dictionary.
        #We will use this in the template to verify that the category exists.
        context_dict['tango'] =  tango
    except Tango.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)

def index(request):
    #return HttpResponse("Lets Tango with Django" "&#10;" <a href='/rango/about'>About</a>)
    #return HttpResponse("Rango says hey there wolrd !")
    #Construct a dict to pass to the template engine as a context
    #Note the key boldmessage is the same as {{ boldmessage}} inn the emplate.
    tango_list = Tango.objects.order_by('-likes')
    tango_context_dict = {'categories': tango_list}
    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier.
    #Note that the first parameter is the template we wish to use.
    return render(request, 'rango/base.html', tango_context_dict) 
