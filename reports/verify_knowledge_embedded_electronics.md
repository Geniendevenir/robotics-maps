# Verification: Embedded & electronics

Date: 2026-11-13. Branch: `research/knowledge-embedded-electronics`.

Reviewed **74 rows**: **22 verified / 52 corrected / 0 rejected**. Retained 17 knowledge nodes, 29 hardware/software references, 28 project candidates.

## Method and boundaries

- Independently opened all 65 distinct input URLs using page-content retrieval and an HTTP audit; reviewed official specifications, repository READMEs, papers and course material. Reused identical URLs across rows rather than pretending each occurrence is a new source.
- HTTP 200 is not sufficient: the AI HAT+ portal URL serves Pico 2 W material; Springer direct HTTP serves a JavaScript challenge, but the page-content reader exposed the actual book metadata. The ICRA 2025 site returned HTTP 403 directly (page-content retrieval exposed conference material); it is not needed by any row and was removed from the cleaned source list.
- The Pico 2 product-brief PDF downloaded (HTTP 200), but the page-content reader did not extract its text. Replaced the hardware row's PDF dependency with the opened official Pico 2 product page and SDK license. The original PDF remains only in the historical consulted list, not in any row Sources; no claim relies on an unread PDF.
- Opened replacement primary references for AI HAT+, ISO 13849-1, battery monitoring, Pico 2, UNO Q licensing, Teensy manufacturing, ODrive CAN protocol and ESP32-S3 CAN-FD restrictions. No Notion reads or writes were performed.
- Source content verifies existence and documented capabilities, not guaranteed stock, shipment, price, student build time, best-in-market rankings or active employment. No Ecosystem organization rows occur in this file; builder identities were checked against official sites/repos, but continuing operations in 2026 cannot be inferred from an old announcement alone.
- Project demos are proposals. Duration, workload shares, complexity, accessibility and cost buckets are lab planning estimates, not experimentally established results. No hardware was built or safety-certified in this verification.
- Followed the explicit existing-branch/no-PR/no-Notion instructions. Knowledge and Robots & Models Status is `To verify`. Projects retain schema-valid `Idea`: `To verify` is not an allowed Projects status. No auto-managed reverse relations (including `Used in projects`) are emitted.
- Preserved the prescribed top-level research envelope. Removed private `_accessibility_reason` keys from database rows to satisfy exact schema keys; original justifications are preserved below. Unknown release years remain null because Release year is numeric, not a string field.

## Important corrections

- ESP32-S3 is Classical-CAN-only natively. A CAN-FD sniffer needs a separate FD controller and compatible transceiver. Current ODrive documentation now supports CAN-FD on Pro/S1 with firmware/configuration conditions; it is not correct to universally call ODrive Classical-only either.
- Current ODrive S1/Pro firmware is not public source. S1 is 66 x 50 mm; the 51 x 64 mm footprint belonged to Pro.
- Smart-servo follower and leader gear ratios differ. Components are represented as Simulator/Tool, N/A form factor, rather than pretending a servo is a hand or a modular actuator a quadruped.
- Emergency power removal is not universally a safe stop for gravity-loaded mechanisms. Contact inference is explicitly not safety-rated. Beginner pack assembly and unguarded hand back-driving were removed.
- Reachy local inference requires the onboard-compute Wireless variant; Berkeley and Reachy budgets now account conservatively for unverified delivered EU costs. Accelerator throughput figures cannot be compared without precision/workload context.

## Row-by-row disposition

### Knowledge Map (0 verified / 17 corrected / 0 rejected)

