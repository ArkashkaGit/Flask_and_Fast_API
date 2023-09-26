import threading
from requests import get
import time

url_img_1 = 'https://static.tildacdn.com/tild6231-3732-4362-b664-613462366564/_.png'
url_img_2 = 'https://cdn-edge.kwork.ru/pics/t3/15/305552-2.jpg'
url_img_3 = 'https://04.img.avito.st/image/1/hROi1ba_KfrUcNv8pP-UHyh2L_Acti0IEHYr_BpwK_oWMA'

def threading_download(save_images):
    def wrapper(*args):
        count = 1
        threads = []
        for img in [*args]:
            thread = threading.Thread(target=save_images, args=(img, count))
            threads.append(thread)
            thread.start()
            count += 1
        for thread in threads:
            thread.join()
        
        return
    return wrapper


@threading_download 
def save_images(image, count=1):
    start_time = time.time()
    load = get(image)
    with open(f"threading/loading_img/img_{count}.jpg", "wb") as save_img:
        save_img.write(load.content)
        print(f'время скачивани изображения под номером {count} = {time.time() - start_time:.4f}')

if __name__ == '__main__':
    start_time = time.time()
    save_images(url_img_1, url_img_2, url_img_3)
    print(f'Общее время исполнения программы = {time.time() - start_time:.4f}')
    