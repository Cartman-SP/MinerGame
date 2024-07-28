from datetime import timedelta
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TelegramUser, Room
from .serializers import TelegramUserSerializer, RoomSerializer

@api_view(['GET'])
def get_or_create_user(request):
    print(request.query_params)
    user_id = request.query_params.get('id')
    username = request.query_params.get('first_name')
    usertag = request.query_params.get('username')

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
    
    if user:
        # Если last_login не Null, обновляем баланс и энергию
        if user.last_login:
            time_diff = timezone.now() - user.last_login
            hours_diff = time_diff.total_seconds() / 3600

            # Обновляем баланс и энергию
            user.balance += user.gph * hours_diff
            user.energy = min(2000, user.energy + 1800 * hours_diff)

        # Обновляем last_login
        user.last_login = timezone.now()
        user.save()

        # Создаём комнаты, если их нет
        if not user.room_set.exists():
            for idx, lvl in enumerate([1, 2], start=1):
                Room.objects.create(
                    user_id=user.id,  # Ассоциируем комнату с пользователем
                    lvl=lvl,
                )
    else:
        # Обрабатываем случай, если создание пользователя не удалось
        return Response({"error": "Failed to create user"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Сериализуем пользователя и его комнаты
    user_serializer = TelegramUserSerializer(user)
    room_serializer = RoomSerializer(user.room_set.all(), many=True)

    # Комбинируем данные пользователя и комнат в ответ
    response_data = {
        "user": user_serializer.data,
        "rooms": room_serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def upgrade_room(request):
    type = request.data.get('type')
    room_id = request.data.get('room_id')
    upgrade_cost = request.data.get('upgrade_cost')
    room = Room.objects.get(id=room_id)
    user = room.user
    balance = user.balance
    if(balance>upgrade_cost):
        print(room_id)
        room = Room.objects.get(id=room_id)
        if(type=='comp'):
            room.comp_lvl +=1
        elif(type=='mic'):
            room.micro_lvl +=1
        elif(type=='webcam'):
            room.webcam_lvl +=1
        room.user.balance -= int(upgrade_cost)
        room.user.save()
        room.save()
        return Response({'status':'Ok'}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Not enoughbalance"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def lvl_up(request):
    user_id =  request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    lvl = request.data.get('lvl')
    user.lvl = lvl
    print(123)
    user.save()
    print(user.lvl)
    if(lvl==2):
        if(len(Room.objects.filter(user=user,lvl=3))==0):
            room = Room.objects.create(lvl=3,user=user)
            room.save()
    if(lvl==3):
        if(len(Room.objects.filter(user=user,lvl=4))==0):
            room = Room.objects.create(lvl=4,user=user)
            room.save()
    if(lvl==4):
        if(len(Room.objects.filter(user=user,lvl=5))==0):
            room = Room.objects.create(lvl=5,user=user)
            room.save()
    if(lvl==5):
        if(len(Room.objects.filter(user=user,lvl=6))==0):
            room = Room.objects.create(lvl=6,user=user)
            room.save()

    return Response({'status':'Ok'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def upgrade_coin(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    gpc = user.gpc
    context = {}
    upgrade_costs = {
        2: 5000,
        3: 10000,
        5: 20000,
        8: 50000,
        12: 100000,
        20: 250000,
        30: 500000,
        50: 1000000,
        100: 2500000
    }
    new_gpc_values = {
        2: 3,
        3: 5,
        5: 8,
        8: 12,
        12: 20,
        20: 30,
        30: 50,
        50: 100,
        100: 150
    }

    if gpc in upgrade_costs:
        cost = upgrade_costs[gpc]
        if user.balance >= cost:
            user.balance -= cost
            user.gpc = new_gpc_values[gpc]
            context['gpc'] = user.gpc
            context['cost'] = cost
            user.save()
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Not enough balance"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Invalid GPC value"}, status=status.HTTP_400_BAD_REQUEST)



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



