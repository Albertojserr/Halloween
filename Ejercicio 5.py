'''La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas las comunicaciones,
por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes,
que contemple los siguientes requerimientos:


        1.cada carácter deberá ser encriptado a ocho caracteres;

        2.se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}”
        es decir desde el 32 al 125 de la tabla ASCII.'''

import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
h = hashlib.new('sha256')
h.update(b"Nobody inspects the spammish repetition")
h.hexdigest()
print(m)
print(h)


m = hashlib.sha256()
m.update(b"El Libro De Python")
salida = m.hexdigest()

print(salida)
print(m.digest_size)

novo = hashlib.sha256()
novo.update(b"Secuencia 1")
novo.update(b"Secuencia 2")
novo.update(b"Secuencia 3")
novo.update(b"Secuencia 4")
salida = novo.hexdigest()

print(salida)



print(hashlib.sha256(b"El Libro de Python").hexdigest())
print(hashlib.sha224(b"El Libro de Python").hexdigest())
print(hashlib.sha512(b"El Libro de Python").hexdigest())
print(hashlib.blake2b(b"El Libro de Python").hexdigest())
print(hashlib.blake2s(b"El Libro de Python").hexdigest())
print(hashlib.blake2s(b"El Libro de Python").hexdigest())
print(hashlib.md5(b"El Libro de Python").hexdigest())