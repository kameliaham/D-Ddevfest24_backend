from django.contrib import admin
from .models import Machine, WeldingRobot, StampingPress, PaintingRobot, AGV, CNCMachine, LeakTestMachine

admin.site.register(Machine)
admin.site.register(WeldingRobot)
admin.site.register(StampingPress)
admin.site.register(PaintingRobot)
admin.site.register(AGV)
admin.site.register(CNCMachine)
admin.site.register(LeakTestMachine)


