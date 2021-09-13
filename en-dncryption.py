import os
os.system ('clear')
print ('welcome to rv en-dncryption')
print ''' \033[33m        welcome wahit Hat islamic
                  Encrypt
                Mahmoud Hassan  
   '''
print ''' \033[34m
    +---------------------------------+
    | [+]                         [+] |
    | [+]      Mahmoud Hassan    [+]  |
    | [+]      Database_HK       [+]  |
    | [+]     rv-dn-en           [+]  |
    +---------------------------------+
'''

print ''' \033[36m
    1  > > > base64\t\t
select = raw_input('Select : ')
if select == '1' : 
        import base64
        print '''
        1 > > > Encrypt
        2 > > > Decrypt
        '''
        select = raw_input('Select : ')
        if select == '1' : 
            encrypt = raw_input('Enter anything for Encryption : ')
            en = base64.b64encode(encrypt)
            print 'Your Encryption : ' + en
        elif select == '2' :
            decrypt = raw_input('Enter anything for Decryption : ')
            de = base64.b64decode(decrypt)
            print 'Your Decryption : ' + de
