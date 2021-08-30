import os
import re
import signal
import json
import requests as req
import subprocess as sb

def sCall(cmd):
    return sb.run(cmd, shell=True, stdout=sb.DEVNULL, stderr=sb.DEVNULL)


def sReturn(cmd):
    return re.sub("[^!-~]+","",sb.Popen(cmd, stdout=sb.PIPE,shell=True).communicate()[0].decode("utf-8")).strip()


def sOpen(cmd):
    return sb.Popen(cmd, shell=True, stdout=sb.DEVNULL, stderr=sb.DEVNULL)


def sKill(pro):
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)