from django.core.management.base import BaseCommand
from notify import create_subscriber,create_workflows

class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write(self.style.SUCCESS('Triggering Notification...'))
        #div = create_subscriber()
        #send_notification()
        create_workflows()
        
