#__*__coding:utf-8__*__
import configparser

class ReadConfig:

    
    def __init__(self):
        '''
        open and prepare to read
        '''
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')  #read config file

    def get_key(self,name):
        key = self.config.get('SECRET KEY',name)
        return key

    def get_host(self,name):
        host = self.config.get('SERVER',name)
        return host

    def get_latitude(self,name):
        latitude = self.config.get('LOCATION',name)
        return latitude

    def get_longtitude(self,name):
        longtitude = self.config.get('LOCATION',name)
        return longtitude

    def get_location(self,*args):
        latitude = self.config.get('LOCATION',args[0])
        longtitude = self.config.get('LOCATION',args[1])
        locationdict = {'latitude':latitude,'longtitude':longtitude}
        return locationdict
