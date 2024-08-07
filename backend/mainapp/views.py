from datetime import timedelta
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import TelegramUserSerializer, RoomSerializer
import requests 



BOT_TOKEN = '6705532890:AAG7x2iBNy9GdCLZWqqNF1LunZtev7_yOmA'

def get_user_profile_photo(bot_token, user_id):
    url = f'https://api.telegram.org/bot{bot_token}/getUserProfilePhotos'
    params = {'user_id': user_id}
    response = requests.get(url, params=params)
    data = response.json()

    if data['ok']:
        photos = data['result']['photos']
        if photos:
            file_id = photos[0][0]['file_id']
            file_info_url = f'https://api.telegram.org/bot{bot_token}/getFile'
            file_info_params = {'file_id': file_id}
            file_info_response = requests.get(file_info_url, params=file_info_params)
            file_info_data = file_info_response.json()

            if file_info_data['ok']:
                file_path = file_info_data['result']['file_path']
                file_url = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'
                return file_url
    return None

@api_view(['GET'])
def get_or_create_user(request):
    print(request.query_params)
    user_id = request.query_params.get('id')
    username = request.query_params.get('first_name')
    usertag = request.query_params.get('username')
    start = request.query_params.get('start')
    is_premium = request.query_params.get('is_premium')

    print(f"user_id: {user_id}, username: {username}, usertag: {usertag}")

    if not user_id or not username or not usertag:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = TelegramUser.objects.get(user_id=user_id)
    except TelegramUser.DoesNotExist:
        user = TelegramUser.objects.create(
            user_id=user_id,
            username=username,
            usertag=usertag
        )
        try:
            inviter = TelegramUser.objects.get(user_id=start)
            referal = Referal.objects.create(
                inviter=inviter,
                user=user
            )
            if(inviter.friends_invited<3):
                inviter.balance += 4000
            inviter.friends_invited+=1
            inviter.save()
            referal.save()
        except:
            pass

    if user:
        date_difference = timezone.now().date() - user.daily_reward_date
        if user.daily_reward_date<timezone.now().date():
            if date_difference > timedelta(days=1):
                user.daily_reward_day = 0
            user.daily_reward_claimed = False

        if(is_premium=='“true”'):
            user.ispremium = True
        else:
            user.ispremium = False
        photo_url = get_user_profile_photo(BOT_TOKEN, user_id)
        if photo_url:
            user.photo_url = photo_url
            user.save()
        
        # Если last_login не Null, обновляем баланс и энергию
        if user.last_login:
            time_diff = timezone.now() - user.last_login
            hours_diff = time_diff.total_seconds() / 3600

            # Обновляем баланс и энергию
            user.balance += user.gph * hours_diff
            user.energy = min(user.max_energy, user.energy + 1800 * hours_diff)
        if user.refresh_energy_date < timezone.now().date():
            user.refresh_energy = 5
            user.refresh_energy_date = timezone.now().date()
        # Обновляем last_login
        user.last_login = timezone.now()
        user.save()

    user_serializer = TelegramUserSerializer(user)
    response_data = {
        "user": user_serializer.data,
    }

    return Response(response_data, status=status.HTTP_200_OK)









