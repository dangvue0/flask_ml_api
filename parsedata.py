import re

class ParseData:
    
    def __init__(self, data):
        self.data = data

    def parse_screen_res(self):
        if (isinstance(self.data["tm_screen_res"],(int, float))):
            return self.data["tm_screen_res"]
        else:
            match = re.findall('\d+$', self.data["tm_screen_res"])
            return int(match[0])
    
    def parse_email(self):
        match = re.findall('(?<=@)[\w+]+', self.data["email_addr"])
        # insert email labelencoder here

        # check value is int, float

        return match[0]
        
    def parse_ip(self):
        if (isinstance(self.data["ip_address"],(int, float))):
            return self.data["ip_address"]
        else:
            match = re.findall('^\d+', self.data["ip_address"])
            return int(match[0])
    
    def parse(self):
        self.data["tm_screen_res"] = ParseData.parse_screen_res(self)
        self.data["email_addr"] = ParseData.parse_email(self)
        self.data["ip_address"] = ParseData.parse_ip(self)
        return self.data