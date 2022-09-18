from django.http import HttpResponse

# create a function
def geeks_view(request):
	
	return HttpResponse("<h1>Welcome to GeeksforGeeks</h1>")
