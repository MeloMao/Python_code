#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#@author: rui.xu
#����ʹ��pycrypto?��
#���շ���:easy_install pycrypto?
 
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 
class prpcrypt():
    def __init__(self,key):
        self.key = key
        self.mode = AES.MODE_CBC
     
    #���ܺ��������text����16λ���ÿո���Ϊ16λ��
    #�������16��ʱ����16�ı������ǾͲ���Ϊ16�ı�����
    def encrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        #������Կkey ���ȱ���Ϊ16��AES-128��,
        #24��AES-192��,����32 ��AES-256��Bytes ����
        #ĿǰAES-128 �㹻Ŀǰʹ��
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #��ΪAES����ʱ��õ����ַ�����һ����ascii�ַ����ģ�������ն˻��߱���ʱ����ܴ�������
        #��������ͳһ�Ѽ��ܺ���ַ���ת��Ϊ16�����ַ���
        return b2a_hex(self.ciphertext)
     
    #���ܺ�ȥ������Ŀո���strip() ȥ��
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text  = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
 
if __name__ == '__main__':
    pc = prpcrypt('keyskeyskeyskeys') #��ʼ����Կ
    import sys
    e = pc.encrypt(sys.argv[1]) #����
    d = pc.decrypt(e) #����
    print "����:",e
    print "����:",d