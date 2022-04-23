import urllib.parse
import urllib.request as urllib2
data = urllib.parse.urlencode({'inputstring': 'Phoenix, AZ'}).encode("utf-8")
info = urllib.request.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()
print(content)
