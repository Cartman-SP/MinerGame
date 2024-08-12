from datetime import timedelta
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import requests
import re


BOT_TOKEN = '7233799288:AAF0WYqgm5H0pgL5t66nip78HQfBHxF8ThA'

@api_view(['GET'])
def get_innovice_link(request):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/createInvoiceLink'
    num = request.query_params.get('num')
    print(num)
    costs = Payments_cost.objects.all().first()
    if(int(num)==2):
        title = '2 видеокарта'
        description = 'Зарабатывай в разы больше за тот же промежуток времени!'
        cost = costs.video2
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==3):
        title = '3 видеокарта'
        description = 'Зарабатывай в разы больше за тот же промежуток времени!'
        cost = costs.video3
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==4):
        title = '4 видеокарта'
        description = 'Зарабатывай в разы больше за тот же промежуток времени!'
        cost = costs.video4
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==6):
        title = '6 уровень'
        description = 'Увеличивай время пассивного дохода!'
        cost = costs.mining_duration6
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==7):
        title = '7 уровень'
        description = 'Увеличивай время пассивного дохода!'
        cost = costs.mining_duration7
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==8):
        title = '8 уровень'
        description = 'Увеличивай время пассивного дохода!'
        cost = costs.mining_duration8
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==9):
        title = '9 уровень'
        description = 'Увеличивай время пассивного дохода!'
        cost = costs.mining_duration9
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)
    if(int(num)==10):
        title = '10 уровень'
        description = 'Увеличивай время пассивного дохода!'
        cost = costs.mining_duration10
        print(cost)
        params = {
            'title':title,
            'description':description,
            'payload': '{}',
            'provider_token': '',
            'start_parameter': 'start_param',
            'currency': 'XTR',
            'prices': [{ 'amount': cost, 'label': title }]
        }
        response = requests.get(url,json=params)
        print(response.json())
        return Response(response.json(), status=status.HTTP_200_OK)

def get_user_profile_photo(bot_token, user_id):
    url = f'https://api.telegram.org/bot{bot_token}/getUserProfilePhotos'
    params = {'user_id': user_id}
    try:
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
    except requests.RequestException as e:
        pass
    return None

def clean_username(username):
    # Разрешенные символы: русские и английские буквы, цифры, знаки препинания и спецсимволы
    allowed_chars = re.compile(r'[а-яА-Яa-zA-Z0-9\s\.,!?@#$%^&*()_+=\-:;"\'<>|\\/\[\]{}~`]')
    
    # Отфильтровать строку, оставив только допустимые символы
    cleaned_username = ''.join(char for char in username if allowed_chars.match(char))
    
    # Если после очистки строка пуста, вернуть "Miner"
    if not cleaned_username:
        return "Miner"
    
    return cleaned_username


@api_view(['GET'])
def get_or_create_user(request):
    user_id = request.query_params.get('id')
    username = clean_username(request.query_params.get('first_name','Miner'))
    usertag = request.query_params.get('username','Miner')
    start = request.query_params.get('start','Miner')
    is_premium = request.query_params.get('is_premium','Miner')
    is_premium = is_premium=='true'

    try:
        user = TelegramUser.objects.get(user_id=user_id)
        user.username = username
        user.ispremium = is_premium
        user.save()
    except Exception as e:
        user = TelegramUser.objects.create(
            user_id=user_id,
            username=username,
            usertag=usertag
        )
        user.ispremium = is_premium
        user.save()
        if start:
            try:
                inviter = TelegramUser.objects.get(user_id=start)
                referal = Referal.objects.create(
                    inviter=inviter,
                    user=user
                )
                inviter.friends_invited += 1
                inviter.save()
                if inviter.friends_invited == 3:
                    inviter.balance += 12000

                if user.ispremium:
                    inviter.balance += 4000
                else:
                    inviter.balance += 1500
                inviter.save()
                task = Task.objects.get(typeT='invite')
                if task:
                    usertask, created = UserTask.objects.get_or_create(task=task, user=inviter)
                    usertask.friends_invited += 1
                    if usertask.friends_invited >= task.friends_toAdd and not usertask.complete:
                        usertask.complete = True
                        inviter.balance += task.reward
                    usertask.save()

                inviter.save()
                referal.save()
            except TelegramUser.DoesNotExist:
                pass
            except Exception as e:
                pass
    if user:
        date_difference = timezone.now().date() - user.daily_reward_date
        if date_difference > timedelta(days=1):
            user.daily_reward_day = 0
            user.daily_reward_claimed = False




        photo_url = get_user_profile_photo(BOT_TOKEN, user_id)
        if photo_url:
            user.photo_url = photo_url
            user.save()

        mined_while_of = 0
        if user.last_login:
            time_diff = min(user.mining_end - user.last_login, timezone.now() - user.last_login)
            if time_diff > timedelta(seconds=0):
                hours_diff = time_diff.total_seconds() / 3600
                mined_while_of = user.gph * hours_diff
                user.balance += mined_while_of
            time_diff = timezone.now()-user.last_login
            if time_diff > timedelta(seconds=0):
                user.energy += min(user.energy+time_diff.total_seconds()/3,user.max_energy)
        if user.refresh_energy_date < timezone.now().date():
            user.refresh_energy = 5
            user.refresh_energy_date = timezone.now().date()

        user.last_login = timezone.now()
        user.save()
    costs = Payments_costSerializer(Payments_cost.objects.all().first())
    user_serializer = TelegramUserSerializer(user)
    response_data = {
        "user": user_serializer.data,
        "mined_while_of": mined_while_of,
        "costs": costs.data
    }

    return Response(response_data, status=status.HTTP_200_OK)





