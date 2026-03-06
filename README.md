# PLANTI2-plant-nanny
Micro:bit-based self-watering plant system with soil moisture sensing, pump control, and optional air humidifier. Recreated in Tinkercad from a 2022 STEM Fair project.

![Logo](images/planti2-logo.png)

## Project Background

This project was originally developed for a **STEM Fair in 2022** by a group of students.  
The goal was to design a simple system that could automatically water plants using sensors and a microcontroller.

![Board](images/display-board)

In 2026, the project was **recreated and expanded in simulation using Tinkercad** in order to document the system and improve its control logic.

# Overview

The Smart Plant Nanny is an **automatic plant watering system** that monitors soil moisture and waters plants when the soil becomes too dry.

The system uses a **BBC micro:bit microcontroller** to read sensor data and control a small water pump that delivers water to the plant through a tube.

An optional humidifier can also be activated to provide moisture to the surrounding air.

# Original Hardware Prototype (2022)

The physical prototype was built using a **two-layer structure**:

### Layer 1 – Electronics Platform
This layer supported the main electronic components and wiring, including:
- BBC micro:bit
- Breadboard
- Transistor motor driver
- Battery holder
- Wiring and crocodile clips

### Layer 2 – Plant and Water System
This layer contained the plant system and watering components:
- Soil moisture sensor
- Water reservoir
- Submersible water pump
- Silicone tube
- 5V USB humidifier

The soil moisture sensor detects dryness in the soil.  
When the soil becomes dry, the micro:bit activates the pump, which pulls water from the reservoir through a tube and waters the plant.

The humidifier can be manually turned on or off by the user to increase air humidity around the plant.

# Materials Used

- BBC micro:bit
- Breadboard
- Soil moisture sensor
- Submersible water pump
- Battery holder
- 5V USB air humidifier
- Transistor (motor driver)
- Silicone tube
- Crocodile clip wires

# 2026 Improvements (Simulation Version)

The original STEM fair project focused mainly on **basic automatic watering**.

When recreating the system in **Tinkercad**, several additional features were implemented to improve the design and make it closer to real smart irrigation systems.

### Added Improvements

• Soil moisture value display on the micro:bit  
• Pump activation animation on the LED display  
• Moisture hysteresis to prevent rapid ON/OFF switching  
• Night mode using the micro:bit light sensor  
• Water tank level protection logic  
• Pump delay to reduce unnecessary switching  

These improvements make the system **more stable, safer, and more realistic for real-world applications**.

# Simulation

The circuit was recreated using:

Tinkercad Circuits

This simulation models the behavior of the original system and demonstrates the control logic used for automatic watering.

Simulation link:
https://www.tinkercad.com/things/7Y3o52LFwUy-planti2-tinkercad-version

# How the System Works

1. The soil moisture sensor measures how wet or dry the soil is.
2. The micro:bit reads the sensor value.
3. If the soil is below a defined dryness threshold, the system activates the pump.
4. The pump moves water from the reservoir through a silicone tube to the plant.
5. Once the soil becomes sufficiently moist, the pump stops.
6. A humidifier can also be toggled manually by the user.

Additional safety logic prevents the pump from running when:
- The water tank is empty
- It is nighttime

# Code

The control logic was implemented using **MicroPython for the BBC micro:bit**.

See:
`microbit_code.py`

# Applications

Systems like this are used in:

- Smart home gardening
- Automated plant care
- Greenhouse irrigation systems
- Agricultural water management


Special Thanks to my Original Team Members :smile: :

- Brielle Chua
- Jaff Caspe
- Jamile Fernandez
- Jasper Villanueva
- Nikko Dela Cruz
- Rain Balansag
- Sean Estrella
- Vinn Milliam
- Izza Nazario
