#Alternative Test
#use pycurl

import pycurl
URL = prod_host + request_path + query_string
cookie = '; '.join("=".join(_) for _ in rfk_cookie.items())
output = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, URL)
c.setopt(c.FOLLOWLOCATION, True)
c.setopt(c.COOKIE, cookie)
#c.setopt(c.HTTPHEADER, ["Content-Type: application/json;charset=UTF-8", "Accept: application/json, text/plain, */*" ])
c.setopt(c.WRITEFUNCTION, output.write)
c.perform()
c.close()
print(output)
print(dir(output))
curl_res = output.getvalue()
print(curl_res)
