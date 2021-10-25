import yaml


# Load yaml
with open('./nhsl.yml', 'r', encoding='utf-8') as f:
    nhsl_yml = yaml.load(f, Loader=yaml.Loader)


# Compare nhsl.yml in root dir to version in _data
with open('./nhsl.yml', 'r', encoding='utf-8') as f:
    f1 = f.read()
with open('./docs/_data/nhsl.yml', 'r', encoding='utf-8') as f:
    f2 = f.read()
    # If they are different, update _data version
    if f1 != f2:
        with open('https://github.com/DamonU2/national-human-settlement/blob/gh-pages/docs/_data/nhsl.yml', 'w', encoding='utf-8') as g:
            g.write(f1)


for lang in ['en', 'fr']:
    # Endlines staying as \n without replacement
    description = nhsl_yml['description'][lang].replace('\\n', '\n')

    # Generate links to available datasets
    datasets = ''
    for layer in nhsl_yml['layers']:
        set = [x for x in nhsl_yml['datasets'] if x['id'] == layer][0]
        datasets += f'- [{set["title"][lang]}](https://github.com/OpenDRR/national-human-settlement/tree/main/{set["folder"]})' + '\n'

    # Language dependant variables
    if lang == 'en':
        filename = 'README.md'
        link_start = '[En français](https://github.com/OpenDRR/national-human-settlement/blob/main/'
        link_end = '/LISEZMOI.md)'
    elif lang == 'fr':
        filename = 'LISEZMOI.md'
        link_start = '[In English](https://github.com/OpenDRR/national-human-settlement/blob/main/'
        link_end = '/README.md)'

    # Readme text
    readme = link_start + link_end[1:] + '\n\n' + \
        nhsl_yml['header'][lang] + description + '\n'
    readme += '### ' + nhsl_yml['sets'][lang] + '\n\n' + datasets + '\n'
    readme += '## ' + nhsl_yml['technical']['title'][lang] + \
        '\n\n' + nhsl_yml['technical']['body'][lang] + '\n'
    readme += '## ' + nhsl_yml['documentation']['title'][lang] + \
        '\n\n' + nhsl_yml['documentation']['body'][lang] + '\n'
    readme += '## ' + nhsl_yml['acceptable']['title'][lang] + \
        '\n\n' + nhsl_yml['acceptable']['body'][lang] + '\n'
    readme += '## ' + nhsl_yml['attribution']['title'][lang] + \
        '\n\n' + nhsl_yml['attribution']['body'][lang]

    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(readme)

    # Generate readme's for active layers
    for layer in nhsl_yml['layers']:
        set = [x for x in nhsl_yml['datasets'] if x['id'] == layer][0]
        description = set['description'][lang].replace('\\n', '\n')

        # Write file
        with open(f'./{set["folder"]}/{filename}', 'w', encoding='utf-8') as f:
            f.write(link_start + set["folder"] + link_end + '\n' + set['header']
                    [lang] + ' ' + set["title"][lang] + '\n\n' + description)
