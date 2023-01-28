A = [10 -7 0
     -3  2 6
      5 -1 5];
%[L,U,P] = lu(A);
%disp(U);
tic;
 [L,U] = picketts(A)
 toc;

 
 function [L,U] = picketts(A)
       
    k=length(A);
    [L,U] = helper(A, k);
end
function [M,S] = helper(A, k)
  
    if k==1
        M=1;
         
        S=A(1,1);
    else
    
    [M1,S1] = helper(A, k-1);
  
    u1k = M1\A(1:k-1,k);%bu row 1 den k ya kadar ama column k-1 yani k-1.column
    disp(size(M1));
    lk1 = A(k,1:k-1)/S1; 
    disp(size(lk1));
    lkk=1;
    
    ukk = (A(k,k)-lk1*u1k)\lkk;
    disp(ukk);
  
    M = [M1 zeros(k-1, 1); lk1 lkk]; %zeros= 1 k 
   
    S = [S1 u1k; zeros(1,k-1) ukk];
    
    end
end