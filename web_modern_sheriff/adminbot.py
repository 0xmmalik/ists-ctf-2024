import os
from requests import post
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import signal
import sys
from time import sleep

class AdminBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def visit_url(self, url):
        self.driver.get("http://challenges.ists.io:8000/")
        self.driver.add_cookie({"name": "flag", "value": "ISTS{y0u_m3an_youd_trad3_me_4_a_h0r53}", "path": "/"})
        self.driver.get(url)

        print(f"[ ] Admin bot visited: {url}")

    def close(self):
        self.driver.quit()

def timeout(signum, frame):
    print("[ ] Time limit exceeded")
    do_stuff()

#url = "http://challenges.ists.io:8000/"
#fetch_from = f"{url}reports/fetch.php"
#clear = f"{url}reports/clear.php"
#delete = f"{url}reports/delete.php?report="
#key = {"key": "ists_ruLez!!"}
#admin_bot = AdminBot()
#signal.signal(signal.SIGALRM, timeout)

# post(clear, data=key)
print("[+] Ready.")
done = []
global curr, times
curr = ""
times = 0
def do_stuff():
    global curr, times
    url = "http://challenges.ists.io:8000/"
    fetch_from = f"{url}reports/fetch.php"
    clear = f"{url}reports/clear.php"
    delete = f"{url}reports/delete.php?report="
    key = {"key": "ists_ruLez!!"}
    admin_bot = AdminBot()
    signal.signal(signal.SIGALRM, timeout)
    while True:
        try:
            info = post(fetch_from, data=key)
            for report in info.text.split(","):
                if len(report) != 25: continue
                if report in done: continue
                if report == curr: times += 1
                else: times = 0
                curr = report
                if times >= 5:
                    print(f"[ ] Deleting {report}.")
                    post(f"{delete}{report}", data=key)
                print(f"\n[+] Visiting {report}.")
                url2 = f"{url}reports/{report}.html"
                signal.alarm(6)
                admin_bot.visit_url(url2)
                print(f"[ ] Deleting {report}.")
                post(f"{delete}{report}", data=key)
                done.append(report)
                signal.alarm(0)
            sleep(1)
        except KeyboardInterrupt:
            nxt = input("\n[+] Paused. [C]ontinue, c[L]ear and continue, [E]nd\n[ ] > ").lower()
            if nxt == "l":
                post(clear, data=key)
                print("[ ] Cleared.")
            elif nxt == "e": break
            print("[ ] Continuing.")
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            print("[ ] Error: Alert still open, skipping.")
        except Exception as e:
            admin_bot = AdminBot()
            print(f"[ ] Error: {str(e)}, skipping.")
do_stuff()
print("\n[+] Ended.")
admin_bot.close()
