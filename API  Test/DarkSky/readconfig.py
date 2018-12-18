#__*__coding:utf-8__*__
import configparser

class ReadConfig:

    
    def __init__(self):
        '''
        open and prepare to read
        '''
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')  #read config file

    def get_key(self):
        key = self.config.get('SECRET KEY','Key')
        return key

    def get_host(self):
        host = self.config.get('SERVER','Host')
        return host

    def get_latitude(self):
        latitude = self.config.get('LOCATION','Latitude')
        return latitude

    def get_longtitude(self):
        longtitude = self.config.get('LOCATION','Longtitude')
        return longtitude

    def get_location(self):
        latitude = self.config.get('LOCATION','Latitude')
        longtitude = self.config.get('LOCATION','Longtitude')
        locationdict = {'latitude':float(latitude),'longtitude':float(longtitude)}
        return locationdict
