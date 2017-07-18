## Demo from BOT
import requests
url = "https://iapi.bot.or.th/Stat/Stat-ReferenceRate/DAILY_REF_RATE_V1/"
querystring = {"start_period":"2011-01-12","end_period":"2011-01-15"}
headers = {
    'api-key': "U9G1L457H6DCugT7VmBaEacbHV9RX0PySO05cYaGsm"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
