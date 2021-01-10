from django.shortcuts import render, redirect
from .forms import BarcodeForm


def barcode_generate(request):
    form = BarcodeForm()
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            temp = form.save()
            print(temp)
            # barcode_download(request, temp)
            # return redirect('barcode-download', temp)
            return redirect(f"http://127.0.0.1:8000/media/images/{temp}.png")
    context = {'form': form}
    return render(request, 'products/bar_generate.html', context)


# def barcode_download(request, temp):
#     return redirect(f"http://127.0.0.1:8000/media/images/{temp}.png")
#
# # img = BarcodeForm.objects.all()
#     # context = {'img': img}
#     # return render(request, 'products/bar_download.html', context)