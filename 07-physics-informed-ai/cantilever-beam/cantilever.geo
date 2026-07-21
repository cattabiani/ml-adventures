DefineConstant[ L = {2.0, Name "Geometry/L"} ];
DefineConstant[ H = {0.5, Name "Geometry/H"} ];
DefineConstant[ lc = {0.05, Name "Geometry/lc"} ];
DefineConstant[ E = {1000.0, Name "Material/E"} ];
DefineConstant[ nu = {0.3, Name "Material/nu"} ];
DefineConstant[ mu = {E / (2.0 * (1.0 + nu)), Name "Material/mu"} ];
DefineConstant[ lambda = {E * nu / ((1.0 + nu) * (1.0 - 2.0 * nu)), Name "Material/lambda"} ];
DefineConstant[ traction_force_x = {0.0, Name "Load/traction_force_x"} ];
DefineConstant[ traction_force_y = {-1.0, Name "Load/traction_force_y"} ];

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
