# PLANTI2-plant-nanny
Micro:bit-based self-watering plant system with soil moisture sensing, pump control, and optional air humidifier. Recreated in Tinkercad from a 2022 STEM Fair project.

Tinkercad link: https://www.tinkercad.com/things/7Y3o52LFwUy-planti2-tinkercad-version?sharecode=dlrpBMB_xjvE_FVYdWx__GbfSy_UxVwCkr0eF3obNak

![Logo](images/planti2-logo.png)

## Project Background

This project was originally developed for a **STEM Fair in 2022** by a group of students.  
The goal was to design a simple system that could automatically water plants using sensors and a microcontroller.

![Board](images/display-board.jpg)

In 2026, the project was **recreated and expanded in simulation using Tinkercad** in order to document the system and improve its control logic.

# Overview

PLANTI2 is an **automatic plant watering system** that monitors soil moisture and waters plants when the soil becomes too dry.

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

# Added Improvements (Simulation Version)

The original STEM fair project focused mainly on **basic automatic watering**.

When recreating the system in **Tinkercad**, several additional features were implemented to improve the design and make it closer to real smart irrigation systems.

- Soil moisture value display on the micro:bit  
- Pump activation animation on the LED display  
- Moisture hysteresis to prevent rapid ON/OFF switching  
- Night mode using the micro:bit light sensor  
- Water tank level protection logic  
- Pump delay to reduce unnecessary switching  

These improvements make the system **more stable, safer, and more realistic for real-world applications**.

# Simulation

The circuit was recreated using:

Tinkercad Circuits

This simulation models the behavior of the original system and demonstrates the control logic used for automatic watering.

Tinkercad link:
https://www.tinkercad.com/things/7Y3o52LFwUy-planti2-tinkercad-version?sharecode=dlrpBMB_xjvE_FVYdWx__GbfSy_UxVwCkr0eF3obNak

BBC Micro:bit

The Micro:bit serves as the controller of the system. It reads sensor inputs and decides when to activate the pump or other devices. In the original prototype, the Micro:bit was the central controller connected to the moisture sensor, pump driver, and humidifier.

Soil Moisture Sensor (Simulated)

The original project used a soil moisture sensor placed in the plant’s soil. In the Tinkercad simulation, this is represented by a potentiometer, which produces adjustable analog values to simulate different soil moisture levels.

Transistor Motor Driver

A transistor is used as a switch that allows the Micro:bit to control the pump. This mirrors the real prototype, where the transistor allowed the Micro:bit to safely power the pump using an external power source.

Water Pump (Simulated with DC Motor)

The real project used a submersible water pump to move water from a reservoir to the plant through a silicone tube. In the simulation, a DC motor represents the pump's electrical behavior.

LED Indicator

The LED in the simulation acts as a status indicator showing when certain outputs are active. This helps visualize system behavior during testing.

Breadboard and Wiring

The breadboard represents the wiring layout used in the physical prototype, where components were connected using crocodile clips and jumper wires.

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

(In `microbit_code.py`)

# Applications

Systems like this are used in:

- Smart home gardening
- Automated plant care
- Greenhouse irrigation systems
- Agricultural water management

## Concepts Demonstrated

- **Embedded Systems Programming**  
  Programming a BBC Micro:bit microcontroller using MicroPython.

- **Sensor Interfacing**  
  Reading analog data from a soil moisture sensor to determine soil dryness.

- **Automation Logic**  
  Automatically activating a water pump when soil moisture drops below a threshold.

- **Motor Control using Transistor Drivers**  
  Using a transistor as a switch to safely control a pump motor from a microcontroller pin.

- **Environmental Monitoring**  
  Measuring soil moisture and ambient light levels to adjust system behavior.

- **Control Logic with Hysteresis**  
  Preventing rapid pump switching by using separate dry and wet thresholds.

- **System Protection Logic**  
  Detecting low water levels to prevent the pump from running dry.

- **Human Interaction**  
  Allowing users to toggle the humidifier using the Micro:bit button.

- **Visual Feedback via Microcontroller Display**  
  Showing system status and animations on the Micro:bit LED matrix.

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
