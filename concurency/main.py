# import time

# # ---------multi-threading---------
# import threading
# from concurrent.futures import ThreadPoolExecutor
# #----------------------------------
# import requests


# # ---------multi-threading----------
# thread_local = threading.local()



# def main():
#     sites = [
#         "https://realpython.com/python-concurrency/","https://www.jython.org",
#     ] *80
#     start_time = time.perf_counter()
#     download_all_sites(sites)
#     duration = time.perf_counter() - start_time
#     print(f"Downloaded in {len(sites)} sites in {duration} seconds ")

# # -----multi-threading---------


# # def download_all_sites(sites):
# #     with requests.Session() as session:
# #         for url in sites:
# #             download_site(url,session)

# def download_all_sites(sites):
#     with ThreadPoolExecutor(max_workers=52) as executor:
#         executor.map(download_site,sites)

# # -----------------------------




# def download_site(url):
#     session = get_session_for_thread()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} bytes from {url}")


# # -----multi-threading---------
# def get_session_for_thread():
#     if not hasattr(thread_local,'session'):
#         thread_local.session = requests.Session()
#     return thread_local.session

# # -----------------------------



# if __name__ == "__main__":
#     main()


# ---------------------asyncio------------------------------------

import asyncio
import time
import aiohttp



async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(url,session) for url in sites]
        await asyncio.gather(*tasks,return_exceptions=True)


async def downlaod_site(url,session):
    async with session.get(url) as response:
        print(f"Read {len(await response.read())} bytes from {url}")


async def main():
    sites = ["https://realpython.com/python-concurrency/","https://www.jython.org"]*80000000

    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time

    print(f" -----------duration --- {duration}")



if __name__=="__main__":
    asyncio.run(main())