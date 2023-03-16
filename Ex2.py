import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str, overwrite=True):
        """Метод загружает файл на яндекс диск"""
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': path_to_file, 'overwrite': overwrite}
        response = requests.get(URL, headers=headers, params=params)

        if 'error' in response.json():
            print(response.json()['message'])
        else:
            href = response.json()['href']
            resp = requests.put(href, data=open(path_to_file, 'rb'))
            if resp.status_code == 201:
                print(f'Файл {path_to_file} успешно загружен')
            else:
                print('Ошибка при загрузке файла')


if __name__ == '__main__':
    path_to_file = 'test.jpg'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
    # uploader.upload(path_to_file, overwrite=False)


