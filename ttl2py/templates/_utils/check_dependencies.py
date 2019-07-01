#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from modules.nie_ontologies.knora_base.properties.hasLinkTo import LinkValue


def check_dependencies(resources, sanitize=False):
        """
        Checks if a linkValue refers to a resource within the same dictionary

        :param resources: dictionary of resources, where the key represents
                          a resources 'virtual' name during a bulk import
        :return:
        """

        noteable_resources = {}
        if not isinstance(resources, dict):
            return noteable_resources
        try:
            for key, resource in resources.items():
                try:
                    for attr, value in resource.__dict__.items():
                        if not value:
                            continue
                        if isinstance(value, LinkValue):
                            # process LinkValue values
                            target = value.target
                            if 'ref' == value.linkType.lower() and target and target not in resources:
                                if key not in noteable_resources:
                                    noteable_resources[key] = set()
                                noteable_resources[key].add(target)
                                if sanitize:
                                    setattr(resource, attr, None)
                            continue
                        elif isinstance(value, list) or isinstance(value, set):
                            # process collection
                            tmp_collection = set() if sanitize else None
                            for item in value:
                                if isinstance(item, LinkValue):
                                    target = item.target
                                    if 'ref' == item.linkType.lower() and target and target not in resources:
                                        if key not in noteable_resources:
                                            noteable_resources[key] = set()
                                        noteable_resources[key].add(target)
                                        continue
                                if sanitize:
                                    tmp_collection.add(item)
                            if sanitize and (not tmp_collection or len(tmp_collection) < len(value)):
                                if not tmp_collection:
                                    tmp_collection = None
                                elif isinstance(value, list):
                                    tmp_collection = [*tmp_collection, ]
                                setattr(resource, attr, tmp_collection)
                except Exception as e:
                    print("Error (1) in check_dependencies.py ({})", format(e))
        except Exception:
            print("Error (2) in check_dependencies.py ({})", format(e))
            pass

        return noteable_resources
