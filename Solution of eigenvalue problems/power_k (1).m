
A = [2, -1; 2, 5];
k=2;
disp(power_k(A,k))
[eigenvalue, eigenvector] = power_k(A, k);

function [eigenvalue, eigenvector] = power_k(A, k)

n=length(A);
eigenvalue = zeros(k,1);
eigenvector = zeros(n,k);

for i = 1:k
x = rand(n,1); % initialize starting vector with random values
x = x/norm(x); % normalize starting vector
prev_eigenvalue = 0;
while true
y = A*x; % multiply matrix A by starting vector
eigenvalue(i) = x'*y; % compute eigenvalue as dot product of starting vector and result of Ax
x = y/norm(y); % normalize result of Ax and set as new starting vector
if abs(prev_eigenvalue - eigenvalue(i)) < 1e-6 % stop when eigenvalue has converged
break;
end
prev_eigenvalue = eigenvalue(i);
end
eigenvector(:,i) = x; % set corresponding eigenvector
A = A - eigenvalue(i)*(x*x');
end 
end

