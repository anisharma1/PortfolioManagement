from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from .models import Stocks,CurrentHoldings,Transaction,ValuationStocks

# Create your views here.
def register(request) :
	"""Register a new user"""
	if request.method != 'POST':
		#Display blank registration form.
		form = UserCreationForm()
	else:
		#Process completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#Log the user in and redirect to home page
			login(request, new_user)
			return redirect('PortfolioManagerHome:index')
	#Display a blank or invalid form
	context = {'form':form}
	return render(request, 'registration/register.html', context)

def logout(request):
  return render(request, 'portfolio/logout.html')


def dashboard(request):
  """Fetches stock information for logged in user """
#   filters users according to logged in user
  curUser=Users.objects.filter(name=request.user.username)

  return render(request,'portfolio/dashboard.html',{'curUser' :curUser})

def stockprofiles(request):
  """"Fetches the stocks of logged in user"""
  #   filters users according to logged in user
  #uid=Users.objects.filter(name=request.user.username)[0].userid
  #ch=CurrentHoldings.objects.filter(userid=uid)

  return render(request, 'portfolio/stockprofiles.html')

def stocks(request):
  """Fetches historical stocks data"""
  stock_list = Stocks.objects.all()
  red=ValuationStocks.objects.filter(date='2018-02-27')
  return render(request, 'portfolio/stocks.html', {'Stocks': stock_list,'ValuationStocks':red})



# To be impeleted


# def deletestocks(request, slug):
#   return render(request, 'stockprofiles.html')


# def addstocks(request, slug):
#   return render(request, 'stockprofiles.html')
