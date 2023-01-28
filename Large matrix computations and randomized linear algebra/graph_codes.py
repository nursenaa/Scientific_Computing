import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
from scipy.sparse.linalg import svds
from PIL import Image
import time
A = np.array([[1, 2], [3, 4]])
k = 1
def randomized_svd(A, k):
    p=5;
    m, n = A.shape
    Q = np.random.randn(m, k+p)
    Q, _ = np.linalg.qr(Q)
    B = np.dot(Q.T, A)
    U, Sigma, V = np.linalg.svd(B, full_matrices=False)
    return np.dot(Q, U), Sigma, V


U, S, V = randomized_svd(A, k)
print("U:", U)
print("S:", S)
print("V:", V)


def get_image_matrix(file_name):
    image = Image.open(file_name)
    image = image.convert("L")
    return np.array(image)

def get_relative_error(A, uk, sigma_k, vk):
    sigma_k_matrix = np.diagflat(sigma_k)
    svd_matrix = np.dot(np.dot(uk, sigma_k_matrix), vk.T)
    return np.linalg.norm(svd_matrix - A) / np.linalg.norm(A)

A_cameraman = get_image_matrix("C:/Users/nur20/Downloads/cameraman.jpg")
A_fingerprint = get_image_matrix("C:/Users/nur20/Downloads/fingerprint.jpg")
k=min(A_cameraman.shape)
U, Sigma, V = svd(A_cameraman)
uk_cameraman, sigma_k_cameraman, vk_cameraman = randomized_svd(A_cameraman, k=20)
u_prime_k_cameraman, sigma_prime_k_cameraman, v_prime_k_cameraman = np.linalg.svd(A_cameraman, full_matrices=False)

reconstruction_1 = np.dot(np.dot(uk_cameraman[:, :k], np.diag(sigma_k_cameraman)), vk_cameraman[:k, :])
reconstruction_2 = np.dot(np.dot(u_prime_k_cameraman[:, :k], np.diag(sigma_prime_k_cameraman[:k])), v_prime_k_cameraman[:k, :])
reconstruction_3 = np.dot(np.dot(U[:, :k], np.diag(Sigma[:k])), V[:k, :])
k_values1 = range(1, min(A_cameraman.shape))
k_values2 = 255

rel_err_rand_cameraman = []
rel_err_svds_cameraman = []
run_times_image1 = []
run_times_image2 = []
run_times_image1_svds=[]
run_times_image2_svds=[]
plt.figure(figsize=(15,15))
plt.subplot(1, 4, 1)
plt.imshow(A_cameraman, cmap="gray")
plt.title("Original Image")
plt.subplot(1, 4, 2)
plt.imshow(reconstruction_1, cmap="gray")
plt.title("Randomized SVD")
plt.subplot(1, 4, 3)
plt.imshow(reconstruction_2, cmap="gray")
plt.title("SVD (full_matrices = False)")
plt.subplot(1, 4, 4)
plt.imshow(reconstruction_3, cmap="gray")
plt.title("SVD (full_matrices = True)")
plt.show()

for k in range(1, min(A_cameraman.shape)):
    start_time = time.time()
    uk_cameraman, sigma_k_cameraman, vk_cameraman = randomized_svd(A_cameraman, k=A_cameraman.shape[1])
    end_time = time.time()
    run_times_image1.append(end_time - start_time)
    start_time = time.time()
    u_prime_k_cameraman, sigma_prime_k_cameraman, v_prime_k_cameraman = np.linalg.svd(A_cameraman, full_matrices=False)
    end_time = time.time()
    run_times_image1_svds.append(end_time - start_time)
    rel_err_rand_cameraman.append(get_relative_error(A_cameraman, uk_cameraman, sigma_k_cameraman, vk_cameraman.T))
    rel_err_svds_cameraman.append(get_relative_error(A_cameraman, u_prime_k_cameraman, sigma_prime_k_cameraman, v_prime_k_cameraman.T))

