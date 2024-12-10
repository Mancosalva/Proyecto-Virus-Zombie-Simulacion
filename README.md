# Modelo de propagación de enfermedad

![1000025817](https://github.com/user-attachments/assets/ffd6ec7b-8ca4-4253-916f-2c14003b7e74) 


## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Características](#características)
3. [Instalación](#instalación)

## Descripción

Este proyecto se basa en la simulacion de una enfermadad zombie, siendo este un automata celular basado el juego de la vida de John Horton Conway de 1970

## Características

- Por cada infectado que una persona sana tenga como vecino tiene un probabilidad de ser infectado por ejemplo por cada vecino hay un 25% de probabilidad de ser infectado esto quiere decir que con 4 infectados vecinos la infección es asegurada 
- Por cada persona sana que un infectado tenga como vecino tiene un probabilidad de ser asesinado por ejemplo por cada vecino hay un 20% de probabilidad de ser asesinado si se es infectado esto quiere decir que con 5 vecinos sanos la muerte es asegurada es asegurada 
- Si despues de cierta cantidad de iteraciones una persona infectada no es asesinada estas se convertirs en una persona inmune la cual comparte las propiedades de los vecinos sanos y además no puede volver a ser infectada

## Instalación

### Requisitos previos

Antes de instalar este proyecto, asegúrate de tener instalados:

- import tkinter as tk
- import numpy as np

### Instrucciones de instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Mancosalva/Proyecto-Virus-Zombie-Simulacion.git
