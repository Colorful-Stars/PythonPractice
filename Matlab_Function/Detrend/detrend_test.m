clc;clear all;
close all;

RawData_int = load('002217-rawdata.txt');
[h,w] =size(RawData_int);

RawLED_G=RawData_int(2:end,1)-RawData_int(1,1);
% RawX = RawData_int(:,5);
% RawY = RawData_int(:,6);
% RawZ = RawData_int(:,7);
Acc_raw = RawData_int(:,5:7);

Fs = 100;
Win_sample = 512;

Loop = (length(RawLED_G)/Fs) - floor(Win_sample/Fs) - 1;
for ii=1:Loop
    LED_G_win=RawLED_G((ii-1)*Fs+1:(ii-1)*Fs+Win_sample);
    
%     X_Acc_win=RawX((ii-1)*Fs+1:(ii-1)*Fs+Win_sample);
%     Y_Acc_win=RawY((ii-1)*Fs+1:(ii-1)*Fs+Win_sample);
%     Z_Acc_win=RawZ((ii-1)*Fs+1:(ii-1)*Fs+Win_sample);
    
    Acc_win = Acc_raw((ii-1)*Fs+1:(ii-1)*Fs+Win_sample,:);
    
%     SSTD = sqrt(var(X_Acc_win) + var(Y_Acc_win) + var(Z_Acc_win));
    SSTD=sum(std(Acc_win));
    
    disp(['三轴 512长度下的各自标准差和:',num2str(SSTD)]);
    if SSTD > 100
        disp('此时非静态！')
    end
    if SSTD <= 100
        disp('静态====>');
        figure
        plot(LED_G_win,'g');
%         LED_G_tmp=IIRfilter(RawLED_G)';
        detrend_G = detrend(LED_G_win);
        trend_G = LED_G_win - detrend_G;
        hold on
        plot(trend_G,':r');
        plot(detrend_G,'b');
        plot(zeros(512),':k')
        legend('Original Data','Trend','Detrended Data',...
       'Mean of Detrended Data')
    end
    disp('============')
end

