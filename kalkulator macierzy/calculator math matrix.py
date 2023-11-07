import numpy as np

def load_matrix():
    try:
        rows = int(input("Enter the number of matrix rows: "))
        columns = int(input("Enter the number of matrix columns: "))
        print("Enter matrix elements (separated by spaces or line breaks):")
        matrix = []
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != columns:
                print("Error: The number of elements in a row does not match the number of columns.")
                return None
            matrix.append(row)
        return np.array(matrix)
    except ValueError:
        print("Error: Invalid input.")
        return None

def calculate_determinant(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        return np.linalg.det(matrix)
    else:
        print("Error: Determinant can only be calculated for a square matrix.")
        return None

def matrix_addition(matrix_a, matrix_b):
    if matrix_a.shape == matrix_b.shape:
        return matrix_a + matrix_b
    else:
        print("Error: Matrices must have the same dimensions.")
        return None

def matrix_subtraction(matrix_a, matrix_b):
    if matrix_a.shape == matrix_b.shape:
        return matrix_a - matrix_b
    else:
        print("Error: Matrices must have the same dimensions.")
        return None

def matrix_multiplication(matrix_a, matrix_b):
    if matrix_a.shape[1] == matrix_b.shape[0]:
        return np.dot(matrix_a, matrix_b)
    else:
        print("Error: The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

def display_matrix(matrix):
    if matrix is not None:
        print(matrix)

if __name__ == "__main__":
    while True:
        print("Matrix Calculator")

        matrix_a = load_matrix()

        if matrix_a is not None:
            while True:
                print("Choose an operation:")
                print("1. Matrix Addition")
                print("2. Matrix Subtraction")
                print("3. Matrix Multiplication")
                print("4. Calculate Matrix Determinant")
                print("5. Exit")

                choice = input("Your choice: ")

                if choice == "1":
                    matrix_b = load_matrix()
                    if matrix_b is not None:
                        sum_matrix = matrix_addition(matrix_a, matrix_b)
                        if sum_matrix is not None:
                            print("Sum of matrices:")
                            display_matrix(sum_matrix)
                elif choice == "2":
                    matrix_b = load_matrix()
                    if matrix_b is not None:
                        diff_matrix = matrix_subtraction(matrix_a, matrix_b)
                        if diff_matrix is not None:
                            print("Difference of matrices:")
                            display_matrix(diff_matrix)
                elif choice == "3":
                    matrix_b = load_matrix()
                    if matrix_b is not None:
                        product_matrix = matrix_multiplication(matrix_a, matrix_b)
                        if product_matrix is not None:
                            print("Matrix product:")
                            display_matrix(product_matrix)
                elif choice == "4":
                    determinant = calculate_determinant(matrix_a)
                    if determinant is not None:
                        print("Matrix determinant:")
                        print(determinant)
                elif choice == "5":
                    break
                else:
                    print("Error: Invalid operation choice.")

            continue_option = input("Do you want to continue (yes/no)? ").lower()
            if continue_option != "yes":
                break
