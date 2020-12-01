import requests
import json
states_convert = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'District of Columbia': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
with open('datacovid.json') as json_file:
    covid_json = json.loads(json_file.read())

with open('dataempoly.json') as json_file:
    empoly_json = json.loads(json_file.read())




employ = {}
for i in empoly_json:
    splt = i.split(',')
    county = splt[0]
    if(county == 'District of Columbia'):
        state_name = 'District of Columbia'
    else:
        state = splt[1].strip()
        print(state)
        state_name = states_convert[state]

    splt = county.split(' ')
    splt.pop()
    county_name = ''
    for s in splt:
        county_name += s + ' '
    county_name = county_name[:-1]
    full_name = county_name + ',' + state_name
    employ[full_name] = empoly_json[i]

res = {}
num = 0
for county_c in covid_json:
    for county_e in employ:
        if(county_c == county_e):
            data_c = covid_json[county_c]
            data_e = employ[county_e]
            data_all = {}
            for i in data_e:
                month_e = i[0]
                e_rate = i[1]
                for j in data_c:
                    month_c = j[0]
                    c_rate = j[1]
                    if(month_e == month_c):
                        data_all[month_c] = {'Month': month_c,'UnemploymentRate': e_rate, 'CovidCaseIncrease':c_rate}
                        res[num] = {'district': county_c, 'monthly_data': data_all}
            num +=1;





with open('result.json', 'w') as outfile:
    json.dump(res, outfile)

with open('result.json') as json_file:
    result =json.loads(json_file.read())

#result = json.dumps(result)
#response = requests.patch('https://covid19groupproject.firebaseio.com/.json', result)











