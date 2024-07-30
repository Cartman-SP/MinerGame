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
            user.energy = min(user.max_energy, user.energy + 1800 * hours_diff)
        if user.refresh_energy_date < timezone.now().date():
            user.refresh_energy=5
            user.refresh_energy_date = timezone.now().date()
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
def upgrade(request):
    upcost = [0,65,140,350,750,1600,3600,10000,22000,55000,90000,130000,160000,200000,250000,350000]
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
            user.tap_lvl+=1
            user.gpc+=1
    user.save()
    return Response({'balance':user.balance,'tap_lvl':user.tap_lvl,'gpc':user.gpc,'energy_lvl':user.enery_lvl,'max_energy':user.max_energy}, status=status.HTTP_200_OK)


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



