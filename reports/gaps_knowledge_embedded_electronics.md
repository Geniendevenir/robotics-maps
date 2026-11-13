# Coverage gaps: Embedded & electronics

Date: 2026-11-13. File reviewed: `output/knowledge_embedded_electronics.json` (verified version: 17 nodes, 29 robots/models/tools, 28 project candidates).
Branch: `research/knowledge-embedded-electronics`. No rows were added and Notion was not touched.

## How this was checked
- Compared against the electronics and embedded topics usually found in the Springer Handbook of Robotics (2nd ed., Part A: actuators and drives, sensing, robot computing and communication, safety), common mechatronics and embedded-systems course syllabi (e.g. Cornell ECE 4760, which the file already cites, plus typical university mechatronics labs), and the hardware a low-cost robot-learning lab (LeRobot/SO-101, legged/humanoid kits) actually uses.
- Ran keyword checks on the file for each candidate topic. "Missing" means there is no dedicated node or row. A passing mention inside another row does not count as coverage.
- These gaps come from comparing the file against those reference outlines and from domain knowledge. No new web sources were opened for this report, so the researcher must source every gap before adding a row.

## High importance
1. **Encoders & joint position sensing**: quadrature/magnetic absolute encoders (AS5047/AS5600 class), calibration, index/homing. No node exists, yet every FOC, servo and actuator project depends on it.
2. **Debugging & bring-up tools**: multimeter/oscilloscope/logic analyzer workflow, SWD/JTAG debug probes, serial-console bring-up. No node, and the oscilloscope gets only one mention. This is the biggest skill gap for software-first students.
3. **Wiring, connectors, grounding & EMI/noise**: harnessing, crimping, strain relief, ground loops, motor noise on buses and sensor lines. No node, and it is a frequent cause of failure in student robots.
4. **Brushed DC & stepper motors with PWM drivers (H-bridge, step/dir, TMC-class drivers)**: the cheapest actuation path. It gets only passing mentions (stepper 2, brushed 1) and has no node or hardware row.
5. **Camera & high-bandwidth sensor interfaces (MIPI CSI-2, USB UVC, latency/bandwidth budgeting)**: robot learning depends on cameras. Nothing covers getting camera data into a Jetson or Raspberry Pi reliably.
6. **USB-to-bus adapters as hardware rows**: the servo bus adapter board used with SO-101/LeRobot, ROBOTIS U2D2, and USB-CAN adapters (CANable/candleLight class). These are needed for nearly every listed project and have no rows.
7. **Raspberry Pi 5 (and an STM32 Nucleo/dev-board family) as hardware rows**: they are named in the text but have no Robots & Models rows, although they are the default companion computer and MCU platform in many syllabi.

## Medium importance
8. **Time synchronization & timestamping (PTP/IEEE 1588, hardware timestamps, multi-sensor sync)**: needed for clean imitation-learning datasets. Zero mentions.
9. **Wireless links for robots (Wi-Fi/BLE/ESP-NOW latency, wireless teleoperation and e-stop limitations)**: BLE appears only in spec strings; there is no node on the practice.
10. **CANopen / CiA 402 drive profile (and DroneCAN)**: this is how commercial servo drives are commanded over CAN. EtherCAT is covered, but CAN-based device profiles are not.
11. **RS-485 / Modbus RTU**: common in industrial grippers and actuators (e.g. Robotiq-class grippers). No coverage.
12. **Firmware architecture essentials (interrupts, DMA, timers, watchdogs, bootloaders/OTA updates)**: partly implied by the MCU node, but bootloader/OTA and DMA have zero mentions.
13. **Thermal management & motor/driver derating**: one mention only. It matters for QDD actuators and humanoids.
14. **Regenerative energy & back-EMF handling (brake resistors, bus-voltage clamping)**: a real hazard with BLDC/QDD drives and battery packs. Not covered.
15. **Low-cost commercial QDD actuators beyond CubeMars/RobStride**: e.g. Damiao and Unitree motors, T-Motor robotics actuators, commonly used in open humanoid/legged kits. No rows.
16. **Flight-controller ecosystem (Pixhawk/PX4/ArduPilot) as a reusable embedded stack**: widely taught, cheap, open. No mention (it may belong partly to the Locomotion/drone scope).
17. **FPGA / SoC-FPGA for robotics (AMD Kria/Zynq)**: low-latency perception and motor control. Zero coverage.

## Low importance
18. **Additional edge accelerators (Google Coral, Hailo-10H, Rockchip NPU boards)**: only Hailo-8 and Jetson are listed.
19. **Nordic nRF52/nRF54 MCUs for low-power wireless sensors/wearables**: useful for teleoperation gloves and data-collection devices.
20. **Industrial servo drives (Maxon EPOS, Elmo, Synapticon)**: reference points for EtherCAT/CANopen projects, but too expensive for the lab.
21. **Soldering & PCB assembly practice (SMD rework, ordering assembled PCBs)**: complements the KiCad node.
22. **ESD and lab bench safety for electronics**: small, but easy to add to the safety node.
23. **Tactile / force-sensing electronics (FSR, load cells with HX711-class ADCs, capacitive skins)**: overlaps the Sensing branch, so it could be left out here.

## Summary
- High: 7 · Medium: 10 · Low: 6.
- Per the pipeline, the High items should be sent back to the knowledge-researcher (gaps only) before the Holygraph step.
