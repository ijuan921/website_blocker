import time
import ast
import os
import platform
from datetime import datetime as dt

def open_data(index):
    with open("data.txt") as f:
        data = f.readlines()
    return data[index]

def initial_hour():
    initial = open_data(0)
    return int(initial.strip('\n'))

def last_hour():
    last = open_data(1)
    return int(last.strip('\n'))

def websites_list():
    lst = open_data(2)
    return ast.literal_eval(lst)

def os_path():
    if platform.system() == 'Linux' or platform.system() == 'Mac':
        return os.path.join(os.path.sep, "etc", "hosts")
    return os.path.join("C:", os.path.sep, "WINDOWS", "system32", "drivers", "etc", "hosts")

def main(path, redirect, websites, start, end):
    while True:
        #try:
        if dt(dt.now().year, dt.now().month, dt.now().day,start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end):
            with open(path, 'r+') as  file:
                content=file.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
        else:
            with open(path, "r+") as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
        time.sleep(5)
        #except:
        #    break

if __name__ == "__main__":
    hosts_temp = "hosts"
    hosts_path = os_path()
    redirect = "127.0.0.1"
    initial_hour = initial_hour()
    last_hour = last_hour()
    websites_list = websites_list()

    main(hosts_path, redirect, websites_list, initial_hour, last_hour)