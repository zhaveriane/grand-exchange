#!/usr/bin/python
import requests
import json
import sys

def pollItemInformation():
    # OFFICIAL_ITEM_API_URL = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="
    OSBUDDY_ITEM_SUMMARY_API_URL = "https://rsbuddy.com/exchange/summary.json"

    # official_item = requests.get(OFFICIAL_ITEM_API_URL + itemId)
    # print(official_item.json()["item"]["current"]["price"])

    osbuddy_item = requests.get(OSBUDDY_ITEM_SUMMARY_API_URL)
    osbuddy_item_json = osbuddy_item.json()
    for itemId in osbuddy_item_json.keys():
        print(osbuddy_item_json[itemId]["buy_average"])
        print(osbuddy_item_json[itemId]["sell_average"])
        print(osbuddy_item_json[itemId]["buy_quantity"])
        print(osbuddy_item_json[itemId]["sell_quantity"])

def trackItems():
    pollItemInformation()

def main():
    # print command line arguments
    if len(sys.argv) is 1:
        trackItems()

if __name__ == "__main__":
    main()