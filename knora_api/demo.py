#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sascha KAUFMANN"
__copyright__ = "Copyright 2018, NIE-INE"
__credits__ = []
__license__ = "3-Clause BSD License"
__version__ = "0.0.1"
__maintainer__ = "Sascha KAUFMANN"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Beta"

import sys
import knora_api


def main():
    """
    A demo script to demonstrate some features of 'knora_api'
    """

    # open a session to a server where Knora is hosted
    cur_session = knora_api.open(host='localhost',
                                 port=3333,
                                 user='<user id>',
                                 password='<password>',
                                 cache="test")

    # show the projects, the server is hosting ...
    projects = cur_session.get_projects()
    print("Following projects are stored at the server:")
    print(projects)
    print()

    # ... and the vocabularies
    print("Following vocabularies are used:")
    vocabularies = cur_session.get_vocabularies()
    print(vocabularies)
    print()

    # create some Person, Gender and Group instances
    # (see ttl2py.py, too)
    from demo_ontologies.human.classes.Person import Person
    from demo_ontologies.human.classes.Female import Female
    from demo_ontologies.human.classes.Male import Male
    from demo_ontologies.agent.classes.Group import Group

    try:
        # create a group ...
        group = Group(label='Club of the unknown')
        # ... get its json representation
        group_js = group.json()
        # ... and store it in Knora
        group_resource_id = cur_session.post_resource(json=group_js)

        # of course, we can also do this in one step
        female_resource_id = cur_session.post_resource(json=Female(label='a female').json())
        male_resource_id = cur_session.post_resource(json=Male(label='A male').json())

        # now, we are going to create two persons
        # (note how we link a the gender to a person's sex by using the gender's resource_id
        #  we got in return, when we created the gender)
        female_person = Person(label='Jane Doe',
                               hasFamilyName='Doe',
                               hasGivenName='Jane',
                               hasBirthDate='1950',
                               hasBiologicalSex=female_resource_id)
                             #  isMemberOf=group_resid)
        male_person = Person(label='John Doe',
                             hasFamilyName='Doe',
                             hasGivenName='John',
                             hasBirthDate='1950-01-30',
                             hasBiologicalSex=male_resource_id)
                             # isMemberOf=group_resid)

        jane_resource_id = cur_session.post_resource(json=female_person.json())
        print("Now we are using the cache")
        john_resource_id = cur_session.post_resource(json=male_person.json(), cache_key='John_Doe')
        print("ResourceID after 1. attempt: {}",format(john_resource_id))
        john_resource_id_b = cur_session.post_resource(json=male_person.json(), cache_key='John_Doe')
        print("ResourceID after 2. attempt: {}",format(john_resource_id))
        print()


        # Just
        if jane_resource_id:
            janes_data = cur_session.get_resource(jane_resource_id)
            print("Jane's data (full set of information):")
            print(janes_data)

        print()
        if john_resource_id:
            # the following is a short form of
            #   johns_data = cur_session.get_resource(john_resource_id)
            #   print(johns_data['props'])
            print("John's data (properties only):")
            print(cur_session.get_properties(john_resource_id))

        cur_session.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    sys.exit(main())

