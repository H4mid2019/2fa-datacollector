import pyotp
import time
import sys
secret = ""
file_name = ""
totp = pyotp.TOTP(secret)

alist = []
alist1 = []

place = []
place1 = []
place2 = []
place3 = []
place4 = []
place5 = []
digit_counter = 0


def first():
    global secret
    global file_name
    try:
        if len(sys.argv) == 1:
            print("PLEASE INSERET THE SECRET KEY")
            reciver(60)
        elif sys.argv[1].lower() == "m":
            argm = int(sys.argv[2])
            secret = sys.argv[3]
            file_name = sys.argv[4]
            reciver(argm*60)
        elif sys.argv[1].lower() == "h":
            argh = int(sys.argv[2])
            secret = sys.argv[3]
            file_name = sys.argv[4]
            reciver(argh*3600)
        else:
            arg = int(sys.argv[1])
            secret = sys.argv[2]
            file_name = sys.argv[3]
            reciver(arg)

    except ValueError:
        print("please enter valid argument")


def time_counter(seconds):
    starttime = time.time()
    while True:
        now = time.time()
        if now > starttime + seconds:
            for i in range(8):
                if i == 0:
                    last(alist)
                elif i == 1:
                    last(alist1, name="All DigitS")
                elif i == 2:
                    last(place, name="Digit")
                elif i == 3:
                    last(place1, name="Digit")
                elif i == 4:
                    last(place2, name="Digit")
                elif i == 5:
                    last(place3, name="Digit")
                elif i == 6:
                    last(place4, name="Digit")
                else:
                    last(place5, name="Digit")
            break
        yield now - starttime


def reciver(w, s=30):
    for t in time_counter(w):
        a = totp.now()
        time.sleep(s)
        counter(a)


def last(compare_list, name="total"):
    global digit_counter
    global file_name
    c = 0
    char_frerq = {}
    for char in compare_list:
        if char in char_frerq:
            char_frerq[char] += 1
        else:
            char_frerq[char] = 1
    char_frerq_sort = sorted(
        char_frerq.items(), key=lambda kv: kv[1], reverse=True)
    dash = (f"-"*90)
    for key, value in char_frerq_sort:
        if c == 0 and name == "total":
            c += 1
            count = len(compare_list)
            result = f"{name}\nInputs:\t{count}\n{dash}\ncount:{value}\t number:{key}\n"
        elif name == "All DigitS" and c == 0:
            result = f"{name}\n{dash}\ncount:{value}\t number:{key}\n"
            c += 1
        elif name == "All DigitS" and c != 0:
            result = f"count:{value}\t number:{key}\n"
            c += 1
        elif digit_counter == 0 and c == 0 and name == "Digit":
            result = f"{name}\t{digit_counter+1}\n{dash}\ncount:{value}\t number:{key}\n"
            digit_counter += 1
            c += 1
        elif c == 0 and name == "Digit":
            result = f"{name}\t{digit_counter+1}\n{dash}\ncount:{value}\t number:{key}\n"
            digit_counter += 1
            c += 1
        else:
            result = f"count:{value}\t number:{key}\n"
            c += 1
        print(result)
        file = open(file_name, "a")
        file.write(result)
        file.close()


def counter(x):
    alist.append(x)
    alist1.append(x[0])
    alist1.append(x[1])
    alist1.append(x[2])
    alist1.append(x[3])
    alist1.append(x[4])
    alist1.append(x[5])
    place.append(x[0])
    place1.append(x[1])
    place2.append(x[2])
    place3.append(x[3])
    place4.append(x[4])
    place5.append(x[5])


banner = """
************************   2FA Data Collector   ***************************


        Recording started.....
"""


if __name__ == "__main__":
    print(banner)
    first()
