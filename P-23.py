import crypt
from hashlib import pbkdf2_hmac
s = b'D8VxSmTZt2E2YV454mkqAY5e'
hash = pbkdf2_hmac('sha256', password, s, 100000)    # Noncompliant: salt is hardcoded
