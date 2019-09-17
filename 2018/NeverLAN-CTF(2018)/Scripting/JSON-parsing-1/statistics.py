from re import findall
# made by munsiwoo

antivirusList = ['Bkav','K7AntiVirus','MicroWorld-eScan','nProtect','CMC','CAT-QuickHeal',
'ALYac','Malwarebytes','Zillya','SUPERAntiSpyware','TheHacker','K7GW','CrowdStrike',
'Arcabit','Invincea','Baidu','F-Prot','Symantec','TotalDefense','TrendMicro-HouseCall',
'Avast','ClamAV','Kaspersky','BitDefender','NANO-Antivirus','Paloalto','ViRobot','Tencent',
'Ad-Aware','Emsisoft','Comodo','F-Secure','DrWeb','VIPRE','TrendMicro','McAfee-GW-Edition',
'Sophos','Ikarus','Cyren','Jiangmin','Webroot','Avira','Antiy-AVL','Kingsoft','Endgame',
'Microsoft','AegisLab','ZoneAlarm','Avast-Mobile','GData','AhnLab-V3','McAfee','AVware',
'MAX','VBA32','Cylance','WhiteArmor','Zoner','ESET-NOD32','Rising','Yandex','SentinelOne',
'eGambit','Fortinet','AVG','Panda','Qihoo-360', 'SymantecMobileInsight', 'Alibaba', 'Trustlook']

antivirus = []
totalCount = []

file = open("file-20171020T1500", 'r')
read = file.read()

find = findall("\"([a-zA-Z0-9-]+)\": {\"detected\": (true|false)", read)
i = 0

for x in find :
	if(x[1] == 'true') :
		i += 1
		#print(str(i)+" : "+x[0])
		antivirus.append(x[0]) 

#print(i)
#print(len(antivirus))

for y in antivirusList :
	count = antivirus.count(y)
	#antivirus = list(filter(lambda word: word != y, antivirus))
	print(y + " : " + str(count))
	totalCount.append(count)

totalCount.sort()

print(totalCount)
#print(antivirus)

'''

ESET-NOD32,Ikarus,McAfee,CAT-QuickHeal,DrWeb
ESET-NOD32,Ikarus,McAfee,CAT-QuickHeal,Fortinet

Why is not it auth???

'''