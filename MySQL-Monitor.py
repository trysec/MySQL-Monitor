#!/usr/bin/env python
# -*- coding : utf-8 -*-


def file_monitor():
    j = 0  # 指针位置
    while True:
        f = open(r'G://phpstudy/PHPTutorial/MySQL/data/sql.log')
        if j != 0:
            f.seek(j, 0)
        while True:
            line = f.readline()
            if line.strip():
                print("[+]当前执行的sql语句为>_<  -> " + line.strip())
            j = j + len(line)
            if not line.strip():
                break
        f.close()


def desc():
    logo = r'''
             _     ___  _ ____  ____  _           _      ____  _      _ _____ ____  ____
            / \__/|\  \/// ___\/  _ \/ \         / \__/|/  _ \/ \  /|/ Y__ __Y  _ \/  __\
            | |\/|| \  / |    \| / \|| |   _____ | |\/||| / \|| |\ ||| | / \ | / \||  \/|
            | |  || / /  \___ || \_\|| |_/\\____\| |  ||| \_/|| | \||| | | | | \_/||    /
            \_/  \|/_/   \____/\____\\____/      \_/  \|\____/\_/  \|\_/ \_/ \____/\_/\_\
                                           V 1.0
                                           design by wing
                                           evilwing.me
    '''
    print(logo)
    print("[*]MySQL日志监控中>_<")


if __name__ == "__main__":
    desc()
    file_monitor()