| # | Input row | Disposition | Reason |
|---|---|---|---|
| 1 | Electronics fundamentals for robots | corrected | Opened references support the retained explanation. Removed non-schema _accessibility_reason (preserved below). |
| 2 | Microcontrollers & bare-metal firmware | corrected | Removed unsourced adoption/rising-popularity claims; verified MCU specifications and Cornell RP2350 teaching platform. Removed non-schema _accessibility_reason (preserved below). |
| 3 | Communication buses (UART, I2C, SPI, CAN) | corrected | Distinguished Classical CAN from CAN-FD; ESP32-S3 TWAI needs an external transceiver and cannot receive FD frames; removed market-share claims. Removed non-schema _accessibility_reason (preserved below). |
| 4 | Smart servos & serial actuator buses | corrected | Specified follower versus mixed-ratio leader servos; replaced unsupported reference-platform/research-standard and majority claims. Removed non-schema _accessibility_reason (preserved below). |
| 5 | Motor drivers & power electronics | corrected | Opened references support the retained explanation. Removed non-schema _accessibility_reason (preserved below). |
| 6 | BLDC motor control & field-oriented control (FOC) | corrected | Separated proprietary ODrive S1/Pro firmware from open moteus/SimpleFOC; removed unsupported price-decline and industry-norm claims. Removed non-schema _accessibility_reason (preserved below). |
| 7 | Sensor interfacing & signal conditioning | corrected | Removed unverified Bosch/TDK player list and speculative sensor-count trend; retained documented education and controller examples. Removed non-schema _accessibility_reason (preserved below). |
| 8 | Batteries & power distribution | corrected | Removed unsupported #1-cause statistic; replaced unrelated H-bridge note with TI battery-monitor/protector reference and beginner-safe scope. Removed non-schema _accessibility_reason (preserved below). |
| 9 | Embedded Linux & companion computers | corrected | Replaced wrong AI HAT+ URL and removed unsupported mainstream-adoption assertion; kept documented Linux/MCU architecture. Removed non-schema _accessibility_reason (preserved below). |
| 10 | Real-time OS & real-time control loops | corrected | Removed false guarantee that an RTOS prevents all deadline misses; distinguished scheduling support from measured system behaviour. Removed non-schema _accessibility_reason (preserved below). |
| 11 | ROS 2 hardware interfaces (ros2_control, micro-ROS) | corrected | Clarified MCU client/agent architecture and development-version documentation; kept observed micro-ROS migration without inferring migration date. Removed non-schema _accessibility_reason (preserved below). |
| 12 | Industrial real-time fieldbus (EtherCAT) | corrected | Removed unsupported market-dominance/high-end-humanoid generalizations; ETG verifies origin, IEC standard and real-time design. Removed non-schema _accessibility_reason (preserved below). |
| 13 | PCB design for robots | corrected | Opened references support the retained explanation. Removed non-schema _accessibility_reason (preserved below). |
| 14 | Edge AI hardware & on-device inference | corrected | Corrected AI HAT+ link and distinguished theoretical accelerator metrics from achieved model performance. Removed non-schema _accessibility_reason (preserved below). |
| 15 | Embedded simulation & hardware-in-the-loop testing | corrected | Separated software simulation from physical hardware-in-the-loop cost and avoided promising all CI use is free. Removed non-schema _accessibility_reason (preserved below). |
| 16 | Electrical safety & functional safety for robots | corrected | Added primary ISO catalogue; removed unsafe universal power-cut advice and unsupported mandatory/certification implication. Removed non-schema _accessibility_reason (preserved below). |
| 17 | Open-source actuator & electronics stacks for legged/humanoid robots | corrected | Distinguished BLDC humanoid stack from smart-servo Open Duck; qualified US BOM estimate and feasibility, not guaranteed reproducibility. Removed non-schema _accessibility_reason (preserved below). |

### Robots & Models (10 verified / 19 corrected / 0 rejected)

