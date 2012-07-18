
class SMS:
    
    @staticmethod
    def from_dictionary(sms_dict):
        return SMS(
            sms_dict['to_number'],
            sms_dict['from_number'],
            sms_dict['body'],
        )
    
    def __init__(self, to_number, from_number, body):
        self.to_number = to_number
        self.from_number = from_number
        self.body = body
        
        
    def short_body(self, max_length=15):
        if len(self.body) > max_length - 3:
            return self.body[:max_length-3] + '...'
        else:
            return self.body
            
    def __repr__(self):
        return "<SMS to:%s|from:%s|body:%s>" % (self.to_number, self.from_number, repr(self.short_body()))
        
    def __str__(self):
        
        length = 0

        body_length = len(self.body)
        
        body = self.body
        
        if body_length == 0:
            body = "\n"
        else:
            if body[body_length - 1] != '\n':
                body += '\n'
                body_length += 1
            
            pos = 0
            while pos < body_length:
        
                c = body[pos]
                if c == '\r':
                    length += 1
                    if pos + 1 < body_length and body[pos + 1] == '\n':
                        pos += 1
                
                elif c == '\n':
                    length += 1
            
                pos += 1
                
        out = ""
        out += "TEXT\n"
        
        
        out += "LENGTH:%d\n" % length
        out += "TO:%s\n" % self.to_number
        out += "FROM:%s\n" % self.from_number
        out += "\n%s" % body #not self.body beacause we transform it
        
        return out