# Observaciones

1. script.py implementa un algoritmo de _encriptación simétrica_, porque la llave que
usa para encriptar es secreta.

2. El algoritmo se basa en el _Problema del Algoritmo Discreto_. El _grupo_ es el de los
_residuos != 0 módulo primo_, en otras palabras el de las unidades del _anillo_ de los
residuos módulo primo.

Ejemplo (12, no primo):
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 (residuos)
1, 5, 7, 11 (unidades, o sea los primos relativos a 12)

3. Teorema Chino del Residuo: el anillo de residuos se puede factorizar tal como se
factoriza su módulo. Problema de la Factorización en Primos.

Ejemplo:
       4   3
0 ->   0,  0
1 ->   1,  1
2 ->   2,  2
3 ->   3,  0
4 ->   0,  1
5 ->   1,  2
6 ->   2,  0
7 ->   3,  1
8 ->   0,  2
9 ->   1,  0
10->   2,  1
11->   3,  2

  Problemas de O(nm) a O(n+m)
  - 5x + 1 = 0
  - raiz_cubica(7)
  - ord(5)
  - totient(12)

4. Datos que permitirían decifrar el mensaje:
  - k, porque estando dentro del grupo, se puede calcular c / k.
  - key, o sea log_A k, que es inviable calcular.

5. B podría ayudar a encontrar k, por ejemplo si encontráramos e = log_g A.
   Si A^e = g entonces k = A^d = g^(e x d) = B^e.

6. Los exponentes forman anillos. Los módulos son los órdenes de las bases.

  "Adición cifrada"
  - Las potencias de un elemento del grupo forman un subgrupo.
    Ejemplos:
    mod 7:  5, 4 (=25), 6 (=20), 2 (=30), 3 (=10), 1 (=15)
    mod 7:  3, 2, 1
    mod 11: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1
  - Primos seguros
  - Las unidades son los elementos, que en el grupo aditivo, su orden es el orden
    del grupo.
  - El orden de los subgrupos divide al orden del grupo por el Teorema de Lagrange
    Ejemplos:
    mod 7: ord(5) = 6; ord(3) = 3; ord(6) = 2
  - ord(3 x 6) = lcm(ord(3), ord(6))
  - La función de Carmichael

  "Multiplicación cifrada"
  - mod 11:           2, 8, 6, 7
    exponente mod 10: 1, 3, 9, 7
  - Solucionando b^x = a (mod m), si a tiene orden j y b tiene orden k.
    Si hay solución entonces el subgrupo generado por a está dentro del
    subgrupo generado por b. Por lo tanto j divide a k.
    b^xj = 1 por lo tanto k divide a xj. Luego k/j divide a x.
    Hay totient(j) posibles valores para x.
  - Si a = g^s y b = g^t, resolver b^x = a (mod m) sólo requiere resolver
    tx = s (mod carmichael(m)).


# Procedimiento

1. Es p primo (test de primalidad Miller-Rabin)? Sí.

2. Es p un primo seguro? Sí. Digamos que p = 2q + 1.
   Alternativamente: factorizar totient(p).

3. Posibles órdenes son: 1, 2, q, 2q.

4. Encontrar cuál es el orden de B. Es 2.

5. Muy posiblemente key == q. Asumámoslo.

6. Calculemos k. Luego c / k.
   Atajo: k^2 = 1 y p es primo, por lo tanto k es 1 o -1.

# Aplicaciones (criptografía asimétrica)

1. Diffie-Hellman Key Exchange
2. RSA
3. ECDH
4. ECDSA
5. Criptosistema Homomórfico de Paillier

# Enlaces Recomendados

1. http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html
