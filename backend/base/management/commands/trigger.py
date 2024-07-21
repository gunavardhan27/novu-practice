from django.core.management.base import BaseCommand
from notify import create_subscriber
import novu
class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write(self.style.SUCCESS('Triggering Notification...'))
        div = create_subscriber()
        
