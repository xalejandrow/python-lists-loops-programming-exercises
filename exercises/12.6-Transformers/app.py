incoming_ajax_data = [
	{ "name": 'Mario', "last_name": 'Montes' },
	{ "name": 'Joe', "last_name": 'Biden' },
	{ "name": 'Bill', "last_name": 'Clon' },
	{ "name": 'Hilary', "last_name": 'Mccafee' },
	{ "name": 'Bobby', "last_name": 'Mc birth' }
]

#Your code go here:
def data_transformer(list1):
	return list(map(lambda person: person["name"] + ' ' + person["last_name"] ,list1 ))

print(data_transformer(incoming_ajax_data))