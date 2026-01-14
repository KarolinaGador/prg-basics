class ebok:
    def __init__(self, title, author, pages, page, status):
        self.title = title
        self.author = author
        self.pages = pages
        self.page =page
        self.status =status

    def open(self):
        self.status = "open"
    def close(self):
        self.status = "closed"
    def stat(self):
        print(f'{self.title} {self.author} {self.pages}, current page on {self.page}')    

    def read(self):
       if self.status=="open": 
        if self.page<self.pages:
          self.page = self.page +1
        else:
           self.page = self.page
       else:
          print(f'The book is closed')      