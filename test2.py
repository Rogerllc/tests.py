import urllib.request
rll = "https://www.youtube.com/watch?v=SvbMu8mIDLA"
conn=urllib.request.urlopen(rll)
html = conn.read().decode('utf-8')
print("status:", conn.status)
print(html[:1000])