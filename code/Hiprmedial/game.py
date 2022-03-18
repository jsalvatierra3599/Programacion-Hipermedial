#
using UnityEngine;
using System.Collections;
using System;
 
// Tipos enumerados para definir las direcciones
public enum DireccionH { Izquierda, Derecha }
public enum DireccionV { Arriba, Abajo }
 
public class MovimientoPlataforma : MonoBehaviour
{
    // Es la velocidad a la que se moverá la plataforma en el eje horizontal.
    public float VelocidadH = 0.3F;
 
    // Indica el sentido horizontal al que comenzará a moverse la plataforma.
    public DireccionH SentidoH = DireccionH.Derecha;
 
    // Es la velocidad a la que se moverá la plataforma en el eje vertical.
    public float VelocidadV = 0.0F;
 
    // Indica el sentido vertical al que comenzará a moverse la plataforma.
    public DireccionV SentidoV = DireccionV.Arriba;
 
    // Es el la distancia que recorrerá la plataforma en modo ping-pong.
    // Para desactivar el modo ping-pong, establecer esta variable a -1.
    public float MaxRecorridoPingPong = 5.0F;
 
    // Variables privadas
    private Transform PlatformTransform;
    private float WalkedDistanceH = 0.0F;
    private float WalkedDistanceV = 0.0F;
    private float ReferencePingPongHPosition;
    private float ReferencePingPongVPosition;
    private Vector3 InitialPlatformPosition;
}
Creamos la función Start() e inicializamos algunas variables:

1
2
3
4
5
6
7
8
9
10
11
12
13
void Start ()
{

 
    // Inicializamos la posición de referencia para el cálculo de rebote vertical (ping-pong)
    ReferencePingPongVPosition = PlatformTransform.position.y;
}