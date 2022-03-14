

{
    'name': 'empSkills',
    'version':'1.0',
    'category': 'empSkills',
    'sequence': 100,
    'summary': 'list employee empSkills , Proficiency level , Certification Status ',
    'description': 'list employee empSkills , Proficiency level , Certification Status ',

    'depends': [
        'hr',
        'skills'
    ],
    'data': [
        'views/empSkills.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}

