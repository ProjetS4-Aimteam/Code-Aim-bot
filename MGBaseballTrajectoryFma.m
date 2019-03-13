function [t,VAR,Output] = MGBaseballTrajectoryFma( thetaDegrees )
if( nargin ~= 1 ) error( 'MGBaseballTrajectoryFma expects 1 (not %d) command line arguments.', nargin ),  end
%===========================================================================
% File: MGBaseballTrajectoryFma.m created Jan 22 2019 by MotionGenesis 5.9.
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
%   yp = -0.7 * yp;
%===========================================================================
eventDetectedByIntegratorTerminate1OrContinue0 = [];
xpp=0; ypp=0; Area=0; vMag=0;


%-------------------------------+--------------------------+-------------------+-----------------
% Quantity                      | Value                    | Units             | Description
%-------------------------------|--------------------------|-------------------|-----------------
coefDrag                        =  0.47;                   % noUnits             Constant
g                               =  9.8;                    % m/s^2               Constant
m                               =  0.0027;                 % kg                  Constant
r                               =  0.02;                   % m                   Constant
rho                             =  1.1123;                 % kg/m^3              Constant

x                               =  0;                      % m                   Initial Value
y                               =  0.3;                    % m                   Initial Value
xp                              =  4.060207137573157;      % m/s                 Initial Value
yp                              =  4.060207137573156;      % m/s                 Initial Value

tInitial                        =  0.0;                    % sec                 Initial Time
tFinal                          =  1.6;                    % sec                 Final Time
tStep                           =  0.01;                   % sec                 Integration Step
printIntScreen                  =  1;                      % 0 or +integer       0 is NO screen output
printIntFile                    =  1;                      % 0 or +integer       0 is NO file   output
absError                        =  1.0E-7;                 %                     Absolute Error
relError                        =  1.0E-08;                %                     Relative Error
%-------------------------------+--------------------------+-------------------+-----------------

% Unit conversions.  UnitSystem: lbm, ft, sec.
g = g * 3.280839895013124;                                 %  Converted from m/s^2 
m = m * 2.204622621848776;                                 %  Converted from kg 
r = r * 3.280839895013124;                                 %  Converted from m 
rho = rho * 0.0624279605761446;                            %  Converted from kg/m^3 
x = x * 3.280839895013124;                                 %  Converted from m 
y = y * 3.280839895013124;                                 %  Converted from m 
xp = xp * 3.280839895013124;                               %  Converted from m/s 
yp = yp * 3.280839895013124;                               %  Converted from m/s 

% Evaluate constants
Area = pi*r^2;


VAR = SetMatrixFromNamedQuantities;
[t,VAR,Output] = IntegrateForwardOrBackward( tInitial, tFinal, tStep, absError, relError, VAR, printIntScreen, printIntFile );
OutputToScreenOrFile( [], 0, 0 );   % Close output files



%===========================================================================
function sys = mdlDerivatives( t, VAR, uSimulink )
%===========================================================================
SetNamedQuantitiesFromMatrix( VAR );
vMag = sqrt(xp^2+yp^2);
xpp = -0.5*coefDrag*rho*Area*xp*vMag/m;
ypp = -g - 0.5*coefDrag*rho*Area*yp*vMag/m;

sys = transpose( SetMatrixOfDerivativesPriorToIntegrationStep );
end



%===========================================================================
function VAR = SetMatrixFromNamedQuantities
%===========================================================================
VAR = zeros( 1, 4 );
VAR(1) = x;
VAR(2) = y;
VAR(3) = xp;
VAR(4) = yp;
end


%===========================================================================
function SetNamedQuantitiesFromMatrix( VAR )
%===========================================================================
x = VAR(1);
y = VAR(2);
xp = VAR(3);
yp = VAR(4);
end


%===========================================================================
function VARp = SetMatrixOfDerivativesPriorToIntegrationStep
%===========================================================================
VARp = zeros( 1, 4 );
VARp(1) = xp;
VARp(2) = yp;
VARp(3) = xpp;
VARp(4) = ypp;
end



