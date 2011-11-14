=================
User Voice Config
=================

Make it possible to enable `UserVoice <https://uservoice.com/>`_ in a
KARL site.

Product Backlog Description
===========================

As a site administrator, I can enable UserVoice integration by
providing an API Key and Account key.

Specifications
==============

- Initial effort, just spend half a day.

- Do this on a branch.

- Make a place in the configuration to put in the keys. Most likely,
  in the same spot as the Google Analytics registration: in the
  ``karl.ini`` file.

- As a demonstration, put a ``<a>`` link on the ``Communities`` page
  that is connected to UserVoice.

- The connection to UserVoice includes some salted key as a limited
  representation of the user for "Single Sign-On". See the example
  Python code below, from Jason.

- Thus, clicking on the link causes you to be identified using your
  first+last name from KARL, inside UserVoice.

Sample Python Code
==================

.. code-block:: python

   from Crypto.Cipher import AES
   import base64
   import hashlib
   import urllib
   import operator
   import array
   import simplejson as json

   message = {
     "guid" : "1276710098"
     "expires" : "2010-06-16 18:11:38",
     "display_name" : "Example User",
     "email" : "example@test.com",
     "url" : "http://example.com/users/1234",
     "avatar_url" : "http://example.com/users/1234/avatar.png"
     }
   block_size = 16
   mode = AES.MODE_CBC

   api_key = "REPLACE_WITH_REAL_KEY"
   account_key = 'REPLACE_WITH_REAL_KEY'
   iv = "OpenSSL for Ruby"

   json = json.dumps(message, separators=(',',':'))

   salted = api_key+account_key
   saltedHash = hashlib.sha1(salted).digest()[:16]

   json_bytes = array.array('b', json[0 : len(json)]) 
   iv_bytes = array.array('b', iv[0 : len(iv)])

   # # xor the iv into the first 16 bytes.
   for i in range(0, 16):
       json_bytes[i] = operator.xor(json_bytes[i], iv_bytes[i])

   pad = block_size - len(json_bytes.tostring()) % block_size
   data = json_bytes.tostring() + pad * chr(pad)
   aes = AES.new(saltedHash, mode, iv)
   encrypted_bytes = aes.encrypt(data)

   param_for_uservoice_sso = urllib.quote(base64.b64encode(encrypted_bytes))
