A = [2,-1;2,5];

[eigenvalue, eigenvector] = power_method(A);
disp(power_method(A))
disp(eigenvector)


function [eigenvalue, eigenvector] = power_method(A)
  % Initialize the eigenvector to a random vector
  eigenvector = rand(size(A, 1), 1);
  tolerance = 1e-5;
  % Iterate until convergence
  while true
    % Calculate the new eigenvector
    new_eigenvector = A * eigenvector;

    % Normalize the new eigenvector
    new_eigenvector = new_eigenvector / norm(new_eigenvector);

    % Calculate the change in eigenvector
    change = norm(new_eigenvector - eigenvector);

    % Check for convergence
    if change < tolerance
      break
    end

    % Update the eigenvector
    eigenvector = new_eigenvector;
  end

  % Calculate the dominant eigenvalue
  eigenvalue = norm(A * eigenvector) / norm(eigenvector);
end
