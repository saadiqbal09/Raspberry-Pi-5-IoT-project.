# Raspberry Pi 5 - 21 Component IoT Interface Project

This project focuses on interfacing a diverse set of **21 sensors and actuators** with a **Raspberry Pi 5**. The system utilizes various communication protocols (Digital I/O, PWM, SPI, 1-Wire) and implements **MQTT** for publishing telemetry data from key sensors to a **ThingsBoard** instance for centralized monitoring and control.

## 🚀 Project Goals

1.  **Comprehensive Interface:** Successfully connect and manage all 21 components on a single Raspberry Pi 5, utilizing all available interface types.
2.  **Efficient Cloud Logging:** Consolidate data from all sensing elements and periodically publish optimized JSON telemetry payloads to ThingsBoard.
3.  **Local Control:** Implement local control logic for actuators (Motors, Relay, Buzzer) driven by sensor inputs and/or control signals from the cloud.

---

## ⚙️ Component List (21 Total)

The project involves the following components, categorized by their primary function and interface requirement.

### 1. Analog Sensors (Requires ADC via SPI)

The Raspberry Pi requires an external **Analog-to-Digital Converter (ADC)**, such as the MCP3208, communicating over SPI to read these sensors.

| Component | Sensor Type | Measurement |
| :--- | :--- | :--- |
| **LDR** | Light Dependent Resistor | Ambient Light Level |
| **LM35** | Temperature Sensor | Analog Temperature Output |
| **MQ-6** | Gas Sensor | LPG, Propane, Smoke Concentration |
| **MQ-7** | Gas Sensor | Carbon Monoxide (CO) Concentration |
| **MQ-135** | Gas Sensor | Air Quality (CO2, Ammonia, Benzene) |
| **TEMT6000**| Light Sensor | Ambient Light Intensity |

### 2. Digital Sensors & Inputs (Dedicated GPIO)

These components output a simple HIGH/LOW state or act as user inputs. The **DHT11** uses the 1-Wire protocol, but only requires one data pin.

| Component | Type | Interface |
| :--- | :--- | :--- |
| **DHT11** | Temperature/Humidity | 1-Wire Protocol |
| **Hall Effect** | Magnetic Field Detection | Digital Input |
| **IR Sensor** | Obstacle Detection | Digital Input |
| **Rain Sensor** | Rain/Water Presence | Digital Input |
| **Resistive Touch** | Touch Event Detection | Digital Input |
| **Tilt Switch** | Orientation Detection | Digital Input |
| **Joystick** | User Input (5 Directions) | 5 Digital Inputs |
| **LED Switch (SW)** | Button Input | Digital Input |

### 3. Actuators & Outputs (GPIO & PWM)

These components are controlled by the Raspberry Pi to perform physical actions or display information.

| Component | Type | Interface |
| :--- | :--- | :--- |
| **DC Motor** | Motion Control | Digital + PWM (via Motor Driver) |
| **Stepper Motor**| Precision Motion Control | 4 Digital Outputs (via Driver) |
| **Relay** | High Current Switching | Digital Output |
| **Buzzer** | Audible Alert | Digital Output |
| **LED Switch (LED)** | Indicator Light | Digital Output |
| **RGB LED** | Color Output | 3 PWM Outputs (R, G, B) |
| **LCD 16x2** | Text Display | 6 Digital Outputs (4-bit mode) |
| **Seven Segment**| Numeric Display | 8 Digital Outputs |

---

## 📌 Interfacing & Pinout

This project utilizes nearly all the available GPIO pins on the RPi 5. A careful, conflict-free pinout map is essential.

| Interface Type | Usage | Components Used |
| :--- | :--- | :--- |
| **SPI** | Communication with the external **ADC (e.g., MCP3208)** to read 6 analog sensors. | LDR, LM35, MQ-6, MQ-7, MQ-135, TEMT6000 |
| **PWM** | Control of speed/intensity. | DC Motor Speed, RGB LED (3 pins) |
| **Digital I/O** | All remaining sensors, inputs (Joystick), and outputs (Relay, Buzzer, LCD, Stepper). | 1-Wire, Digital Inputs, Motor Driver control, Display Pins |

### Pinout Alert ⚠️

**Note:** The initial uploaded scripts contained conflicting pin assignments (e.g., multiple devices on BCM 5). A unified script with a dedicated, unique GPIO pin for every connection point is required for the final project implementation.

---

## ☁️ ThingsBoard Integration

Telemetry data is published to a ThingsBoard server using the **paho-mqtt** client.

* **Host:** `demo.thingsboard.io`
* **Topic:** `v1/devices/me/telemetry`
* **Access Tokens:** Please replace the placeholder tokens in the provided scripts (`IF3MHO5mZBj6N7b6RPbZ` and `bdThfGxgIYh7TmSuLrM8`) with your final, verified ThingsBoard device tokens.

Data from sensors like DHT11, LM35, MQ-135, LDR, IR, and Hall Effect should be consolidated into a single JSON payload to maximize data throughput and minimize network overhead.

## 📦 Required Libraries

To run the Python scripts on your Raspberry Pi 5, install the following dependencies:

```bash
# Core RPi GPIO access
pip3 install RPi.GPIO

# DHT Sensor library
pip3 install Adafruit_DHT

# MQTT client library for ThingsBoard communication
pip3 install paho-mqtt

# SPI library for ADC communication
pip3 install spidev
