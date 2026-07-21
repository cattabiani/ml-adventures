L = 2.0;
H = 0.5;
lc = 0.05; // element size

Point(1) = {0, 0, 0, lc};
Point(2) = {L, 0, 0, lc};
Point(3) = {L, H, 0, lc};
Point(4) = {0, H, 0, lc};

Line(1) = {1, 2}; // bottom
Line(2) = {2, 3}; // right (traction)
Line(3) = {3, 4}; // top
Line(4) = {4, 1}; // left (clamped)

Curve Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

Physical Curve("clamped") = {4};
Physical Curve("traction") = {2};
Physical Surface("domain") = {1};
