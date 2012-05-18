from model.Outlaw import Outlaw

class OutlawController(object):

    def __init__(self):
        pass
    
    def save(self, model):
        if model != None:            
            if model.name == '' or model.surname == '':
                return False
            
            model.save()
            return True
            
    def get_all(self):
        return Outlaw.get_all()