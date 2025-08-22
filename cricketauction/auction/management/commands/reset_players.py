from django.core.management.base import BaseCommand
from auction.models import Player

class Command(BaseCommand):
    help = 'Reset auction status of all players'

    def handle(self, *args, **kwargs):
        Player.objects.update(
            is_sold=False,
            has_been_shown=False,
            is_unsold=False,
            bid_price=500  # Optional: reset bid price too if needed
        )
        self.stdout.write(self.style.SUCCESS('✅ Successfully reset all player statuses!'))
