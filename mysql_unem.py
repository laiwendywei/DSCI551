import mysql.connector
import datetime
import json

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='project')
cursor=cnx.cursor()
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

query =("select * from unemployment where Period Like \"%20%\" ")
cursor.execute(query)
table_results =cursor.fetchall()


mysql_dict={}

for each in table_results:
    if(each[0]!="District of Columbia"):
        county = each[0].replace('County','').split(',')[0].strip()
        state = each[0].split(',')[1].strip()
        state = states_convert[state]
        area = county + "," + state
    else:
        area = each[0]
        
    date = each[1]
    rate=each[2]
    temp = str(date).replace('(p)','')
        
    if temp == 'Sep-20':
        temp = '20-Sep'
    
    month = datetime.datetime.strptime(temp,"%y-%b").month
    if area not in mysql_dict:
        mysql_dict[area]=[]
    
    mysql_dict[area].append([month,rate])

with open('data_empoly.json', 'w') as outfile:
    json.dump(mysql_dict, outfile)