| # | Input row | Disposition | Reason |
|---|---|---|---|
| 1 | SO-101 arm | corrected | Clarified five arm joints plus gripper, follower versus leader gearing, and source-reported BOM price. |
| 2 | Feetech STS3215 servo | corrected | Classified servo as a component/tool, not a hand or standalone robot; removed unsupported cheapest and encoder-detail claims. |
| 3 | Dynamixel (Protocol 2.0) | corrected | DYNAMIXEL protocol/family is not a hand or gripper; removed unsupported research-standard assertion. |
| 4 | ESP32-S3 | corrected | Made native Classical-CAN-only restriction explicit and removed unsourced euro board quote. |
| 5 | Raspberry Pi Pico 2 (RP2350) | corrected | Added readable official product page and scoped open-source flag to SDK rather than claiming open silicon. |
| 6 | Teensy 4.1 | corrected | Distinguished PJRC design from current SparkFun manufacturing/sales and removed fastest-hobby-MCU superlative. |
| 7 | Arduino UNO Q | corrected | Documented scope of open-source claim using official UNO Q licensing FAQ. |
| 8 | NVIDIA Jetson Orin Nano Super Developer Kit | verified | Opened official references support existence, builder and retained specifications. |
| 9 | NVIDIA Jetson AGX Thor | verified | Opened official references support existence, builder and retained specifications. |
| 10 | Hailo-8 | corrected | Replaced Pico-page URL with AI HAT+ product page and clarified 26-TOPS versus 13-TOPS variants. |
| 11 | ODrive S1 / Pro | corrected | Fixed S1/Pro size conflation and made non-public current-generation firmware explicit. |
| 12 | mjbots moteus | corrected | Removed unsubstantiated hobby-quadruped adoption claim. |
| 13 | SimpleFOC | corrected | Removed unsupported lowest-cost/any-MCU assertion. |
| 14 | MIT Mini Cheetah actuator | corrected | Actuator reference is a component, not a complete quadruped; removed unsupported template-for-most claim and set release year unknown (thesis date is not product release evidence). |
| 15 | Berkeley Humanoid Lite | corrected | Removed most-accessible ranking and qualified the source-reported US parts budget. |
| 16 | Open Duck Mini v2 | corrected | Added source-reported BOM target and clarified community builder attribution; N/A form factor avoids mislabeling a biped character robot as a humanoid. |
| 17 | Reachy Mini | verified | Opened official references support existence, builder and retained specifications. |
| 18 | ros2_control | verified | Opened official references support existence, builder and retained specifications. |
| 19 | micro-ROS | verified | Opened official references support existence, builder and retained specifications. |
| 20 | Zephyr RTOS | verified | Opened official references support existence, builder and retained specifications. |
| 21 | FreeRTOS | corrected | Removed unsupported most-widely-used RTOS ranking. |
| 22 | KiCad | verified | Opened official references support existence, builder and retained specifications. |
| 23 | Wokwi | verified | Opened official references support existence, builder and retained specifications. |
| 24 | Renode | corrected | Distinguished emulation/CI capability from a physical HIL rig. |
| 25 | SOEM (Simple Open EtherCAT Master) | corrected | Qualified license/access rather than calling all uses free. |
| 26 | Edge Impulse | corrected | Removed unsupported fastest-pipeline superlative. |
| 27 | LiteRT for Microcontrollers | verified | Opened official references support existence, builder and retained specifications. |
| 28 | LeRobot | verified | Opened official references support existence, builder and retained specifications. |
| 29 | CubeMars / RobStride integrated actuators | corrected | Replaced ambiguous two-manufacturer aggregate with one identifiable official RobStride product; classified as actuator tool. Renamed to RobStride 00 integrated actuator. |

### Project candidates (12 verified / 16 corrected / 0 rejected)

| # | Input row | Disposition | Reason |
|---|---|---|---|
| 1 | Blink to bus: simulated firmware bootcamp | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 2 | Breadboard power & multimeter lab | corrected | Replaced beginner loose-cell/LiPo exercise with current-limited supply scope. |
| 3 | Drive one STS3215 servo from Python | corrected | Current-feedback availability is not established for every selected servo/driver combination. |
| 4 | Build and calibrate an SO-101 leader/follower pair | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 5 | Custom power & e-stop board for the SO-101 | corrected | Qualified emergency-stop demonstration against gravity/load hazards and avoided implying a certified safety function. |
| 6 | micro-ROS ESP32 sensor node | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 7 | ros2_control hardware interface for SO-101 | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 8 | Jitter lab: FreeRTOS vs Zephyr vs PREEMPT_RT | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 9 | SimpleFOC gimbal motor: position, velocity, torque modes | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 10 | Low-cost quasi-direct-drive actuator test bench | corrected | Distinguished CAN/CAN-FD controller compatibility and removed unsafe hand back-driving test. |
| 11 | CAN-FD bus sniffer & dashboard | corrected | ESP32-S3 cannot natively sniff CAN-FD; added external-controller/transceiver requirement. |
| 12 | Firmware CI with hardware-in-the-loop | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 13 | TinyML gesture/keyword control on an MCU | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 14 | On-board policy: run an ACT/diffusion policy on Jetson Orin Nano | corrected | Made power/network assumptions explicit; on-board inference alone does not make a robot untethered. |
| 15 | Edge AI accelerator benchmark for robot perception | corrected | Corrected AI HAT+ reference and avoided promising identical full-size detector fits both accelerators and MCU. |
| 16 | VLA on board a mobile manipulator with Jetson Thor | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 17 | Arduino UNO Q split-brain robot | corrected | Made watchdog/stop behaviour an implementation requirement, not an automatic property of UNO Q. |
| 18 | Custom BLDC driver PCB | corrected | Restricted first custom power-stage testing to supervised low-voltage/current-limited setup. |
| 19 | Open Duck Mini build | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 20 | Berkeley Humanoid Lite reproduction | corrected | US$5k BOM is not a verified EUR delivered budget; budget conservatively above €5k for reproduction. |
| 21 | Battery pack + BMS telemetry for a walking robot | corrected | Replaced unsafe novice custom-cell pack scope and unrelated KiCad-only BMS evidence. Renamed to Protected battery pack + BMS telemetry for a walking robot. |
| 22 | EtherCAT test cell with SOEM | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |
| 23 | Reachy Mini custom expressive behaviours on the edge | corrected | On-device inference requires wireless onboard-compute version, not tethered Lite; raised delivered budget category. |
| 24 | Tactile-free force estimation from motor currents | corrected | Reframed unverified servo-current force estimation as an exploratory telemetry/contact experiment, never a safety function. Renamed to Experimental contact detection from servo telemetry. |
| 25 | Embedded Rust (Embassy) firmware for a robot joint | corrected | Embassy target support and 1 kHz performance are experimental requirements; avoid implying Teensy is a ready-supported path. |
| 26 | Sim-matched digital twin of the arm electronics | corrected | Renode is not an out-of-box SO-101 mechanics/serial-servo digital twin; made custom modeling requirement explicit. |
| 27 | Joint bus shoot-out: serial vs CAN-FD vs EtherCAT | corrected | One joint cannot generally switch among all three buses; use three supported endpoints and document non-bus confounders. |
| 28 | ros2_control driver for an EtherCAT servo drive | verified | Official references support the named tools and proposed workflow; demo is a proposal, not an observed result. |

