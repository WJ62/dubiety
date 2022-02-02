This package introduces a new type of object that permits the user to give, if desired, an uncertainty to a value. Plus, 
you will have the ability to use these values in basic arithmetic calculations and have the uncertainty properly propagated 
(with a non-uncertain and uncertain value). For more possible operations (such as the trigonometric ones [more to come in 
the future]), use the dmath class of functions available through the package. The uncertainty is calculated following the 
equations found in Data reduction and error analysis for the Physical Sciences by Philip R. Bevington and D. Keith Robinson 
(McGraw-Hill). The reson behind the project is to simplify the data data analysis that has to be done in my PHY1501 class 
for the physics bacc. at the university of Montreal that I'm currently taking.

Example of use :

import dubiety,dmath

1)
dubiety(32.9038,0.0323)
>>> 32.90 ± 0.03

2)
dubiety(32.9038,0.0323,onecs=False)
>>> 32.9038 ± 0.0323

3)
dubiety(13.878,0.0623)+dubiety(32.9038,0.0323)
>>> 46.78 ± 0.09

4)
dmath.sin(dubiety(13.878,0.0623))
>>> 0.24 ± 0.06
