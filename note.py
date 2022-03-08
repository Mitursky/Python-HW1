import datetime

class Note:
    def __init__(self, memo='', tags='', id=1):
        self.memo = memo
        self.id = id
        self.tags = tags
        self.date = datetime.date.today()
    
    def modify(self, memo, tags):
        if memo:
            self.memo = memo
        if tags:
            self.tags = tags




    

