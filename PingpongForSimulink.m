function [Output] = PingpongForSimulink( x, xp, xpp, y, yp, ypp, thetaDegrees, Vi )
if( nargin ~= 1 ) error( 'PingpongForSimulink expects 8 (not %d) command line arguments.', nargin ),  end
%===========================================================================
% File: PingpongForSimulink.m created Jan 22 2019 by MotionGenesis 5.9.
% Portions copyright (c) 2009-2017 Motion Genesis LLC.  Rights reserved.
% Student Licensee: Simon Therrien (until March 2022).
% Paid-up MotionGenesis Student licensees are granted the right
% to distribute this code for legal student-academic (non-professional) purposes only,
% provided this copyright notice appears in all copies and distributions.
%===========================================================================
% The software is provided "as is", without warranty of any kind, express or    
% implied, including but not limited to the warranties of merchantability or    
% fitness for a particular purpose. In no event shall the authors, contributors,
% or copyright holders be liable for any claim, damages or other liability,     
% whether in an action of contract, tort, or otherwise, arising from, out of, or
% in connection with the software or the use or other dealings in the software. 
%===========================================================================


%-------------------------------+--------------------------+-------------------+-----------------
% Quantity                      | Value                    | Units             | Description
%-------------------------------|--------------------------|-------------------|-----------------
coefDrag                        =  0.47;                   % noUnits             Constant
g                               =  9.8;                    % m/s^2               Constant
m                               =  0.0027;                 % kg                  Constant
r                               =  0.02;                   % m                   Constant
rho                             =  1.1123;                 % kg/m^3              Constant
%-------------------------------+--------------------------+-------------------+-----------------

% Unit conversions.  UnitSystem: lbm, ft, sec.
g = g * 3.280839895013124;                                 %  Converted from m/s^2 
m = m * 2.204622621848776;                                 %  Converted from kg 
r = r * 3.280839895013124;                                 %  Converted from m 
rho = rho * 0.0624279605761446;                            %  Converted from kg/m^3 


%===========================================================================
vMag = sqrt(xp^2+yp^2);
Area = pi*r^2;



%===========================================================================
Output = zeros( 1, 6 );

Output(1) = x*0.3048;
Output(2) = xp*0.3048;
Output(3) = xpp*0.3048;
Output(4) = y*0.3048;
Output(5) = yp*0.3048;
Output(6) = ypp*0.3048;

%============================================
end    % End of function PingpongForSimulink
%============================================
