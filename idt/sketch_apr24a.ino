int trigger=5;   //Variables donde conectamos los pines T y E 
int echo=6;  
int tiempo;     // Es para depositar el valor convertido del tiempo que se tarda en volver 
float distancia;   //  Depositamos la señal convertida en centímetros
int buzz =8;    // Variable donde conectamos el buzzer
void setup() {
  Serial.begin (9600);
  pinMode (trigger, OUTPUT);
  pinMode (echo, INPUT);

}
void loop() {
  digitalWrite (trigger, LOW);  //standby o colocado
  delayMicroseconds (10);  //Estabiliza el sensor y genera la señal
  digitalWrite (trigger, HIGH);
  delayMicroseconds (10);  //Genera pulso por 10 micro segundos
  digitalWrite (trigger, LOW);
  delayMicroseconds (10); //Desactivamos la señal para evitar interferencias
  //Obtenemos datos y realizamos la conversión a cm
  tiempo= pulseIn (echo, HIGH); // Calcula el tiempo que vuelve de T a E
  distancia= tiempo/58;    //  Ahora, convertimos el tiempo en centimentros
  Serial.print ("Distancia = ");
  Serial.print (distancia);
  Serial.println ("cm");
  delay (300);

   if(distancia>=200 && distancia<=300){
    digitalWrite(buzz, HIGH); 
  } 
  else{
      digitalWrite(buzz, LOW);
  }
}
