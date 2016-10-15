from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from post.models import textpost
from django.contrib.auth.models import User
from .models import Profile,ProfilePictures
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ProfileForm, ProfilePicturesForm
from django.contrib import messages

from django.views.generic import FormView, View


@login_required
def my_posts(request):

    posts = textpost.objects.filter(user=request.user).order_by("-time_stamp")

    context = {
        "all_post":posts,
        }
    return render(request, 'profile/postprofile.html',context)

@login_required



def userprofile(request):
    profile=Profile.objects.filter(user=request.user)
    pictures=ProfilePictures.objects.filter(user=request.user)
    context ={"profile":profile, "pictures":pictures,}
    return render(request,'profile/profilehome.html', context)


class EditUserProfileForm(FormView):
    form_class = ProfilePicturesForm
    template_name = 'profile/profileedit.html'
    success_url = '/profile'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        profile=Profile.objects.filter(user=request.user)
        pictures=ProfilePictures.objects.filter(user=request.user)

        if request.method == 'POST':
            pictures_form=ProfilePicturesForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                #for f in files:
                instance= ProfilePictures(user=request.user,pictures = request.FILES['pictures'])
                instance.save()
                return self.form_valid(form)
            context = {'pictures':pictures,'pictures_form':pictures_form,}
            return render(request, 'profile/profileedit.html', context,)

@login_required
def profile_formedit(request):
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/profile')
    context = {'user_form':user_form,
                'profile_form':profile_form,
                }


    return render(request,'profile/profileedit.html', context)

@login_required
def profileimage_delete(request, slug=None):
	instance = get_object_or_404(ProfilePictures, slug=slug)
	instance.delete()



        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            pictures_form=ProfilePicturesForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                if form.is_valid():

                    for f in files:

                    # instance= ProfilePictures(user=request.user,pictures = request.FILES['pictures'])
                    # instance.save()
                    # messages.success(request, ('Your profile was successfully updated!'))
                        return self.form_valid(form)
                    else:
                        return self.form_invalid(form)
                    return HttpResponseRedirect('/profile')
                else:
                    messages.error(request, _('Please correct the error below.'))
            else:
                messages.error(request, _('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            pictures_form=ProfilePicturesForm()
        return render(request, 'profile/profileedit.html', {
        'pictures':pictures,
        'user_form': user_form,
        'profile_form': profile_form,
        'pictures_form':pictures_form,
    })

def profileimage_delete(request, slug=None):
	instance = get_object_or_404(ProfilePictures, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("userprofile:profile")
