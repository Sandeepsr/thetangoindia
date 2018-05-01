from django.views import generic
from datetime import date , datetime, timedelta
from profiles.models import Tango_Events,TangoCommunityInfo,FBEvents
import django_tables2 as tables


tango_location = {'264587550321500':'Hyderabad', '527770257327317': 'Bangalore', '1636178923304872':'Mumbai', '100006844149398':'Chennai', '197346010313291': 'Auroville-Pondichery', '305372292817505':'Pune','107857822580692' : 'Mumbai Tango', '1099207956812482': 'Bangalore - Elcabeco' , '7213847061':'New Delhi Tango'}

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

    
    
class PastEventsPage(generic.TemplateView):
    startdate = datetime.today()
    enddate = startdate + timedelta(days=8)
    #context_object_name = 'Tango-Events1'
    sdate = startdate.strftime("%Y-%m-%d %H:%M")
    edate = enddate.strftime("%Y-%m-%d %H:%M")                            
    template_name = "Past-Events.html"
    
    def get_context_data(self, **kwargs):
        context = super(PastEventsPage,self).get_context_data(**kwargs)
        context['PastEvents'] =  FBEvents.objects.filter(Start_Time__lt=self.sdate)
        return context
  
class EventsPage(generic.TemplateView):
    #model = Tango_Events
    startdate = datetime.today()
    enddate = startdate + timedelta(days=8)
    #context_object_name = 'Tango-Events1'
    sdate = startdate.strftime("%Y-%m-%d %H:%M")
    edate = enddate.strftime("%Y-%m-%d %H:%M")                            
    template_name = "Tango-Events.html"
    
    def get_context_data(self, **kwargs):
        context = super(EventsPage,self).get_context_data(**kwargs)
        context['Next2weeks'] = FBEvents.objects.filter(Start_Time__range=[self.sdate, self.edate]).distinct()
        context['FutureEvents'] =  FBEvents.objects.filter(Start_Time__gte=self.edate)
        #context['PastEvents'] =  FBEvents.objects.filter(Start_Time__lt=self.sdate)
        context['tango_location'] = tango_location
        return context
    
#class EventsPage(generic.ListView):
    #model = Tango_Events
 #   context_object_name = 'Tango-Events'
  #  queryset = Tango_Events.objects.order_by('-created_time').distinct()[:30]
   # template_name = "Events.html"  
    
#class Events(generic.ListView):
    #model = Tango_Events
    #context_object_name = 'Events'
    #queryset = FBEvents.objects.all()
    #template_name = "Events.html"

class TangoHyderabadPage(generic.ListView):
    #model = Tango_Events
    context_object_name = 'Tango-In-Hyderabad'
    queryset = TangoCommunityInfo.objects.all()[0]
    template_name = "Tango-In-Hyderabad.html"
    #0
class TangoMumbai(generic.ListView):
    #model = Tango_Events
    context_object_name = 'Tango_Mumbai'
    queryset = TangoCommunityInfo.objects.all()[1]
    template_name = "Tango-In-Mumbai.html"
    #1
class TangoNewDelhiPage(generic.ListView):
    context_object_name = 'Tango-In-Delhi'
    queryset = TangoCommunityInfo.objects.all()[2]
    template_name = "Tango-In-Delhi.html"
    #2
class TangoBangalorePage(generic.ListView):
    context_object_name = 'Tango-In-Bangalore'
    queryset = TangoCommunityInfo.objects.all()[3]
    template_name = "Tango-In-Bangalore.html"
    #3
class TangoAurovillePage(generic.ListView):
    context_object_name = 'Tango-In-Auroville-Pondicherry'
    queryset = TangoCommunityInfo.objects.all()[4]
    template_name = "Tango-In-Auroville-Pondicherry.html"
    #4
class TangoChennaiPage(generic.ListView):
    context_object_name = 'Tango-In-Chennai'
    queryset = TangoCommunityInfo.objects.all()[5]
    template_name = "Tango-In-Chennai.html"
    #5
class TangoPunePage(generic.ListView):
    context_object_name = 'Tango-In-Pune'
    queryset = TangoCommunityInfo.objects.all()[6]
    template_name = "Tango-In-Pune.html"
    #6
class TangoElCabeceoPage(generic.ListView):
    context_object_name = 'Tango-In-Bangalore-El-Cabeceo'
    queryset = TangoCommunityInfo.objects.all()[7]
    template_name = "Tango-In-Bangalore-El-Cabeceo.html"
    #7
class TangoMumbaiBTangoConscious(generic.ListView):
    context_object_name = 'Tango-In-Mumbai-BTangoConscious'
    queryset = TangoCommunityInfo.objects.all()[8]
    template_name = "Tango-In-Mumbai-BTangoConscious.html"
    #8

class TangoEssentials(generic.TemplateView):
    template_name = "Tango-Essentials.html"

class TangoRadio(generic.TemplateView):
    template_name = "Tango-Radio.html"
    
class TangoSitemap(generic.TemplateView):
    template_name = "sitemap_location.xml"

class LegalTC(generic.TemplateView):
    template_name = "legal.html"

#class BannerPage(generic.TemplateView):
    #template_name = "banner.jpg"
