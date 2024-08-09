
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

