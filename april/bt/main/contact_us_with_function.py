def contact_us(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.send_,mail()
            return HttpResponseRedirect('/')
    else:
        form = forms.ContactForm()
    return render(request, 'contact_form.html', { 'form': form })