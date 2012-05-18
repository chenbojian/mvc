from model.Outlaw import Outlaw

class OutlawController(object):

    def __init__(self):
        pass
    
    def save(self, model):
        if model != None:
            model.save()
            
    def all(self):
        return Outlaw.get_all()