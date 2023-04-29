import requests
import re
import json

def req(input):
  x = requests.get(f'https://kbbi.kemdikbud.go.id/entri/{input}')
  regex_kata = '<h2 style="margin-bottom:3px">(.*?) <\/h2>'
  regex_type = '<span title="(.*?)">'
  regex_desc = '<\/i><\/font>(.*?);|<\/i><\/font>(.*?)<\/li>'
  kata = re.compile(regex_kata)
  type_kata = re.compile(regex_type)
  desc_kata = re.compile(regex_desc)

  try:
    kata_datas = re.findall(kata,x.text)[0]
    type_datas = re.findall(type_kata,x.text)
    del type_datas[-1]
    result = {
      "error": False,
      "kata": re.sub('<sup>[0-9]<\/sup>', '', kata_datas), 
      "type": type_datas, 
      "desc": re.search(desc_kata, x.text).group(0).replace('</i></font>', '').replace('</li>', '').replace(";", "")
    }
    return json.dumps(result, indent=2)
  except:
    result = {
      "error": True, 
      "kata": input,
      "reason": "Entri tidak ditemukan"
    }
    return json.dumps(result, indent=2)


print(req("yg"))

# Output
# {
#   "error": false,
#   "kata": "yg",
#   "type": [
#     "Nomina: kata benda",
#     "singkatan"
#   ],
#   "desc": "yang"
# }


