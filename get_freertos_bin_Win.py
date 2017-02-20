#!/usr/bin/env python

import sys
import os

def get_freertos_bin(iar_bin, freertos_bin, freertos_offset):
    print 'get binary begin'
    iar_bin_size = os.path.getsize(iar_bin)
    print 'iar bin size: %d' % iar_bin_size
    print 'offset: %d' % freertos_offset
    freertos_bin_size = iar_bin_size - freertos_offset
    if (freertos_bin_size < 0):
        print 'Error! parameter offset is invalid'
        return -1
    print 'freertos bin size: %d' % freertos_bin_size
    f_in = open(iar_bin,'rb')
    f_out = open(freertos_bin,'wb')
    f_in.seek(freertos_offset, 0)
    inbytes = f_in.read(freertos_bin_size)
    f_out.write(inbytes)
    f_in.close()
    f_out.close()
    print 'get binary done'
    return 1

if __name__=='__main__':
    retval = 0
    freertos_bin = 'freertos.bin'
    freertos_offset = '' 
    if (2>len(sys.argv)):
        print('usage: \n\t%s [input file] [offset]' % (sys.argv[0]))
        sys.exit(1)
    elif (2==len(sys.argv)):
        iar_bin = sys.argv[1]
    else:
        iar_bin = sys.argv[1]    
        freertos_offset = int(sys.argv[2])

    if (freertos_offset == ''):
        freertos_offset = 495616
    ret_val = get_freertos_bin(iar_bin,freertos_bin,freertos_offset)
        
    sys.exit(retval)