%===========================================================================
function Output = mdlOutputs( t, VAR, uSimulink )
%===========================================================================
Output = zeros( 1, 2 );
Output(1) = x*0.3048;
Output(2) = y*0.3048;
end


%===========================================================================
function OutputToScreenOrFile( Output, shouldPrintToScreen, shouldPrintToFile )
%===========================================================================
persistent FileIdentifier hasHeaderInformationBeenWritten;

if( isempty(Output) ),
   if( ~isempty(FileIdentifier) ),
      fclose( FileIdentifier(1) );
      clear FileIdentifier;
      fprintf( 1, '\n Output is in the file MGBaseballTrajectoryFma.1\n' );
      fprintf( 1, '\n Note: To automate plotting, issue the command OutputPlot in MotionGenesis.\n' );
      fprintf( 1, '\n To load and plot the first two columns in file MGBaseballTrajectoryFma.1, enter the following:\n' );
      fprintf( 1, '    someName = load( ''MGBaseballTrajectoryFma.1'' );\n' );
      fprintf( 1, '    plot( someName(:,1), someName(:,2) )\n\n' );
   end
   clear hasHeaderInformationBeenWritten;
   return;
end

if( isempty(hasHeaderInformationBeenWritten) ),
   if( shouldPrintToScreen ),
      fprintf( 1,                '%%       x              y\n' );
      fprintf( 1,                '%%      (m)            (m)\n\n' );
   end
   if( shouldPrintToFile && isempty(FileIdentifier) ),
      FileIdentifier(1) = fopen('MGBaseballTrajectoryFma.1', 'wt');   if( FileIdentifier(1) == -1 ), error('Error: unable to open file MGBaseballTrajectoryFma.1'); end
      fprintf(FileIdentifier(1), '%% FILE: MGBaseballTrajectoryFma.1\n%%\n' );
      fprintf(FileIdentifier(1), '%%       x              y\n' );
      fprintf(FileIdentifier(1), '%%      (m)            (m)\n\n' );
   end
   hasHeaderInformationBeenWritten = 1;
end

if( shouldPrintToScreen ), WriteNumericalData( 1,                 Output(1:2) );  end
if( shouldPrintToFile ),   WriteNumericalData( FileIdentifier(1), Output(1:2) );  end
end


%===========================================================================
function WriteNumericalData( fileIdentifier, Output )
%===========================================================================
numberOfOutputQuantities = length( Output );
if( numberOfOutputQuantities > 0 ),
   for( i = 1 : numberOfOutputQuantities ),
      fprintf( fileIdentifier, ' %- 14.6E', Output(i) );
   end
   fprintf( fileIdentifier, '\n' );
end
end



%===========================================================================
function [functionsToEvaluateForEvent, eventTerminatesIntegration1Otherwise0ToContinue, eventDirection_AscendingIs1_CrossingIs0_DescendingIsNegative1] = EventDetection( t, VAR, uSimulink )
%===========================================================================
% Detects when designated functions are zero or cross zero with positive or negative slope.
% Step 1: Uncomment call to mdlDerivatives and mdlOutputs.
% Step 2: Change functionsToEvaluateForEvent,                      e.g., change  []  to  [t - 5.67]  to stop at t = 5.67.
% Step 3: Change eventTerminatesIntegration1Otherwise0ToContinue,  e.g., change  []  to  [1]  to stop integrating.
% Step 4: Change eventDirection_AscendingIs1_CrossingIs0_DescendingIsNegative1,  e.g., change  []  to  [1].
% Step 5: Possibly modify function EventDetectedByIntegrator (if eventTerminatesIntegration1Otherwise0ToContinue is 0).
%---------------------------------------------------------------------------
% mdlDerivatives( t, VAR, uSimulink );        % UNCOMMENT FOR EVENT HANDLING
% mdlOutputs(     t, VAR, uSimulink );        % UNCOMMENT FOR EVENT HANDLING
functionsToEvaluateForEvent = [];
eventTerminatesIntegration1Otherwise0ToContinue = [];
eventDirection_AscendingIs1_CrossingIs0_DescendingIsNegative1 = [];
eventDetectedByIntegratorTerminate1OrContinue0 = eventTerminatesIntegration1Otherwise0ToContinue;
end