plt.plot(range(1, min(A_cameraman.shape)), rel_err_rand_cameraman, label="Randomized SVD")
plt.plot(range(1, min(A_cameraman.shape)), rel_err_svds_cameraman, label="svds")
plt.xlabel("k")
plt.ylabel("Relative error")
plt.title("cameraman.jpg")
plt.legend()
plt.show()
plt.plot(k_values1, run_times_image1, label=A_cameraman)
plt.plot(k_values1, run_times_image1_svds, label=A_cameraman)
plt.xlabel("k")
plt.ylabel("Run time (seconds)")
plt.title("camera Run times of approximate_svd (svds) vs k")
plt.legend()
plt.show()

rel_err_rand_fingerprint = []
rel_err_svd_fingerprint = []

m, n = A_fingerprint.shape
k = 255
U, Sigma, V = svd(A_fingerprint)
uk_fingerprint, sigma_k_fingerprint, vk_fingerprint = randomized_svd(A_fingerprint, 20)
u_prime_k_fingerprint, sigma_prime_k_fingerprint, v_prime_k_fingerprint = np.linalg.svd(A_fingerprint,full_matrices=False)
reconstruction_1 = np.dot(np.dot(uk_fingerprint[:, :k], np.diag(sigma_k_fingerprint)), vk_fingerprint[:k, :])
reconstruction_2 = np.dot(np.dot(u_prime_k_fingerprint[:, :k], np.diag(sigma_prime_k_fingerprint[:k])), v_prime_k_fingerprint[:k, :])
reconstruction_3 = np.dot(np.dot(U[:, :k], np.diag(Sigma[:k])), V[:k, :])
plt.figure(figsize=(15,15))
plt.subplot(1, 4, 1)
plt.imshow(A_fingerprint, cmap="gray")
plt.title("Original Image")
plt.subplot(1, 4, 2)
plt.imshow(reconstruction_1, cmap="gray")
plt.title("Randomized SVD")
plt.subplot(1, 4, 3)
plt.imshow(reconstruction_2, cmap="gray")
plt.title("SVD (full_matrices = False)")
plt.subplot(1, 4, 4)
plt.imshow(reconstruction_3, cmap="gray")
plt.title("SVD (full_matrices = True)")
plt.show()
for k in range(1, 255):
    start_time = time.time()
    uk_fingerprint, sigma_k_fingerprint, vk_fingerprint = randomized_svd(A_fingerprint, k)
    end_time = time.time()
    run_times_image2.append(end_time - start_time)
    start_time = time.time()
    u_prime_k_fingerprint, sigma_prime_k_fingerprint, v_prime_k_fingerprint = np.linalg.svd(A_fingerprint,full_matrices=False)
    end_time = time.time()
    run_times_image2_svds.append(end_time - start_time)
    rel_err_rand_fingerprint.append(get_relative_error(A_fingerprint, uk_fingerprint, sigma_k_fingerprint, vk_fingerprint.T))
    rel_err_svd_fingerprint.append(get_relative_error(A_fingerprint, u_prime_k_fingerprint, sigma_prime_k_fingerprint, v_prime_k_fingerprint.T))

plt.plot(range(1, k+1), rel_err_rand_fingerprint, label="Randomized SVD")
plt.plot(range(1, k+1), rel_err_svd_fingerprint, label="svd")
plt.xlabel("k")

plt.ylabel("Relative error")
plt.title("fingerprint.jpg")
plt.legend()
plt.show()
plt.plot(range(1, k+1), run_times_image2, label=A_fingerprint)
plt.plot(range(1, k+1), run_times_image2_svds, label=A_fingerprint)
plt.xlabel("k")
plt.ylabel("Run time (seconds)")
plt.title("fingerprint-Run times of approximate_svd (svds) vs k")
plt.legend()
plt.show()