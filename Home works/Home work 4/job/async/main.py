import asyncio
from requests import get
import time

url_img_1 = 'https://static.tildacdn.com/tild6231-3732-4362-b664-613462366564/_.png'
url_img_2 = 'https://cdn-edge.kwork.ru/pics/t3/15/305552-2.jpg'
url_img_3 = 'https://04.img.avito.st/image/1/hROi1ba_KfrUcNv8pP-UHyh2L_Acti0IEHYr_BpwK_oWMA'
images = [url_img_1, url_img_2, url_img_3]


async def save_images(image, count=1):
    start_time = time.time()
    load = get(image)
    with open(f"async/loading_img/img_{count}.jpg", "wb") as save_img:
        save_img.write(load.content)
        print(
            f'время скачивани изображения под номером {count} = {time.time() - start_time:.4f}'
        )
    count += 1


async def main():
    tasks = []
    count = 1
    for url in images:
        asyn = asyncio.ensure_future(save_images(url, count))
        tasks.append(asyn)
        count += 1
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time_1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(
        f'Общее время исполнения программы = {time.time() - start_time_1:.4f}')
