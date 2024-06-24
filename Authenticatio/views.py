from django.shortcuts import render,redirect

from Authenticatio.forms import adduser

from django.contrib import messages

from django.contrib.auth import authenticate,update_session_auth_hash,login,logout

from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm 



def home(request):
  return render(request,'base.html')



def signupuser(request):
  if request.method=='POST':
    signupform=adduser(request.POST)
    if signupform.is_valid():
      signupform.save()
      messages.success(request,"please login here")

      return redirect('login')
  else:
    signupform=adduser()

  return render(request,'signup.html',{'form':signupform})


def loginuser(request):
  if request.method=='POST':
    form=AuthenticationForm(request=request,data=request.POST)
    if form.is_valid():
      users=form.cleaned_data['username']
      userpass=form.cleaned_data['password']
      user=authenticate(username=users,password=userpass)
      if user is not None:
          login(request,user)
          messages.success(request,f"Logged In Successfully {users}")
          return redirect('profile')
      else:
        messages.error(request,'username or password may incorrect,check again!')
        return redirect('login')
  else:
    form=AuthenticationForm()
  return render(request,'login.html',{'form':form,'type':login})
  

def profile(request):
  return render (request,'profile.html')



def userlogout(request):
  logout(request)
  messages.success(request,"Logged Out Successfully")
  return redirect('home')



def oldpass(request):
   if request.method=='POST':
     form=PasswordChangeForm (user=request.user,data=request.POST)
     if form.is_valid():
       form.save()
       update_session_auth_hash(request,form.user)
       messages.success(request,'Your password hasbeen changed successfully!')
       return redirect('profile')
     else:
        messages.error(request,'Your information may incorect!')

   else:
     form=PasswordChangeForm (user=request.user)
   return render(request,'oldpass.html',{"form":form})
     


def newpass(request):
  if request.method=='POST':
    form=SetPasswordForm(user=request.user,data=request.POST)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request,form.user)
      messages.success(request,'Your password hasbeen changed successfully!')
      return redirect('profile')

    else:
       messages.error(request,'Your information may incorect!')


  else:
      form=SetPasswordForm(user=request.user)
  return render(request,'newpass.html',{"form":form})

