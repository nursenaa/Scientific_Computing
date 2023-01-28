A = [2, -1; 2, 5];
k=2;
disp(subspace_iteration(A,k))
[largestEigVal, largestEigVec] = subspace_iteration(A, k)
disp(largestEigVal)
function [eig_vals, eig_vecs] = subspace_iteration(A, k)

% calculate size of matrix
[n,~] = size(A);

% initialize subspace with random matrix of size n x k
V = rand(n,k);

% perform subspace iterations to find k largest eigenvalues and eigenvectors
for i = 1:10
AV = A*V;
[Q,R] = qr(AV);
V = Q;
end

% calculate eigenvalues and eigenvectors
eig_vals = diag(R);
eig_vecs = V;

end