@api_view(['POST'])
def uptime(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    upcost = [0,6500,45000,150000,500000]
    if(user.mining_time_lvl<5):
        if(user.balance>upcost[user.mining_time_lvl]):
            user.balance-=upcost[user.mining_time_lvl]
            user.mining_time_lvl+=1
            user.mining_duration+=timedelta(minutes=30)
            user.save()
            return Response({'balance':user.balance,'mining_time_lvl':user.mining_time_lvl}, status=status.HTTP_200_OK)
    elif(user.mining_time_lvl>=5):
        user.mining_time_lvl+=1
        user.mining_duration+=timedelta(minutes=30)
        user.save()
        return Response({'mining_time_lvl':user.mining_time_lvl}, status=status.HTTP_200_OK)

    return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)
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
def set_video(request):
    user_id = request.data.get('user_id')
    num = request.data.get('num')
    user = TelegramUser.objects.get(user_id = user_id)
    if(num==2):
        user.video2_lvl = 1
    elif(num==3):
        user.video3_lvl = 1
    elif(num==4):
        user.video4_lvl = 1
    user.save()
    return Response({'status':'ok'}, status=status.HTTP_200_OK)





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
            user.save()
            return Response({'balance':user.balance,'tap_lvl':user.tap_lvl,'gpc':user.gpc,'energy_lvl':user.enery_lvl,'max_energy':user.max_energy,'lvl':user.lvl}, status=status.HTTP_200_OK)
    else:
        cost = upcost[user.tap_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.gpc+=uptap[user.tap_lvl]
            user.tap_lvl+=1
            user.save()
            return Response({'balance':user.balance,'tap_lvl':user.tap_lvl,'gpc':user.gpc,'energy_lvl':user.enery_lvl,'max_energy':user.max_energy,'lvl':user.lvl}, status=status.HTTP_200_OK)
    return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

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
    upcost = [0,30000,115000,350000,1000000,2950000,8200000,23400000,58500000,175500000,350000000]
    upgph = [731,1638,3627,8307,18720,42120,94770,213408,480285,1080612,2250550]
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    num = request.data.get('num')-1
    print(num)
    if(num==1):
        cost = upcost[user.video_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.gph+=upgph[user.video_lvl]
            user.video_lvl+=1
            user.save()
            return Response({'balance':user.balance,'video_lvl':user.video_lvl,'gph':user.gph}, status=status.HTTP_200_OK)
    elif(num==2):
        cost = upcost[user.video2_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.gph+=upgph[user.video2_lvl]
            user.video2_lvl+=1
            user.save()
            return Response({'balance':user.balance,'video2_lvl':user.video2_lvl,'gph':user.gph}, status=status.HTTP_200_OK)
    elif(num==3):
        cost = upcost[user.video3_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.gph+=upgph[user.video3_lvl]
            user.video3_lvl+=1
            user.save()
            return Response({'balance':user.balance,'video3_lvl':user.video3_lvl,'gph':user.gph}, status=status.HTTP_200_OK)
    elif(num==4):
        cost = upcost[user.video4_lvl]
        if(user.balance>cost):
            user.balance-=cost
            user.gph+=upgph[user.video4_lvl]
            user.video4_lvl+=1
            user.save()
            return Response({'balance':user.balance,'video4_lvl':user.video4_lvl,'gph':user.gph}, status=status.HTTP_200_OK)

    return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def new_card(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    num = request.data.get('num')

    if(num==2):
        user.video2_lvl =1
    elif(num==3):
        user.video3_lvl =1
    elif(num==4):
        user.video4_lvl =1
    return Response({'status':'ok'}, status=status.HTTP_200_OK)

    return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def check_subscribe(request):
    bot_token = '7079394719:AAHWyslDgeCfWSYnrJ9VvCZDOP5jt9qAeJM'
    channel_id = '@ylionminer'
    user_id = request.query_params.get('user_id')
    print(user_id)
    url = f'https://api.telegram.org/bot{bot_token}/getChatMember'
    params = {
        'chat_id': channel_id,
        'user_id': user_id
    }
    response = requests.get(url, params=params)
    data = response.json()
    user = TelegramUser.objects.get(user_id=user_id)
    tasks = Task.objects.filter(typeT='subscribe')
    print(data)
    if tasks:
        for task in tasks:
            try:
                usertask = UserTask.objects.get(task=task, user=user)
            except UserTask.DoesNotExist:
                usertask = UserTask.objects.create(task=task, user=user)

            if not usertask.complete:
                params['chat_id'] = task.channel_id
                response = requests.get(url, params=params)
                bufftaskdata = response.json()
                if bufftaskdata.get('ok'):
                    state = bufftaskdata['result']['status']
                    if state in ['member', 'administrator', 'creator']:
                        usertask.complete = True
                        user.balance += task.reward
                    usertask.save()
                    user.save()

    taskdata = []
    if tasks:
        for task in tasks:
            taskdata.append({
                'task_id': task.id,
                'complete': UserTask.objects.get(task=task, user=user).complete
            })


    if data['ok']:
        state = data['result']['status']
        if state in ['member', 'administrator', 'creator']:
            if(user.subscribe_money_gived):
                print(321)
                user.subscribed=True
                user.save()
                return Response({'subscribed':user.subscribed,'balance':user.balance,'taskdata':taskdata}, status=status.HTTP_200_OK)
            else:
                print(123)
                user.subscribed=True
                user.balance+=5000
                user.subscribe_money_gived=True
                user.save()
                return Response({'subscribed':user.subscribed,'balance':user.balance,'taskdata':taskdata}, status=status.HTTP_200_OK)
        else:
            user.subscribed = False
            user.save()
            return Response({'subscribed':user.subscribed,'balance':user.balance,'taskdata':taskdata}, status=status.HTTP_200_OK)
    else:
        return Response({'subscribed':user.subscribed,'balance':user.balance,'taskdata':taskdata}, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_friends(request):
    user_id = request.query_params.get('user_id')
    try:
        user = TelegramUser.objects.get(user_id=user_id)
    except TelegramUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    referals = Referal.objects.filter(inviter=user)
    friends = [referal.user for referal in referals]
    
    # Sort friends by balance from highest to lowest
    friends.sort(key=lambda x: x.balance, reverse=True)

    
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
    top = TelegramUser.objects.order_by('-balance')[:100]
    
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

@api_view(['POST'])
def sitevisited(request):
    task_id = request.data.get('task_id')
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    task = Task.objects.get(id=task_id)
    try:
        usertask = UserTask.objects.get(user=user,task=task)
        if (not(usertask.complete)):
            usertask.complete = True
            user.balance+=task.reward
    except Exception as e:
        usertask = UserTask.objects.create(user=user,task=task)
        if (not(usertask.complete)):
            usertask.complete = True
            user.balance+=task.reward
    usertask.save()
    user.save()
    return Response({'balance':user.balance}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def gettasks(request):
    user_id = request.query_params.get('user_id')
    try:
        print(user_id)
        user = TelegramUser.objects.get(user_id=user_id)
    except TelegramUser.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    serialized_data = serializer.data
    
    for i in serialized_data:
        try:
            usertask = UserTask.objects.get(task_id=i['id'], user=user)
            complete = usertask.complete
        except UserTask.DoesNotExist:
            complete = False
        i['complete'] = complete
    print(serialized_data)
    return Response(serialized_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def turnsound(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    user.sound = not(user.sound)
    user.save()
    return Response({'status':'ok'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def turnvibrate(request):
    user_id = request.data.get('user_id')
    user = TelegramUser.objects.get(user_id=user_id)
    user.vibrate = not(user.vibrate)
    user.save()
    return Response({'status':'ok'}, status=status.HTTP_200_OK)