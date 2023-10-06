import re

class ParseData:

    def parse_screen_res(self, data):
        self.data = data
        if (isinstance(self.data["tm_screen_res"],(int, float))):
            return self.data["tm_screen_res"]
        else:
            match = re.findall('\d+$', self.data["tm_screen_res"])
            return int(match[0])
    
    def parse_email(self, data):
        self.data = data
        match = re.findall('(?<=@)[\w+]+', self.data["email_addr"])
        # insert email labelencoder here

        # check value is int, float

        return match[0]
        
    def parse_ip(self, data):
        self.data = data
        if (isinstance(self.data["ip_address"],(int, float))):
            return self.data["ip_address"]
        else:
            match = re.findall('^\d+', self.data["ip_address"])
            return int(match[0])
    
    def parse(self, data):
        self.data = data
        self.data["tm_screen_res"] = self.parse_screen_res(self.data)
        self.data["email_addr"] = self.parse_email(self.data)
        self.data["ip_address"] = self.parse_ip(self.data)
        return self.data
