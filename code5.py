from OpenSSL import SSL

ctx = SSL.Context(SSL.TLSv1_2_METHOD)
ctx.set_verify(SSL.VERIFY_PEER, verify_callback)
