deselect(); reset();

gslp = [
 {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["a", "e", "g"], "name":"A", "pars":[-8.5644, 3.708, 1], "pos":[-8.5644, 3.708, 1], "recalc":["a", "E", "c", "d", "e", "g", "G", "H", "k", "K"], "size":8, "type":"P", "visibool":true},
 {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["a", "f", "h"], "name":"B", "pars":[4.397, 6.1362, 1], "pos":[4.397, 6.1362, 1], "recalc":["a", "E", "c", "d", "f", "h", "G", "H", "k", "K"], "size":8, "type":"P", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["A", "B"], "color":[0.149, 0.3451, 0.451], "name":"a", "pars":[], "pos":[-0.0346, 0.1849, -0.9822], "recalc":["E", "c", "d", "G", "k", "K"], "size":2, "type":"L", "visibool":true},
 {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["b", "c", "h"], "name":"C", "pars":[-6.5628, -2.0673, 1], "pos":[-6.5628, -2.0673, 1], "recalc":["b", "c", "F", "e", "f", "h", "G", "H", "k", "K"], "size":8, "type":"P", "visibool":true},
 {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["b", "d", "g"], "name":"D", "pars":[6.169, -1.5751, 1], "pos":[6.169, -1.5751, 1], "recalc":["b", "d", "F", "e", "f", "g", "G", "H", "k", "K"], "size":8, "type":"P", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["C", "D"], "color":[0.149, 0.3451, 0.451], "name":"b", "pars":[], "pos":[-0.0187, 0.4828, 0.8755], "recalc":["F", "e", "f", "G", "k", "K"], "size":2, "type":"L", "visibool":true},
 {"alg":"PointOnLine", "alpha":1, "args":["a"], "color":[0.7882, 0.3686, 0.5255], "incidences":["c", "d"], "name":"E", "pars":[-2.3954, 4.6924, 1], "pos":[-0.4395, 0.8798, 0.1811], "recalc":["c", "d", "G", "k", "K"], "size":8, "type":"P", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["C", "E"], "color":[0.149, 0.3451, 0.451], "name":"c", "pars":[], "pos":[-0.1834, 0.1095, -0.9769], "recalc":["G", "k"], "size":2, "type":"L", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["E", "D"], "color":[0.149, 0.3451, 0.451], "name":"d", "pars":[], "pos":[0.2276, 0.3041, -0.9251], "recalc":["K"], "size":2, "type":"L", "visibool":true},
 {"alg":"PointOnLine", "alpha":1, "args":["b"], "color":[0.7882, 0.3686, 0.5255], "incidences":["e", "f"], "name":"F", "pars":[-0.886, -1.6407, 1], "pos":[-0.3856, -0.8114, 0.4392], "recalc":["e", "f", "G", "k", "K"], "size":8, "type":"P", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["A", "F"], "color":[0.149, 0.3451, 0.451], "name":"e", "pars":[], "pos":[0.2608, 0.3608, 0.8955], "recalc":["G", "k"], "size":2, "type":"L", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["F", "B"], "color":[0.149, 0.3451, 0.451], "name":"f", "pars":[], "pos":[-0.8022, 0.53, 0.2749], "recalc":["K"], "size":2, "type":"L", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["A", "D"], "color":[0.149, 0.3451, 0.451], "name":"g", "pars":[], "pos":[0.2895, 0.8073, -0.5142], "recalc":["H", "k"], "size":2, "type":"L", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["C", "B"], "color":[0.149, 0.3451, 0.451], "name":"h", "pars":[], "pos":[-0.2409, 0.3218, -0.9156], "recalc":["H", "k"], "size":2, "type":"L", "visibool":true},
 {"alg":"Meet", "alpha":1, "args":["c", "e"], "color":[0.7882, 0.3686, 0.5255], "incidences":["k"], "name":"G", "pars":[-4.758, 0.9844, 1], "pos":[0.9602, -0.193, -0.2019], "recalc":["k"], "size":8, "type":"P", "visibool":true},
 {"alg":"Meet", "alpha":1, "args":["g", "h"], "color":[0.7882, 0.3686, 0.5255], "incidences":["k"], "name":"H", "pars":[-2.1657, 1.5422, 1], "pos":[-0.7645, 0.5183, 0.3833], "recalc":["k"], "size":8, "type":"P", "visibool":true},
 {"alg":"Join", "alpha":1, "args":["G", "H"], "color":[0.149, 0.3451, 0.451], "name":"k", "pars":[], "pos":[0.0745, -0.5196, 0.8512], "recalc":[], "size":2, "type":"L", "visibool":true},
 {"alg":"Meet", "alpha":1, "args":["d", "f"], "color":[0.7882, 0.3686, 0.5255], "incidences":[], "name":"K", "pars":[1.6407, 1.8048, 1], "pos":[0.597, 0.7069, 0.3793], "recalc":[], "size":8, "type":"P", "visibool":true}
];

update(); recalcall();