from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def indexs(request):
    return render(request,'index.html')


def mainpage(request):
    return render(request,'landingPage.html')

def flightfav(request):
    return render(request,'Flightfav.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def basicInfo(request):
    return render(request,'BasicInfo.html')

def customerAbout(request):
    return render(request,'CustomerAbout.html')

def customerProfile(request):
    return render(request,'CustomerProfile.html')

def customerService(request):
    return render(request,'CustomerService.html')

def flightDetails(request):
    return render(request,'FlightDetails.html')

def flightFinalPayment(request):
    return render(request,'FlightFinalPayment.html')


def flightReservation(request):
    return render(request,'FlightReservation.html')

def flightSearch(request):
    return render(request,'FlightSearch.html')

def flightTicket(request):
    return render(request,'FlightTicket.html')

def helpAndFeedback(request):
    return render(request,'Help&Feedback.html')

def hotelBooking(request):
    return render(request,'HotelBooking.html')

def hotelF(request):
    return render(request,'HotelF.html')

def hotelFull(request):
    return render(request,'HotelFull.html')

def hotelInfo(request):
    return render(request,'HotelInfo.html')

def hotelReservation(request):
    return render(request,'HotelReservation.html')

def hotelS(request):
    return render(request,'HotelS.html')

def hotelSandR(request):
    return render(request,'HotelS&R.html')

@csrf_exempt
def login(request):
    return render(request,'login.html')

def pageError(request):
    return render(request,'PageError.html')

def paymentInfo(request):
    return render(request,'PaymentInfo.html')

def profilePreference(request):
    return render(request,'PreferenceProfile.html')

def register(request):
    return render(request,'register.html')

def settingProfile(request):
    return render(request,'SettingProfile.html')

def trackBooking(request):
    return render(request,'TrackingBooking.html')

def footer(request):
    return render(request,'footer.html')

def base(request):
    return render(request,'base.html')