@api_view(['POST'])
def set_max_energy(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    if(user.refresh_energy==5):
        user.refresh_energy_date = timezone.now()
    user.energy = user.max_energy
    user.refresh_energy-=1
    user.save()
    return Response({"success": "Mining started"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def lvlup(request):
    multiples = [0, 1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 3]
    uptap = [0,0,1,3,5,7,10,13,17,20,35]
    user_id = request.data.get('user_id')
    lvl = request.data.get('lvl')
    user = TelegramUser.objects.get(user_id=user_id)    
    user.lvl = lvl
    user.gpc +=uptap[int(lvl)]
    user.modifier = multiples[int(lvl)]
    user.max_energy+=250
    user.save()
    return Response({'gpc':user.gpc,'modifier':user.modifier,'max_energy':user.max_energy}, status=status.HTTP_200_OK)



@api_view(['POST'])
def upgrade(request):
    upcost = [0,1400,3500,7500,10600,30600,100000,220000,550000,900000,1300000,1600000,2000000,2500000,3500000]
    uptap = [0,2,2,4,4,6,6,7,7,8,8,10,10,15,15]
    user_id = request.data.get('user_id')
    print(user_id)
    user = TelegramUser.objects.get(user_id=user_id)
    num = request.data.get('num')
    if(num==1):
        cost = upcost[user.enery_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.enery_lvl+=1
            user.max_energy+=250
    else:
        cost = upcost[user.tap_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.gpc+=uptap[user.tap_lvl]
            user.tap_lvl+=1
    user.save()
    return Response({'balance':user.balance,'tap_lvl':user.tap_lvl,'gpc':user.gpc,'energy_lvl':user.enery_lvl,'max_energy':user.max_energy,'lvl':user.lvl}, status=status.HTTP_200_OK)


@api_view(['POST'])
def start_mining(request):
    user_id = request.data.get('user_id')
    if not user_id:
        return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = TelegramUser.objects.get(user_id=user_id)
    except TelegramUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.update_mining_end()

    return Response({"success": "Mining started", "mining_end": user.mining_end}, status=status.HTTP_200_OK)

@api_view(['POST'])
def upgrade_mining(request):
    upcost = [0,30000,115000,350000,1000000,2950000,8200000,23400000,58500000,175500000,470000000]
    user_id = request.data.get('user_id')
    print(user_id)
    user = TelegramUser.objects.get(user_id=user_id)
    num = request.data.get('num')
    if(num==1):
        cost = upcost[user.enery_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.enery_lvl+=1
    else:
        cost = upcost[user.tap_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.tap_lvl+=1
            user.gpc+=1
    user.save()
    return Response({'balance':user.balance,'tap_lvl':user.tap_lvl,'gpc':user.gpc,'energy_lvl':user.enery_lvl,'max_energy':user.max_energy}, status=status.HTTP_200_OK)


@api_view(['GET'])
def check_subscribe(request):
    bot_token = '6705532890:AAG7x2iBNy9GdCLZWqqNF1LunZtev7_yOmA'
    channel_id = '@MinerGam3'
    user_id = request.query_params.get('user_id')
    print(user_id)
    url = f'https://api.telegram.org/bot{bot_token}/getChatMember'
    params = {
        'chat_id': channel_id,
        'user_id': user_id
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    user = TelegramUser.objects.get(user_id=user_id)
    if data['ok']:
        state = data['result']['status']
        if state in ['member', 'administrator', 'creator']:
            if(user.subscribe_money_gived):
                print(321)
                user.subscribed=True
                user.save()
                return Response({'status':user.subscribed,'balance':user.balance}, status=status.HTTP_200_OK)
            else:
                print(123)
                user.subscribed=True
                user.balance+=5000
                user.subscribe_money_gived=True
                user.save()
                return Response({'status':user.subscribed,'balance':user.balance}, status=status.HTTP_200_OK)
        else:
            user.subscribed = False
            user.save()
            return Response({'status':user.subscribed,'balance':user.balance}, status=status.HTTP_200_OK)
    else:
        return Response({'status':user.subscribed,'balance':user.balance}, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_friends(request):
    user_id = request.query_params.get('user_id')
    try:
        user = TelegramUser.objects.get(user_id=user_id)
    except TelegramUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    referals = Referal.objects.filter(inviter=user)
    friends = [referal.user for referal in referals]
    
    # Debug prints
    for friend in friends:
        print(friend.username)
    print(friends)
    
    serializer = TelegramUserSerializer(friends, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def claim_reward(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    gifts = [500,1000,3000,5000,10000,20000,40000,100000]
    if(not(user.daily_reward_claimed)):
        user.balance += gifts[user.daily_reward_day]
        user.daily_reward_claimed = True
        user.daily_reward_date = timezone.now().date()
        user.daily_reward_day+=1
    user.save()
    return Response({"balance": user.balance, "daily_reward_claimed": user.daily_reward_claimed,"daily_reward_day": user.daily_reward_day,}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_top(request):
    user_id = request.query_params.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    
    # Получаем первых 7 пользователей, отсортированных по balance
    top = TelegramUser.objects.order_by('-balance')[:7]
    
    # Определяем позицию текущего пользователя
    user_position = TelegramUser.objects.filter(balance__gt=user.balance).count() + 1
    
    # Сериализуем данные
    serializer = TelegramUserSerializer(top, many=True)
    
    # Возвращаем данные вместе с позицией пользователя
    response_data = {
        "top_users": serializer.data,
        "user_position": user_position
    }
    
    return Response(response_data, status=status.HTTP_200_OK)