==========================
UKHAS Parser Configuration
==========================

Introduction
============

The UKHAS protocol is the most widely used at time of writing, and is
implemented by the UKHAS parser module. This document provides information
on how what configuration settings the UKHAS parser module expects.

Parser module configuration is given in the "sentence" dictionary of the
payload dictionary in a flight document.

Standard UKHAS Sentences
========================

A typical minimum UKHAS protocol sentence may be::

    $$habitat,123,13:16:24,51.123,0.123,11000*ABCD

This sentence starts with a double dollar sign (``$$``) followed by the
payload name (here ``habitat``), several comma-delimited fields and is then
terminated by an asterisk and four-digit CRC16 CCITT checksum (``*ABCD``).

In this typical case, the fields are a message ID, the time, a GPS
latitude and longitude in decimal degrees, and the current altitude.

However, both the checksum algorithm in use and the number, type and order of
fields may be configured per-payload.

Parser Module Configuration
===========================

The parser module expects to be given the payload name, the checksum algorithm,
the protocol name ("UKHAS") and a list of fields, each of which should at
least specify the field name and data type.

For example, a configuration for the above typical sentence might be:

.. code-block:: javascript

    "habitat": {
        "sentence": {
            "protocol": "UKHAS",
            "checksum": "crc16-ccitt",
            "fields": [
                {
                    "name": "message_count",
                    "type": "int"
                }, {
                    "name": "time",
                    "type": "time"
                }, {
                    "name": "latitude",
                    "type": "coordinate",
                    "format": "dd.dddd"
                }, {
                    "name": "longitude",
                    "type": "coordinate",
                    "format": "dd.dddd"
                }, {
                    "name": "altitude",
                    "type": "int"
                }
            ]
        },
        "filters": {
            "intermediate": [
                {
                    "type": "normal",
                    "callable": "habitat.filters.upper_case"
                }
            ], "post": [
            ]
        }
    }

Payload Name
------------

The payload name is given as the key to the configuration dictionary, in
the above case the string "habitat" on the first line.

Checksum Algorithms
-------------------

Three algorithms are available:

* CRC16 CCITT (``crc16-ccitt``):

  The recommended algorithm, uses two bytes
  transmitted as four ASCII digits in hexadecimal. Can often be
  calculated using libraries for your payload hardware platform.
  In particular, note that we use a polynomial of 0x1021 and a start
  value of 0xFFFF, without reversing the input. If implemented
  correctly, the string ``habitat`` should checksum to 0x3EFB.

* XOR (``xor``):

  The simplest algorithm, calculating the one-byte XOR
  over all the message data and transmitting as two ASCII digits in
  hexadecimal. ``habitat`` checksums to 0x63.

* Fletcher-16 (``fletcher-16``):

  Not recommended but supported. Uses a modulus of 255 by default, if
  modulus 256 is required use ``fletcher-16-256``.

In all cases, the checksum is of everything after the ``$$`` and before
the ``*``.

Field Names
-----------

Field names may be any string that does not start with an underscore.

Field Types
-----------

Supported types are:

* ``string``: a plain text string which is not interpreted in any way.
* ``float``: a value that should be interpreted as a floating point
  number. Transmitted as a string, e.g., "123.45", rather than in
  binary.
* ``int``: a value that should be interpreted as an integer.
* ``time``: a field containing the time as either ``HH:MM:SS`` or just
  ``HH:MM``. Will be interpreted into a time representation.
* ``coordinate``: a coordinate, see below

Coordinate Fields
-----------------

Coordinate fields are used to contain, for instance, payload latitude and
longitude. They have an additional configuration parameter, ``format``, which
is used to define how the coordinate should be parsed. Options are:

* ``dd.dddd``: decimal degrees, with any number of digits after the
  decimal point. Leading zeros are allowed.
* ``ddmm.mm``: degrees and decimal minutes, with the first two digits
  taken as the degrees and the rest as the minutes. Degrees must be
  padded to two digits, so for instance 2 degrees and 12.3 minutes
  should be transmitted as ``0212.3``.

In both cases, the number can be prefixed by a space or + or - sign.

Filters
-------

See :doc:`filters`
