from OpenSSL import SSL

ctx2 = SSL.Context(SSL.TLSv1_2_METHOD)
ctx2.set_verify(SSL.VERIFY_NONE, verify_callback)
