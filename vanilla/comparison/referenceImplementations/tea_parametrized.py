from ctypes import *

def encipher(v, k, delta, n):
    y=c_uint32(v[0])
    z=c_uint32(v[1])
    sum=c_uint32(0)
    #delta=0x9E3779B9; these are now parameters!
    #n=32
    w=[0,0]

    while(n>0):
        sum.value += delta
        y.value += ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        z.value += ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        n -= 1

    w[0]=y.value
    w[1]=z.value
    return w

def decipher(v, k, delta, n):
    y=c_uint32(v[0])
    z=c_uint32(v[1])
    #sum=c_uint32(0xC6EF3720)
    sum = c_uint32(delta << 4)
    #delta=0x9E3779B9 these are now parameters!
    #n=32
    w=[0,0]

    while(n>0):
        z.value -= ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        y.value -= ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        sum.value -= delta
        n -= 1

    w[0]=y.value
    w[1]=z.value
    return w