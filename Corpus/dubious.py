import numpy as np

def mult_dub(f,a,a_,b,b_):
    cov=np.cov(a,b,bias=True)[0][1]
    cov2=2*((cov**2)/(a*b))
    term1=(a_/a)**2
    term2=(b_/b)**2
    comp=np.sqrt((term1+term2+cov2)*(f**2))
    return comp
def div_dub(f,a,a_,b,b_):
    cov=np.cov(a,b,bias=True)[0][1]
    cov2=2*((cov**2)/(a*b))
    term1=(a_/a)**2
    term2=(b_/b)**2
    comp=np.sqrt((term1+term2-cov2)*(f**2))
    return comp
def pow_dub(f,a,a_,b):
    term1=a_/a
    comp=f*b*term1
    return comp

def cs(duby,cs=1):
    x=duby[1]
    y='{:e}'.format(x)
    try:
        indx=int(y.split('e-')[1])
    except IndexError:
        indx=0
    dubyn='{0:.{1}f}'.format(duby[0],indx+cs-1)
    dubyw='{0:.{1}f}'.format(duby[1],indx+cs-1)
    return (dubyn,dubyw)

class dubiety():
    """Type of object that can take into concideration a certain uncertanty on a value"""
    def __init__(self,norm,worry=0,onecs=True):
        self.norm=norm
        self.worry=worry
        self.onecs=onecs
        self.dubiety=(self.norm,self.worry)
    def __repr__(self):
        if self.onecs:
            self.dubiety=cs(self.dubiety)
        return '{} ± {}'.format(self.dubiety[0],self.dubiety[1])
    def __getitem__(self,i):
        return self.dubiety[i]
    def __setitem__(self,i,value):
        self.dubiety[i]=value
    def __add__(self, other):
        if type(other)!=dubiety:
            other=dubiety(other)
        norm=self.norm+other.norm
        worry=self.worry+other.worry
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __radd__(self, other):
        if type(other)!=dubiety:
            other=dubiety(other)
        norm=self.norm+other.norm
        worry=self.worry+other.worry
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __sub__(self, other):
        if type(other)!=dubiety:
            other=dubiety(other)
        norm=self.norm-other.norm
        worry=self.worry+other.worry
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __rsub__(self,other):
        if type(other)!=dubiety:
            other=dubiety(other)
        norm=self.norm-other.norm
        worry=self.worry+other.worry
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __mul__(self,other):
        if type(other)!=dubiety:
            norm=self.norm*other
            worry=self.worry*other
        else:
            norm=self.norm*other.norm
            worry=mult_dub(norm,self.norm,self.worry,other.norm,other.worry)
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __rmul__(self,other):
        if type(other)!=dubiety:
            norm=self.norm*other
            worry=self.worry*other
        else:
            norm=self.norm*other.norm
            worry=mult_dub(norm,self.norm,self.worry,other.norm,other.worry)
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __truediv__(self,other):
        if type(other)!=dubiety:
            norm=self.norm/other
            worry=self.worry/other
        else:
            norm=self.norm/other.norm
            worry=div_dub(norm,self.norm,self.worry,other.norm,other.worry)
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __pow__(self,other):
        norm=self.norm**other
        worry=pow_dub(norm,self.norm,self.worry,other)
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])
    def __abs__(self):
        norm=abs(self.norm)
        worry=abs(self.worry)
        dub=(norm,worry)
        return dubiety(dub[0],dub[1])

class dmath():
    """Class of basic math functions modified to accept dubiety types"""
    def sin(duby):
        if type(duby)!=dubiety: 
            return np.sin(np.deg2rad(duby))
        norm=np.sin(np.deg2rad(duby.norm))
        worry=duby.worry*np.cos(np.deg2rad(norm))
        return dubiety(norm,worry)
    def cos(duby):
        if type(duby)!=dubiety: 
            return np.cos(np.deg2rad(duby))
        norm=np.cos(np.deg2rad(duby.norm))
        worry=(-1)*duby.worry*np.sin(np.deg2rad(norm))
        return dubiety(norm,worry)
    def ln(duby):
        pass
