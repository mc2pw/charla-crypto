# Observaciones

1. salsa20.py implementa el algoritmo Salsa20 de encriptación simétrica.

2. Salsa20 encripta generando bloques de 512 bits (64 bytes). Esto es el keystream.

3. Para hacer un bloque del keystream, primero se hace un bloque con:
   la llave (256 bits), el nonce (64 bits), la posición del bloque (64 bits).
   Luego se "expande" con s20_expand32.

3. El paso final de la encriptación hace XOR del keystream con el plaintext.

4. XOR es la suma en el anillo de residuos modulo 2. El plaintext y el keystream
   son vectores cuyos escalares provienen de este anillo.
   Propiedad: Si c = p XOR k, entonces p = c XOR k.

# Procedimiento

1. Nótese el error de implementación. _si_ debería ser la posición en bytes dentro
   del stream encriptado. En vez de esto, _si_ es la posición del bloque del stream.

   - Vulnerabilidad de seguridad: Bloques reutilizados permiten permiten CPA
    (Chosen Plaintext Attack).

2. El primer bloque del keystream es el mismo que el segundo. Utilizar esto
   para decifrar el primer bloque de cifertexto.

   - Elegimos un plaintext que nos permita recibir el segundo bloque del keystream.
     El plaintext es 96 x '\x00'. Debe ser lo suficientemente largo como para darnos
     todos los bytes del bloque del keystream que necesitamos.
   - Hay que tomar en cuenta la base64 y ajustar el número de bytes mandados de
     acuerdo a esto.

3. Recibimos 150 bytes, que son suficientes para decifrar los 142 bytes que primero
   recibimos. Aplicamos el paso de base64, y json para obtener el plaintext final.

4. Aplicamos XOR tomando en cuenta que en el paso de XOR de Salsa20 hay un offset
   de 1 byte cuando se aplica el bloque del keystream.

# Enlaces recomendados

AES
http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html


