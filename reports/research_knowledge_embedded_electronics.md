# Research log: Embedded & electronics

Output: output/knowledge_embedded_electronics.json (17 nodes, 29 robots/models/tools, 28 project candidates, 65 sources opened).

## Method
- Every URL below was fetched with curl and key claims were grepped from page text (specs, prices, dates).
- No web search engine was available in this session. Candidate sources came from known primary pages (vendor docs, papers, repos, course pages, conference sites). So the saturation stop was judged on the taxonomy, not measured on query results: the last two fetch batches (14 URLs) added no new nodes.
- Pages blocked (403/timeout) are NOT used as sources: raspberrypi.com product pages, st.com, iso.org, wiki.linuxfoundation.org, analog.com. That is why ISO 13849 claims rest on Wikipedia only, which is weak.
- Release year is null whenever the opened page did not state it.

## Fetch status
```
1 200 456901 https://docs.arduino.cc/hardware/uno-q/
2 200 413946 https://docs.arduino.cc/learn/
3 200 76546 https://www.espressif.com/en/products/socs/esp32-s3
4 403 5550 https://www.raspberrypi.com/products/raspberry-pi-pico-2/
5 403 5535 https://www.raspberrypi.com/products/raspberry-pi-5/
6 403 5490 https://www.raspberrypi.com/products/ai-hat/
7 000 0 https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html
8 200 68988 https://www.pjrc.com/store/teensy41.html
9 200 1212137 https://www.freertos.org/
10 200 228275 https://www.zephyrproject.org/
11 200 686 https://micro.ros.org/
12 200 293442 https://github.com/micro-ROS/micro_ros_espidf_component
13 200 14953 https://control.ros.org/rolling/index.html
14 200 315923 https://github.com/ros-controls/ros2_control
15 200 71944 https://www.kicad.org/
16 200 177051 https://odriverobotics.com/
17 429 18 https://mjbots.com/products/moteus-r4-11
18 200 51565 https://simplefoc.com/
19 200 340277 https://github.com/simplefoc/Arduino-FOC
20 200 330264 https://emanual.robotis.com/docs/en/dxl/protocol2/
21 200 31511 https://www.feetechrc.com/
22 200 374304 https://github.com/TheRobotStudio/SO-ARM100
23 200 204927 https://huggingface.co/docs/lerobot/so101
24 200 345389 https://github.com/huggingface/lerobot
25 200 295093 https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/
26 200 553168 https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
27 200 207082 https://hailo.ai/products/ai-accelerators/hailo-8-ai-accelerator/
28 200 146310 https://ai.google.dev/edge/litert/microcontrollers/overview
29 200 164232 https://docs.edgeimpulse.com/
30 200 64187 https://www.ethercat.org/en/technology.html
31 200 89382 https://www.can-cia.org/can-knowledge/
32 200 245716 https://github.com/OpenEtherCATsociety/SOEM
33 200 478889 https://kernelnewbies.org/Linux_6.12
34 403 5510 https://wiki.linuxfoundation.org/realtime/start
35 403 5490 https://www.iso.org/standard/73481.html
36 403 5490 https://www.iso.org/standard/59970.html
37 200 43007 https://hades.mech.northwestern.edu/index.php/Modern_Robotics
38 200 3038 https://link.springer.com/referencework/10.1007/978-3-319-32552-1
39 200 8064 https://ptolemy.berkeley.edu/books/leeseshia/
40 200 299900 https://ece4760.github.io/
41 200 558442 https://dspace.mit.edu/handle/1721.1/118671
42 200 14525 https://lite.berkeley-humanoid.org/
43 200 43905 https://arxiv.org/abs/2504.17249
44 200 324848 https://www.ti.com/product/DRV8833
45 200 196672 https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries
46 200 29190 https://docs.rust-embedded.org/book/
47 200 16609 https://embassy.dev/
48 200 213137 https://www.cubemars.com/
49 200 1875 https://robstride.com/
50 200 297450 https://github.com/apirrone/Open_Duck_Mini
51 200 529115 https://huggingface.co/blog/reachy-mini
52 200 52743 https://wokwi.com/
53 200 352901 https://renode.io/
54 200 2958 https://www.falstad.com/circuit/
55 200 9730 https://platformio.org/
56 200 372102 https://2025.ieee-icra.org/
57 200 11452 https://roboticsconference.org/
58 200 305919 https://www.corl.org/
59 403 5490 https://www.iso.org/standard/73933.html
60 200 675222 https://www.ti.com/lit/an/slva321/slva321.pdf
61 200 67995 https://learn.sparkfun.com/tutorials/i2c/all
62 200 60976 https://learn.adafruit.com/category/learn-arduino
63 200 269488 https://github.com/mjbots/moteus
64 200 238165 https://github.com/odriverobotics/ODrive
```

## Open issues for the verifier
- Prices for the Jetson Orin Nano Super, Arduino UNO Q and ODrive were not found on the opened pages, so they are left as unknown.
- The Key players list for Sensor interfacing is not verified (overlaps with the Sensing branch).
- Relevant orgs, Built by and Used by are left empty. The ecosystem branches should fill them.
