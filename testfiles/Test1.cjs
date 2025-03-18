deselect(); reset();

gslp = [
    {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["a", "C0"], "name":"A", "pars":[-7.7441, 4.8564, 1], "pos":[-7.7441, 4.8564, 1], "recalc":["a", "C0"], "size":8, "type":"P", "visibool":true},
    {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["a", "C0"], "name":"B", "pars":[1.0172, 9.1879, 1], "pos":[1.0172, 9.1879, 1], "recalc":["a", "C0"], "size":8, "type":"P", "visibool":true},
    {"alg":"Join", "alpha":1, "args":["A", "B"], "color":[0.149, 0.3451, 0.451], "name":"a", "pars":[], "pos":[-0.0565, 0.1142, -0.9919], "recalc":[], "size":2, "type":"L", "visibool":true},
    {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["C0"], "name":"C", "pars":[-3.4454, -0.4922, 1], "pos":[-3.4454, -0.4922, 1], "recalc":["C0"], "size":8, "type":"P", "visibool":true},
    {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["C0"], "name":"D", "pars":[1.2141, 2.1001, 1], "pos":[1.2141, 2.1001, 1], "recalc":["C0"], "size":8, "type":"P", "visibool":true},
    {"alg":"Free", "alpha":1, "args":[], "color":[0.7882, 0.3686, 0.5255], "incidences":["C0"], "name":"E", "pars":[6.5628, 6.7925, 1], "pos":[6.5628, 6.7925, 1], "recalc":["C0"], "size":8, "type":"P", "visibool":true},
    {"alg":"ConicBy5", "alpha":1, "args":["A", "B", "C", "D", "E"], "color":[0.149, 0.3451, 0.451], "name":"C0", "pars":[], "pos":[[0.0259, -0.0332, 0.1993], [-0.0332, 0.0689, -0.3508], [0.1993, -0.3508, 0.8166]], "recalc":[], "size":2, "type":"C", "visibool":true}
];

update(); recalcall();