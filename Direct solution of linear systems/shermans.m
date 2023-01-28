A = hilb(4);
%[L,U,P] = lu(A);
%disp(U);
tic;
 [L,U] = shermans(A)
 toc;

 
function [L,U] = shermans(A)
      
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
    lk1t = A(k,1:k-1)/S1; 
    disp(size(lk1t));
    ukk = A(k,k)-lk1t*u1k;
    disp(ukk);
    M = [M1 zeros(k-1, 1); lk1t 1]; %zeros= 1 k 
   
    S = [S1 u1k; zeros(1,k-1) ukk];
    
    end
end