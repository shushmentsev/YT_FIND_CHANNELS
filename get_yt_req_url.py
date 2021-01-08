# -*- coding: utf-8 -*-

def get_yt_req_url(ans):

    # ans = input("Искать материал по следующим словам (слова разделяются пробелом): ")
    ans_list = ans.split()
    print("ans_list: ", ans_list)
    ans = "+".join(ans_list)
    print("ans: ", ans)
    yt_url = "https://www.youtube.com/results?search_query="
    yt_url = yt_url + ans
    # yt_url = yt_url + "&sp=EgIoAQ%253D%253D"
    print("yt_url: ", yt_url)

    return yt_url

if __name__ == "__main__":

    get_yt_req_url()
