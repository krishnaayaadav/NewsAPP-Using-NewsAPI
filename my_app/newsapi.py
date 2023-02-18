
import requests,pickle,os


class NewAppAPI:
    """This is class that will make request to api endpoints and
        it will also store the api response in some file so that we don't need make request to that api for same kind response.
        Note: I know that we may not store the api response. But
        I am doing this thing just to reduce repetion of same steps like for every time we make request to another server I think it's better to save same kind response
        """

    def __init__(self, url:str, apikey:str, file_name:str, mode:str):
        # initializing defualt things
        self.endpoints  = url
        self.apikey     = apikey
        self.file_name  = file_name
        self.file_mode  = mode

        # it will automatically called when object is created
        self.__fetch_data_from_api() # fetching data from api and saving into file
        self.__store_data_in_file()  # storing data in files
    # private methods here
    def __fetch_data_from_api(self):
        """Fetching data from different apis endpoints"""

        URL = f'{self.endpoints}{self.apikey}'
        try:
            req = requests.get(url=URL)
        except:
            print('\n Some Execption Occurs While make request to api endpoints \n')
            result = {'Exception': 'Some Execption Occurs While make request to api endpoints'}
        else:
            result = req.json()

        return result

    # private methods here
    def __store_data_in_file(self):
        """Storing responsed data in file some file.
           So that We dont make everytime request to some server.
        """
            
        with open(self.file_name, mode=self.file_mode) as news:
            data = self.__fetch_data_from_api()
            
            try:
                pickle.dump(data, news) # pickling here
            except: 
                print('\n Some Execption Occurs While make request to api endpoints \n')
                result = {'Exception': 'Some Execption Occurs While make request to api endpoints'}
            else:
                result = {'Succefuly': 'Data successfuly stored it done'}
                print('\n Data successfuly stored it done\n')
            
            finally:
                return result

    def get_all_data(self):
        """Get data from stored file of request api.
           It Will return all data from entered file."""
        exist = os.path.isfile(self.file_name)
        if exist: 

            with open(self.file_name, mode='rb') as new_file:
                
                try:
                    news_data = pickle.load(new_file)
                except: 
                    print(f'\n Exception Occurs during fetching data from enterd file {Exception.__class__} \n')
                
                return news_data
        else:
            print("Sooorry Enter Invalid file name! ")
    
    def get_top_headlines(self):
        headlines = []
        all_data = self.get_all_data()

        for art in all_data['articles']:
            headlines.append(art)
        return headlines
    
# URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=69e84eb4d05d4b6d802a74469b2cd6d1'
# apikey = '<your_api_key_here>'
# URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey='

# n1 = NewAppAPI(url=URL, apikey=apikey, mode='ab', file_name='news.dat')



# for art in news_data['articles']:
#     print(type(art), art.keys())
#     print( art['author'], art['urlToImage'])

