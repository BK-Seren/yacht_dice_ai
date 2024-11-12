from y_model import Ymodel
from y_view import Yview
from y_controller import Ycontroller

m = Ymodel()
v = Yview(m)
Ycontroller(m,v)