import requests
import os
from termcolor import colored

lista = open("admin.txt", 'r').readlines()
#Admin List name admin.txt in same path
os.system('clear')
#________________________________________________

name = """
	
░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██║████╗░██║░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
███████║██║░░██║██╔████╔██║██║██╔██╗██║█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝

    [!]𝒞ℴ𝒟ℯ𝒹 ℬ𝓎 ℳℴ𝓈𝓉𝒶𝒻𝒶 ℰ𝓁𝒢𝓊ℯ𝓇𝒹𝒶𝓌𝒾
    [*]𝔉𝔞𝔠𝔢𝔅𝔬𝔬𝔨 >>> 𝔥𝔱𝔱𝔭𝔰://𝔴𝔴𝔴.𝔣𝔞𝔠𝔢𝔟𝔬𝔬𝔨.𝔠𝔬𝔪/𝔪𝔬𝔰𝔱𝔞𝔣𝔞.𝔞𝔨𝔯𝔞𝔪.9237
    [*]ℑ𝔫𝔰𝔱𝔞𝔤𝔯𝔞𝔪 >>> 𝔥𝔱𝔱𝔭𝔰://𝔦𝔫𝔰𝔱𝔞𝔤𝔯𝔞𝔪.𝔠𝔬𝔪/𝔪𝔬𝔰𝔱𝔞𝔣𝔞_𝔢𝔩𝔤𝔲𝔢𝔯𝔡𝔞𝔴𝔦
"""
#ASCII Site 'https://fsymbols.com/text-art/'

print(colored(name, color='blue'))
#Create The Function...
def admin_finder(url):
    try:
        #To Catch Error...
        for admin in lista:
            admin_2 = admin.replace('\n', '')
            url_2 = "https://{}/{}".format(url, admin_2)
            req = requests.get(url_2).status_code
            if req == 200 or req == 302: #Cause Any Staus code are not working
                print(colored(f"𝓕𝓞𝓤𝓝𝓓!!! ===> {url}", color='green'))
                print(" ")
                break #To Stop Search
            else:
                print(colored(f"{url_2} ==> 𝓝𝓸𝓽 𝓦𝓸𝓻𝓴𝓲𝓷𝓰...", color='red')) #Still BruteForcing
                print(" ")

    except Exception as e:
        print(e) #To Print The Error

url = input(colored("＜＜ 𝓔𝓷𝓽𝓮𝓻 𝓤𝓡𝓛 𝓦𝓲𝓽𝓱𝓸𝓾𝓽 𝓱𝓽𝓽𝓹𝓼 ://\t＞＞ ", color='green'))
admin_finder(url)
