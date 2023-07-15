//HERC01G JOB CLASS=A,MSGCLASS=H,MSGLEVEL=(1,1),REGION=3M, 
//            USER=HERC01,PASSWORD=CUL8TR,TIME=1440        
//STEP001  EXEC PGM=IEBGENER                               
//SYSUT1 DD DSN=$PATH,        
//          UNIT=DISK,DISP=SHR                             
//SYSUT2 DD SYSOUT=*                                       
//SYSPRINT DD SYSOUT=*                                     
//SYSIN DD DUMMY
