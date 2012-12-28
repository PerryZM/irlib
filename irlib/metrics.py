''' 
Informations Retrieval Library
==============================
Utilities
'''

# Author: Tarek Amr <@gr33ndata> 

import math

class Metrics:

    def euclid_vectors(self, a=[], b=[]):
        if len(a) != len(b):
            print len(a), '!=', len(b)
            raise Exception
        euclid_sqrd = 0
        for i in range(0,a.__len__()):
            euclid_sqrd += ((a[i] - b[i])*(a[i] - b[i]))
        return math.sqrt(euclid_sqrd)
