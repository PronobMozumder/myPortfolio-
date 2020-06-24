from django.contrib import admin
from. models import myinfo, education, experience, awards, services

admin.site.register(myinfo)

class adminedu(admin.ModelAdmin):
    list_display = ('degreeName', 'uniName', 'year', 'eduDes')
admin.site.register(education, adminedu)

class adminexp(admin.ModelAdmin):
    list_display = ('expName', 'instName', 'year', 'expDes')
admin.site.register(experience, adminexp)

class adminawards(admin.ModelAdmin):
    list_display = ('awardsName',   'year', 'awardsDes')
admin.site.register(awards, adminawards)

class adminservices(admin.ModelAdmin):
    list_display = ('serviceName', 'experienceYear', 'reletedTechnology','serviceDes')
admin.site.register(services, adminservices)

