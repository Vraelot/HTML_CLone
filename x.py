import csv

lines = list(csv.reader(open('data/data.csv')))[1:]

template_data = open('data/template.html').read()

for line in lines:
	if not line:
		continue;
	print(line)
	filename = 'outputs/{}.html'.format(line[1].replace(' ', '_'))
	filename_data = template_data.replace('[URL]', line[0])
	open(filename, 'w').write(filename_data)
