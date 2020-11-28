import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        xv = np.linspace(-2*np.pi,2*np.pi,1000)
        fighand=plt.gca()
        foundsin, foundcos, foundtan = False, False, False
        for k in range(3) :
           figdat = fighand.get_lines()[k].get_xydata()
           this_x, this_y = zip(*figdat)
           self.assertTrue( len(this_x)==1000, "One or more of your data series contains the wrong number of points" )
           if np.abs( np.sin(xv[1])-this_y[1] )<1e-7 : 
              foundsin=True
              for i in range( len(this_x) ) : 
                  self.assertTrue( np.abs(xv[i]-this_x[i])<1e-7, "The x values for your graphs are not correct" )
                  self.assertTrue( np.abs(np.sin(this_x[i])-this_y[i])<1e-4, , "The y values for one of your graphs is not correct" )
           elif np.abs( np.cos(xv[1])-this_y[1] )<1e-7 : 
              foundcos=True
              for i in range( len(this_x) ) : 
                  self.assertTrue( np.abs(xv[i]-this_x[i])<1e-7, "The x values for your graphs are not correct" )
                  self.assertTrue( np.abs(np.cos(this_x[i])-this_y[i])<1e-4, , "The y values for one of your graphs is not correct" )
           elif np.abs( np.tan(xv[1])-this_y[1] )<1e-7 :
              foundtan=True
              for i in range( len(this_x) ) : 
                  self.assertTrue( np.abs(xv[i]-this_x[i])<1e-7, "The x values for your graphs are not correct" )
                  self.assertTrue( np.abs(np.tan(this_x[i])-this_y[i])<1e-4, , "The y values for one of your graphs is not correct" )
           else :
              self.assertTrue( False, "The y values for one of your graphs is not correct" )
    
        self.assertTrue( foundsin and foundcos and foundtan, "The y values for one of your graphs is not correct" )
