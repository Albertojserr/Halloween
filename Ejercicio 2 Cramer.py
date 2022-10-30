import os

def sarrus(A):

    val = ((A[0][0]*A[1][1]*A[2][2])+\
        (A[0][1]*A[1][2]*A[2][0])+\
        (A[0][2]*A[1][0]*A[2][1]))-\
        ((A[2][0]*A[1][1]*A[0][2])+\
        (A[2][1]*A[1][2]*A[0][0])+\
        (A[2][2]*A[1][0]*A[0][1]))

    return val


def main():

    os.system("cls")

    sismat = [[0.0,0.0,0.0,0.0],\

                [0.0,0.0,0.0,0.0],\

                [0.0,0.0,0.0,0.0]]

    res = [0.0,0.0,0.0]

    print ("\n\tREGLA DE CRAMER\n\n\nA1x + B1y + C1z = D1")

    print ("A2x + B2y + C2z = D2\nA3x + B3y + C3z = D3\n\nIngresar valores:\n")

    sismat[0][0] = input("Ingrese A1 > ")

    sismat[0][1] = input("Ingrese B1 > ")

    sismat[0][2] = input("Ingrese C1 > ")

    sismat[0][3] = input("Ingrese D1 > ")

    sismat[1][0] = input("\nIngrese A2 > ")

    sismat[1][1] = input("Ingrese B2 > ")

    sismat[1][2] = input("Ingrese C2 > ")

    sismat[1][3] = input("Ingrese D2 > ")

    sismat[2][0] = input("\nIngrese A3 > ")

    sismat[2][1] = input("Ingrese B3 > ")

    sismat[2][2] = input("Ingrese C3 > ")

    sismat[2][3] = input("Ingrese D3 > ")

    mat_x = [[sismat[0][3],sismat[0][1],sismat[0][2]],\

            [sismat[1][3],sismat[1][1],sismat[1][2]],\

            [sismat[2][3],sismat[2][1],sismat[2][2]]]

    mat_y = [[sismat[0][0],sismat[0][3],sismat[0][2]],\

            [sismat[1][0],sismat[1][3],sismat[1][2]],\

            [sismat[2][0],sismat[2][3],sismat[2][2]]]

    mat_z = [[sismat[0][0],sismat[0][1],sismat[0][3]],\

            [sismat[1][0],sismat[1][1],sismat[1][3]],\

            [sismat[2][0],sismat[2][1],sismat[2][3]]]

    det_mat = sarrus(sismat)

    if (det_mat == 0):

        raw_input("Determinante de A nulo...")

    else:

        det_matx = sarrus(mat_x)

        det_maty = sarrus(mat_y)

        det_matz = sarrus(mat_z)

        res[0] = det_matx/det_mat

        res[1] = det_maty/det_mat

        res[2] = det_matz/det_mat

        print ("\nP => ",res)

        raw_input("\n\nRegla de Cramer terminado...")

