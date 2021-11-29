import Cookie

HTTP_COOKIE = r'integer=5; string_with_quotes="He said, \"Hello, World!\""'

print ('From constructor:')
c = Cookie.SimpleCookie(HTTP_COOKIE)
print (c)

print()
print ('From load():')
c = Cookie.SimpleCookie()
c.load(HTTP_COOKIE)
print (c)

