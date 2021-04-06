#! /usr/bin/env python

import math
import numpy as np

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            return 1
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0

    # function returns a random double (0.22 to 0.25) according to an exponential distribution
    def Exponential(self, beta=1.):
      # make sure beta is consistent with an exponential
      if beta <= 0.:
        beta = 1.
      R = np.exp(-0.35*beta) + ((np.exp(-0.30*beta)-np.exp(-0.35*beta))*self.rand())

      X = -np.log(R)/beta

      return X


    def Category6(self,wt=0.2):
        #wt = Random.Exponential(self,beta=1)
        #wt = 0.35
        R = self.rand()
        face = 0.
        ty = (1 - wt)/5
        ty = ty * 6
        if R <= ty/6:
            face = 1

        elif R > ty/6 and R <= (2*ty)/6:
            face = 2

        elif R > (2*ty)/6 and R <= (3*ty)/6:
            face = 3

        elif R > (3*ty)/6 and R <= (4*ty)/6:
            face = 4

        elif R > (4*ty)/6 and R <= (5*ty)/6:
            face = 5

        else:
            face = 6

        return face


    def Category6f(self):
        R = self.rand()
        out = 0.
        if R <= 1/6:
            out = 1

        elif R > 1/6 and R <= 2/6:
            out = 2

        elif R > 2/6 and R <= 3/6:
            out = 3

        elif R > 3/6 and R <= 4/6:
            out = 4

        elif R > 4/6 and R <= 5/6:
            out = 5

        else:
            out = 6

        return out

