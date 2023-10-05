from parsedata import ParseData

data = {
    "score" : 750,
    "tm_screen_res" : "1920x1080",
    "email_addr" : "dang.vue0@gmail.com",
    "ip_address" : "192.168.0.1"
    }

p = ParseData(data)
p1 = p.parse_screen_res()
p2 = p.parse_email()
p3 = p.parse_ip()
print(p1, type(p1), p2, type(p2), p3, type(p3))

pAll = ParseData(data).parse()
print(pAll)