## Accessibility justifications retained outside sync rows

These are the researcher's educational estimates, not verified market or effort guarantees. Unsupported precise price claims below are historical rationale only; cleaned rows and source evidence take precedence.

- **Electronics fundamentals for robots**: Cheap kit, huge amount of beginner tutorials, results in days.
- **Microcontrollers & bare-metal firmware**: Software-strong team: firmware is just code with timers and pins; boards cost €5-40.
- **Communication buses (UART, I2C, SPI, CAN)**: Concepts are software-like (protocols, packets); need a logic analyzer and care with wiring.
- **Smart servos & serial actuator buses**: Plug-and-play, Python SDKs (LeRobot), ~€14 per servo.
- **Motor drivers & power electronics**: Off-the-shelf driver boards are easy; understanding and debugging power stages takes real electrical skill and can burn parts.
- **BLDC motor control & field-oriented control (FOC)**: Open-source boards and libraries exist, but tuning and safety need care; actuator cost €50-300 each.
- **Sensor interfacing & signal conditioning**: Mostly code and breakout boards; noise debugging needs an oscilloscope.
- **Batteries & power distribution**: Concepts are simple, but LiPo safety must be learned and respected.
- **Embedded Linux & companion computers**: Pure software territory for this team; boards €60-250.
- **Real-time OS & real-time control loops**: OS concepts are familiar to 42 students; measuring timing needs a scope/logic analyzer.
- **ROS 2 hardware interfaces (ros2_control, micro-ROS)**: Software-heavy; documentation is decent but integration debugging takes time.
- **Industrial real-time fieldbus (EtherCAT)**: Drives and slaves are expensive and the stack is complex; low priority for a 4-6 month student lab.
- **PCB design for robots**: Tool is free and fabs are cheap, but each board iteration takes 1-2 weeks and first boards often have bugs.
- **Edge AI hardware & on-device inference**: Team's AI strength applies directly; Jetson Orin Nano Super is affordable, Thor is €3.5k+.
- **Embedded simulation & hardware-in-the-loop testing**: Free, software-only, runs in CI.
- **Electrical safety & functional safety for robots**: E-stop and watchdog basics are easy; formal functional safety is a specialist field.
- **Open-source actuator & electronics stacks for legged/humanoid robots**: Integrating 10-20 actuators, power and compute is a multi-month effort even with open designs.

## Source audit

Every input URL below was attempted. “Opened” means content was accessible with the page reader and/or HTTP, not that every assertion on a page is independently true. Row-level support and corrections are recorded above.

