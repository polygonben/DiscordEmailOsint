#!/bin/python
import requests
import sys
import json
import argparse 
import time


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--email", type=str, help="Email address to check ")
group.add_argument("--file", type=str, help="Text file containing a list of email addresses to check")
args = parser.parse_args()


url = "https://discord.com/api/v9/auth/register"

def check(email):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-Super-Properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5NjA5OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        'X-Fingerprint': '1104751028177473637.GI_tRdrngvBBq3rg6kCf37rbXnk',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'Alt-Used': 'discord.com',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers',
        'Cookie' :'__dcfduid=239cc820ecd511edb63ce16188c243bd; __sdcfduid=239cc821ecd511edb63ce16188c243bd28b34ab5ec4b64c7aa4cda6f1a824522275704faf45629c491f727735f468432; __cfruid=15f6585a652967bcb810175805267c694e97dc06-1683463568; __cf_bm=wNub.ICh9wK27ND1_idm6M8KSsajwJ.axobA0rWjeis-1683463570-0-AWU7btfMLPpLeJECj9G/jyti96r18mwc7+mDGn3sqH/h+VarQS3axX8MbhEeW9JKYt2w0Pffiu0SdWBVHzaPM/r4kebLh6ewIrDkXarcOYdw'
    }

    data = {
        "fingerprint":"1104751028177473637.GI_tRdrngvBBq3rg6kCf37rbXnk",
        "email":email,
        "username":"ARaonEentUername1942gdt",
        "password":"S3up4rs4cReT!Passowrd",
        "invite":"null",
        "consent":"true",
        "date_of_birth":"1994-04-03",
        "gift_code_sku_id":"null",
        "captcha_key":"null",
        "promotional_email_opt_in":"false"
        }

    response = requests.post(url, headers=headers, json=data)

    if "code" in response.json().keys():
        if response.json()["code"] == 50035:
            if response.json()["errors"]["email"]["_errors"][0]["code"] == "EMAIL_INVALID":
                print(email, "Invalid email")
            elif response.json()["errors"]["email"]["_errors"][0]["code"] == "EMAIL_ALREADY_REGISTERED":
                print(email,"Registered")
    else:
        print(email, "Not Registered")


if args.email:
    check(args.email)
else:
    with open(args.file) as emailFile:
        for line in emailFile:
            check(line.strip())
