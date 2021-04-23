from django.shortcuts import render

# Create your views here.


def render_home_page(request):
    """

    :param request:
    :return:
    """
    return render(request, 'homepage/homepage.html')
