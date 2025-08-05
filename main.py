from machine import Pin
from utime import sleep


print("Hello World!")

ledAmarelo = Pin(15, Pin.OUT)
ledVerde = Pin(16, Pin.OUT)
ledVermelho = Pin(17, Pin.OUT)

while True:
  ledVerde.on()
  print("Led ON!")
  sleep(20)
  ledVerde.off()
  print("Led OFF!")
  sleep(0.5)

  ledAmarelo.on()
  print("Led ON!")
  sleep(10)
  ledAmarelo.off()
  print("Led OFF!")
  sleep(0.5)

  ledVermelho.on()
  print("Led ON!")
  sleep(10)
  ledVermelho.off()
  print("Led OFF!")
  sleep(0.5)



