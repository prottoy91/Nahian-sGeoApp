Pro=bluetoothRangeConfig;
Par=bluetoothRangeConfig;
Pat=bluetoothRangeConfig;
Pro.Environment='Home';
Pro.SignalPowerType = "ReceivedSignalPower";
Pro.TransmitterPower=-20;
Par.Environment='Home';
Par.SignalPowerType = "ReceivedSignalPower";
Par.TransmitterPower=-20;
Pat.Environment='Home';
Pat.SignalPowerType = "ReceivedSignalPower";
Pat.TransmitterPower=-20;
server = 'ws://***************.in.ngrok.io/ws/socket-server/';
client = SimpleClient(server);
Rot=[cosd(113) -sind(113); sind(113) cosd(113)];
measureNoise = diag([3 3]);
KF=trackingKF;
KF.MeasurementNoise=measureNoise;
KF.ProcessNoise=diag([20 20]);
KF.State=[1;0;3;0];
KF.MeasurementModel=[1 1 0 0;0 0 1 1];
%KF.ProcessNoise=diag([0;1;0;1]);
txPosition = [0 3.64 3.64;0 0 3.17];  
localizationMethod = "lateration";

while(1)
    measured=get(0,'userdata');
    measured=jsondecode(measured);
    if (measured.rss(1)<0)
        measured=measured.rss;
        fprintf("\nRSSIs [%d  %d  %d] received!",measured(1),measured(2),measured(3));
        Pro.ReceivedSignalPower=measured(1);
        Par.ReceivedSignalPower=measured(2);
        Pat.ReceivedSignalPower=measured(3);
        pro_dist=bluetoothRange(Pro);  
        par_dist=bluetoothRange(Par);
        pat_dist=bluetoothRange(Pat);
        %Pro_dist_values = min(pro_dist):max(pro_dist);
        Pro_distanceEst = min(pro_dist);
        Par_distanceEst = min(par_dist);
        Pat_distanceEst = min(pat_dist);
        %idx1 = randi(length(Pro_dist_values),1);
        %Pro_distanceEst = Pro_dist_values(idx1);
        %Par_dist_values = min(par_dist):max(par_dist);
        %idx2 = randi(length(Par_dist_values),1);
        %Par_distanceEst = Par_dist_values(idx2);
        %Pat_dist_values = min(pat_dist):max(pat_dist);
        %idx3 = randi(length(Pat_dist_values),1);
        %Pat_distanceEst = Pat_dist_values(idx3);
        distance=[Pro_distanceEst Par_distanceEst Pat_distanceEst];
        Position = blePositionEstimate(txPosition,localizationMethod,distance);
        Kfiltered_Pos_4D=correct(KF,Position);
        Kfiltered_Pos=[Kfiltered_Pos_4D(1,1)+(0.5*Kfiltered_Pos_4D(2,1));Kfiltered_Pos_4D(3,1)+(0.5*Kfiltered_Pos_4D(4,1))];
        POS=Kfiltered_Pos;
        scatter(POS(1),POS(2));
        %POS=POS*-1;
        POS=Rot*POS;
        %POS=[POS(1)+3.64 POS(2)];
        %POS=[-POS(1) POS(2)]
        POS=[(10060058.13+POS(1)) (2724494.55+POS(2))];
        pos=struct("rss",POS);
        pos=jsonencode(pos);
        client.send(pos);
        %format long g
        %fprintf("\nPosition [%d  %d] sent!",POS(1),POS(2));
    end
    pause(0.1);
end
    
    
    

