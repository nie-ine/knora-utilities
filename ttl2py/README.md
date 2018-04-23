TTL2PY
======

ttl2py is a script that generates equivalent python classes from
a set of given .ttl files, that define RDF properties and resources.
Since it was developed with a Knora-Base Ontology (KBO) environment
in mind, it also creates these classes automaticaly.
In addition, each class that is derived from the KBO 'Resource'-class
provides a method 'json' that delivers the objects data in a json-format
that can directly be used with the KNORA API v1.


Getting Started
---------------

    $ python3 ttl2py.py [-t <target-dir>| -h] <file|dir>
