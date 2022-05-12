all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(item):
	#if item != None:
		#return item
	return '<li>'+item+'</li>'

def filter_colors(color):
	if color['sexy'] == True:
		return color

#new_colors = list(filter(generate_li,all_colors))
#new_colors = list(filter(filter_colors, map( lambda color: '<li>' + color['label'] + '</li>',all_colors)))
new_colors = list(filter(filter_colors, all_colors))
new_colors_map = list(map( lambda color: generate_li(color['label']),new_colors))
#new_colors_map = map( lambda color: generate_li(color['label']),new_colors)
#print(new_colors)
print(new_colors_map)