from django.shortcuts import render, redirect
from .models import Player
from django.http import JsonResponse

def get_next_player():
    # Priority 1: Unshown, not sold players (First Round)
    player = Player.objects.filter(is_sold=False, has_been_shown=False).order_by('id').first()
    if player:
        return player

    # Priority 2: Unsold from last round (Second Round and beyond)
    player = Player.objects.filter(is_unsold=True).order_by('id').first()
    return player

def auction_home(request):
    
    current_player = get_next_player()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'bid':
            current_player.bid_price += 500
            
            current_player.save()
        elif action == 'sold':
            if current_player.bid_price >= 500:
                current_player.is_sold = True
                current_player.has_been_shown=True
                current_player.is_unsold = False  # Just in case
                current_player.save()
                
                return redirect('auction_home')
                
        elif action == 'unsold':
            #  if current_player.bid_price == 500:
                current_player.has_been_shown = True
                current_player.is_unsold = True
                current_player.save()
                return redirect('auction_home')

    context = {
        'player': current_player
    }
    return render(request, 'auction/auction.html', context)