%===========================================================================
function [isIntegrationFinished, VAR] = EventDetectedByIntegrator( t, VAR, nIndexOfEvents )
%===========================================================================
isIntegrationFinished = eventDetectedByIntegratorTerminate1OrContinue0( nIndexOfEvents );
if( ~isIntegrationFinished ),
   SetNamedQuantitiesFromMatrix( VAR );
%  Put code here to modify how integration continues.
   VAR = SetMatrixFromNamedQuantities;
end
end



%===========================================================================
function [t,VAR,Output] = IntegrateForwardOrBackward( tInitial, tFinal, tStep, absError, relError, VAR, printIntScreen, printIntFile )
%===========================================================================
OdeMatlabOptions = odeset( 'RelTol',relError, 'AbsTol',absError, 'MaxStep',tStep, 'Events',@EventDetection );
t = tInitial;                 epsilonT = 0.001*tStep;                   tFinalMinusEpsilonT = tFinal - epsilonT;
printCounterScreen = 0;       integrateForward = tFinal >= tInitial;    tAtEndOfIntegrationStep = t + tStep;
printCounterFile   = 0;       isIntegrationFinished = 0;
mdlDerivatives( t, VAR, 0 );
while 1,
   if( (integrateForward && t >= tFinalMinusEpsilonT) || (~integrateForward && t <= tFinalMinusEpsilonT) ), isIntegrationFinished = 1;  end
   shouldPrintToScreen = printIntScreen && ( isIntegrationFinished || printCounterScreen <= 0.01 );
   shouldPrintToFile   = printIntFile   && ( isIntegrationFinished || printCounterFile   <= 0.01 );
   if( isIntegrationFinished || shouldPrintToScreen || shouldPrintToFile ),
      Output = mdlOutputs( t, VAR, 0 );
      OutputToScreenOrFile( Output, shouldPrintToScreen, shouldPrintToFile );
      if( isIntegrationFinished ), break;  end
      if( shouldPrintToScreen ), printCounterScreen = printIntScreen;  end
      if( shouldPrintToFile ),   printCounterFile   = printIntFile;    end
   end
   [TimeOdeArray, VarOdeArray, timeEventOccurredInIntegrationStep, nStatesArraysAtEvent, nIndexOfEvents] = ode45( @mdlDerivatives, [t tAtEndOfIntegrationStep], VAR, OdeMatlabOptions, 0 );
   if( isempty(timeEventOccurredInIntegrationStep) ),
      lastIndex = length( TimeOdeArray );
      t = TimeOdeArray( lastIndex );
      VAR = VarOdeArray( lastIndex, : );
      printCounterScreen = printCounterScreen - 1;
      printCounterFile   = printCounterFile   - 1;
      if( abs(tAtEndOfIntegrationStep - t) >= abs(epsilonT) ), warning('numerical integration failed'); break;  end
      tAtEndOfIntegrationStep = t + tStep;
      if( (integrateForward && tAtEndOfIntegrationStep > tFinal) || (~integrateForward && tAtEndOfIntegrationStep < tFinal) ) tAtEndOfIntegrationStep = tFinal;  end
   else
      t = timeEventOccurredInIntegrationStep( 1 );    % time  at firstEvent = 1 during this integration step.
      VAR = nStatesArraysAtEvent( 1, : );             % state at firstEvent = 1 during this integration step.
      printCounterScreen = 0;
      printCounterFile   = 0;
      [isIntegrationFinished, VAR] = EventDetectedByIntegrator( t, VAR, nIndexOfEvents(1) );
   end
end
end


%================================================
end    % End of function MGBaseballTrajectoryFma
%================================================
