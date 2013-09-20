============
NpSchematics
============

Numpy types for Schematics.

[![Build Status](https://travis-ci.org/adamlwgriffiths/npschematics.png?branch=master)](https://travis-ci.org/adamlwgriffiths/npschematics)


About
=====

Adds Numpy Types to the Schematics module.

Schematics is a Python library to combine types into structures, validate them,
and transform the shapes of your data based on simple descriptions.

The internals are similar to ORM type systems, but there is no database layer
in Schematics.  Instead, Schematics believes the task of building a database
layer is made significantly easier when Schematics handles everything but
writing the query.

Further, it can be used for a range of tasks where having a database involved
may not make sense.

Benefits of using Numpy Schematics Types:

+ Enforce Numpy properties: dtype, size, shape, ndim.
+ Serialise / deserialise data


Examples
--------

This is a simple Model with Schamtics and NpSchematics.

```
  >>> from schematics.models import Model
  >>> from schematics.types import StringType, URLType
  >>> from npschematics.types import NumpyArrayType
  >>> import numpy as np
  >>> class Person(Model):
  ...     name = StringType(required=True)
  ...     website = URLType()
  ...     ratings = NumpyArrayType(required=True, dtype='int16', shape=(5,), default=np.array([0]*5))
  ...
  >>> person = Person({'name': u'Joe Strummer', 
  ...                  'website': 'http://soundcloud.com/joestrummer'})
  >>> person.name
  u'Joe Strummer'
  >>> person.ratings
  [0, 0, 0, 0, 0]
```

Serializing the data to JSON.

```
  >>> import json
  >>> json.dumps(person.to_primitive())
  {"name": "Joe Strummer", "website": "http://soundcloud.com/joestrummer", "ratings": "[0, 0, 0, 0, 0]"}
```

Let's try validating with an invalid shape.

```
  >>> person = Person()
  >>> person.ratings = [1,2,3]
  >>> person.validate()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "schematics/models.py", line 231, in validate
      raise ModelConversionError(e.messages)
  schematics.exceptions.ModelConversionError: {'ratings': [u'Could not convert shape']}
```

Add the field and validation passes

```
  >>> person = Person()
  >>> person.name = 'Amon Tobin'
  >>> person.website = 'http://www.amontobin.com/'
  >>> person.ratings = [1,2,3,4,5]
  >>> person.validate()
  >>> 
```
