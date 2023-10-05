import re

class ParseData:
    
    def __init__(self, data):
        self.data = data
        # print(self.data)
        

    def parse_screen_res(self):
        match = re.findall('\d+$', self.data["screen_res"])
        return int(match[0])
    
    def parse_email(self):
        match = re.findall('(?<=@)[\w+]+', self.data["email"])
        return match[0]
        
    def parse_ip(self):
        match = re.findall('^\d+', self.data["ip"])
        return int(match[0])
    
    def parse(self):
        self.data["screen_res"] = ParseData.parse_screen_res(self)
        self.data["email"] = ParseData.parse_email(self)
        self.data["ip"] = ParseData.parse_ip(self)
        return self.data

data = {
    "score" : 750,
    "screen_res" : "1920x1080",
    "email" : "dang.vue0@gmail.com",
    "ip" : "192.168.0.1"
    }

p = ParseData(data)
p1 = p.parse_screen_res()
p2 = p.parse_email()
p3 = p.parse_ip()
print(p1, type(p1), p2, type(p2), p3, type(p3))

pAll = ParseData(data).parse()
print(pAll)