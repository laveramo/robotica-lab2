%%
%rosinit; %Conexión con nodo maestro, correr solo 1 una vez
%%
jstatesPub = rospublisher('/dynamixel_workbench/joint_states','sensor_msgs/JointState'); %Creación publicador
jstatesMsg = rosmessage(jstatesPub); %Creación de mensaje
%%
jstatesMsg.Name = "waist"; %Valor del mensaje
send(jstatesPub,jstatesMsg); %Envio
pause(1)