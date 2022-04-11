from django.shortcuts import render
from django.views import View
from main_app.forms import WriteLineForm


class MainView(View):

    def get(self, request):
        context = {
            'form': WriteLineForm(),
            'title': "Form",
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = WriteLineForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            print(f"{firstname}|{lastname}|{age}|{comment}")
            data["title"] = "Profile"
            return render(request, 'profile.html', data)
