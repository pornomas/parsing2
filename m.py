import requests      
import json          
import time          
import os           
import pandas as pd

def getAreas():
    req = requests.get('https://api.hh.ru/areas')    
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    areas = []
    for k in jsObj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:                      
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'], 
                                  k['name'], 
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:                                                                
                areas.append([k['id'], 
                              k['name'], 
                              k['areas'][i]['id'], 
                              k['areas'][i]['name']])
    return areas

areas = getAreas()
def getEmployers():
    req = requests.get('https://api.hh.ru/employers')
    data = req.content.decode()
    req.close()
    count_of_employers = json.loads(data)['found']
    employers = []
    i = 0
    j = count_of_employers
    while i < j:
            req = requests.get('https://api.hh.ru/employers/'+str(i+1))
            data = req.content.decode()
            req.close()
            jsObj = json.loads(data)
            try:
                employers.append([jsObj['id'], jsObj['name']])
                i += 1
                print([jsObj['id'], jsObj['name']])
            except:
                i += 1
                j += 1
            if i%200 == 0:
                time.sleep(0.2)
    return employers
    
employers = getEmployers()
def getPage(page, area):
    params = {
        'employer_id': 3529,  
        'area': area,         
        'page': page,        
        'per_page': 100       
    }   
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode() 
    req.close()
    return data
for area in areas:
    for page in range(0, 20):
        jsObj = json.loads(getPage(page, area[2]))
        if not os.path.exists('./areas/'):
            os.makedirs('./areas/')
        nextFileName = './areas/{}.json'.format(str(area[2])+'_'+str(area[3])+'_'+str(page))
        f = open(nextFileName, mode='w', encoding='utf8')
        f.write(json.dumps(jsObj, ensure_ascii=False))
        f.close()
        if (jsObj['pages'] - page) <= 1:  
            print('[{0}/{1}] Область: {3} ({2}) - {5} ({4}) Вакансий: {6}'.format(area_list_id+1, 
                                                                         len(areas), 
                                                                         area[0], 
                                                                         area[1], 
                                                                         area[2], 
                                                                         area[3], 
                                                                         jsObj['found']))
            break
    time.sleep(0.2)
    dt = []
for fl in os.listdir('./areas/'):
    f = open('./areas/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()
    jsonObj = json.loads(jsonText)
    if jsonObj['found'] != 0:
        for js in jsonObj['items']:
            if js['salary'] != None:
                salary_from = js['salary']['from']
                salaty_to = js['salary']['to']
            else:
                salary_from = None
                salaty_to = None
            if js['address'] != None:
                address_raw = js['address']['raw']
            else:
                address_raw = None
            dt.append([
                js['id'],
                js['premium'],
                js['name'],
                js['department']['name'],
                js['has_test'],
                js['response_letter_required'],
                js['area']['id'],
                js['area']['name'],
                salary_from, 
                salaty_to,
                js['type']['name'],
                address_raw,
                js['response_url'],
                js['sort_point_distance'],
                js['published_at'],
                js['created_at'],
                js['archived'],
                js['apply_alternate_url'],
                js['insider_interview'],
                js['url'],
                js['alternate_url'],
                js['relations'],
                js['employer']['id'],
                js['employer']['name'],
                js['snippet']['requirement'],
                js['snippet']['responsibility'],
                js['contacts'],
                js['schedule']['name'],
                js['working_days'],
                js['working_time_intervals'],
                js['working_time_modes'],
                js['accept_temporary']
                ])
            dt = []
for fl in os.listdir('./areas/'):
    f = open('./areas/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()
    jsonObj = json.loads(jsonText)
    if jsonObj['found'] != 0:
        for js in jsonObj['items']:
            if js['salary'] != None:
                salary_from = js['salary']['from']
                salaty_to = js['salary']['to']
            else:
                salary_from = None
                salaty_to = None
            if js['address'] != None:
                address_raw = js['address']['raw']
            else:
                address_raw = None
            dt.append([
                js['id'],
                js['premium'],
                js['name'],
                js['department']['name'],
                js['has_test'],
                js['response_letter_required'],
                js['area']['id'],
                js['area']['name'],
                salary_from, 
                salaty_to,
                js['type']['name'],
                address_raw,
                js['response_url'],
                js['sort_point_distance'],
                js['published_at'],
                js['created_at'],
                js['archived'],
                js['apply_alternate_url'],
                js['insider_interview'],
                js['url'],
                js['alternate_url'],
                js['relations'],
                js['employer']['id'],
                js['employer']['name'],
                js['snippet']['requirement'],
                js['snippet']['responsibility'],
                js['contacts'],
                js['schedule']['name'],
                js['working_days'],
                js['working_time_intervals'],
                js['working_time_modes'],
                js['accept_temporary']
                ])