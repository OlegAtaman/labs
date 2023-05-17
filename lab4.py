import requests
import json

class Singleton(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance
    

class WebSurfer:
    def __init__(self):
        self.pagestack = ['https://olegataman.github.io/Course_Work/main.html']
        self.base = 'https://olegataman.github.io/Course_Work/'
        self.exceptions = ['styles/style.css', '#']
        self.postaple = ['https://olegataman.github.io/Course_Work/login.html',
                         'https://olegataman.github.io/Course_Work/registration.html',
                         'https://olegataman.github.io/Course_Work/newadd.html']

    def runserfer(self):
        while True:
            r = requests.get(self.pagestack[len(self.pagestack)-1])
            print(r.text)
            if self.pagestack[len(self.pagestack)-1] in self.postaple:
                print('There is POST form!')
                ans = input('Input dict data or 0 to continue surfing: ')
                if ans != '0':
                    post_r = requests.post(self.pagestack[len(self.pagestack)-1], data=json.loads(ans))
                    print(post_r)
                    input('Resp 405 is success! Enter to continue...')
            print('----------------------------------------')
            print('Available links:')
            if len(self.pagestack) > 1:
                print('0. <- back')
            i = 1
            for href in self._get_links(r):
                print(f'{i}. {href}')
                i += 1
            ans = input("What's next? q - exit: ")
            if ans == 'q':
                break
            if ans == '0':
                self.pagestack.pop(len(self.pagestack)-1)
                continue
            self.pagestack.append(self.base + self._get_links(r)[int(ans)-1])
    
    def _get_links(self, resp):
        splited = resp.text.split('href="')
        hrefs = []
        for text in splited:
            href = text.split('"')[0]
            if href not in self.exceptions:
                hrefs.append(href)
        hrefs.pop(0)
        return hrefs
    

class SingletonSurfer(Singleton, WebSurfer):
    pass


surfer = SingletonSurfer()
surfer.runserfer()