| Input URL | Access / relevance |
|---|---|
| https://2025.ieee-icra.org/ | Direct HTTP 403; page reader exposed conference material; removed as unnecessary taxonomy-only source. |
| https://ai.google.dev/edge/litert/microcontrollers/overview | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://arxiv.org/abs/1909.06586 | Opened 2019 Mini Cheetah controller paper; platform context, not a 2018 actuator release announcement. |
| https://arxiv.org/abs/2504.17249 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://control.ros.org/rolling/index.html | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://datasheets.raspberrypi.com/pico/pico-2-product-brief.pdf | HTTP 200 PDF downloaded; text extraction unavailable in page reader; readable official product replacement used. |
| https://docs.arduino.cc/hardware/uno-q/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://docs.arduino.cc/learn/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://docs.edgeimpulse.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/twai.html | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://docs.rust-embedded.org/book/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://docs.zephyrproject.org/latest/introduction/index.html | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://dspace.mit.edu/handle/1721.1/118671 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://ece4760.github.io/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://emanual.robotis.com/docs/en/dxl/protocol2/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://embassy.dev/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://en.wikipedia.org/wiki/ISO_13849 | Opened secondary summary; safety row upgraded to ISO primary abstract. |
| https://github.com/OpenEtherCATsociety/SOEM | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/TheRobotStudio/SO-ARM100 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/apirrone/Open_Duck_Mini | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/huggingface/lerobot | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/huggingface/lerobot/blob/main/README.md | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/micro-ROS/micro_ros_espidf_component | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/mjbots/moteus | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/mjbots/moteus/blob/main/docs/reference.md | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/odriverobotics/ODrive | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/ros-controls/ros2_control | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://github.com/simplefoc/Arduino-FOC | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://hades.mech.northwestern.edu/index.php/Modern_Robotics | Opened conference/book material for taxonomy, not hardware capability evidence. |
| https://hailo.ai/products/ai-accelerators/hailo-8-ai-accelerator/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://huggingface.co/blog/reachy-mini | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://huggingface.co/docs/lerobot/so101 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://kernelnewbies.org/Linux_6.12 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://learn.adafruit.com/category/learn-arduino | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://learn.sparkfun.com/tutorials/i2c/all | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://link.springer.com/referencework/10.1007/978-3-319-32552-1 | Direct HTTP challenge, actual title/editors/2016 edition accessible via page reader; taxonomy reference only. |
| https://lite.berkeley-humanoid.org/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://micro.ros.org/ | HTTP 200 move notice points to micro.vulcanexus.org; checked destination. |
| https://micro.vulcanexus.org/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://odriverobotics.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://pip.raspberrypi.com/categories/1088-raspberry-pi-ai-hat | HTTP 200, WRONG CONTENT (Pico 2 W); replaced by official AI HAT+ product page. |
| https://platformio.org/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://ptolemy.berkeley.edu/books/leeseshia/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://renode.io/ | Redirects to Antmicro Renode page; simulation capabilities, not a supplied physical HIL rig. |
| https://roboticsconference.org/ | Opened conference/book material for taxonomy, not hardware capability evidence. |
| https://robstride.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://simplefoc.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://wokwi.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.can-cia.org/can-knowledge/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.corl.org/ | Opened conference/book material for taxonomy, not hardware capability evidence. |
| https://www.cubemars.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.espressif.com/en/products/socs/esp32-s3 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.ethercat.org/en/technology.html | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.falstad.com/circuit/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.feetechrc.com/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.freertos.org/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.kicad.org/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.pjrc.com/store/teensy41.html | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.ti.com/lit/an/slva321/slva321.pdf | PDF opened/read; current recirculation/decay in motor drivers, not a battery/BMS design source. |
| https://www.ti.com/product/DRV8833 | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |
| https://www.zephyrproject.org/ | Opened; 200 in direct HTTP audit; official product/project/documentation or scholarly source used where relevant. |

### Added primary references

- https://docs.espressif.com/projects/esp-faq/en/latest/software-framework/peripherals/twai.html
- https://docs.odriverobotics.com/v/latest/manual/can-protocol.html
- https://raw.githubusercontent.com/raspberrypi/pico-sdk/master/LICENSE.TXT
- https://www.arduino.cc/product-uno-q/
- https://www.iso.org/standard/73481.html
- https://www.raspberrypi.com/products/ai-hat/
- https://www.raspberrypi.com/products/raspberry-pi-pico-2/
- https://www.sparkfun.com/sparkfun-teensy-press-release
- https://www.ti.com/product/BQ76952

## Validation

Passed: JSON parsing; exact field sets for all 74 rows; every select/multi-select against the checked-in schema; required text/boolean/numeric and null-release-year handling; all 28 effort-share sums = 100; unique titles; all local Knowledge nodes / Robots & models / project prerequisite references resolve; all row source URLs appear in the consulted list; 46 knowledge/hardware statuses = To verify; 28 project statuses = Idea; no formulas, private metadata or auto-managed reverse fields. `git diff --check` passed. No executable application changes; lint/type-check/test tooling is not defined in this documentation/data repository, so data validation was used instead. No active non-sample git hooks were present.
