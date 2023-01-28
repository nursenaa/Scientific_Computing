A = [2,-1;2,5];
shift=2;
v0=[1;1];
[lambda, v] = inverse_power(A, shift);
disp(inverse_power(A,shift))
disp(v)
function [lambda, v] = inverse_power(A, shift)


% Set tolerance and maximum number of iterations
tol = 1e-6;
max_iter = 1000;
shift=2;
v0=[1;1;];
% Initialize lambda and v
lambda = shift;
v = v0;

% Iterate until convergence or maximum number of iterations reached
for i = 1:max_iter
% Compute y = (A - shiftI)^(-1) * v
y = (A - shift*eye(size(A))) \ v;
% Normalize y
y = y / norm(y);

% Compute lambda = v' * A * y
lambda_new = y' * A * y;

% Check for convergence
if abs(lambda - lambda_new) < tol
    lambda = lambda_new;
    v = y;
    return;
end

% Update lambda and v
lambda = lambda_new;
v = y;
 
end

% Maximum number of iterations reached
warning('Shifted inverse power method did not converge');
end