%%
%rosinit; %Conexion con nodo maestro
%%
jstatesSub = rossubscriber('/dynamixel_workbench/join_states'); %Creación subscriptor
%%
jstatesMsg = jstatesSub.LatestMessage; %Recibe el último mensaje
jstatesMsg.Position
%jstatesMsg = receive(velSub); % Otra opción
