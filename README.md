# Publications

## Instructions

1. [Search Google Scholar for "x-io Technologies"](https://scholar.google.com/scholar?q=%22x-io+Technologies%22) and save each results page to the **html** directory (Ctrl+S, "Webpage, HTML only"). Then run **crawl.py**.
2. Run **crawl_txt_to_json.py**
3. Run **sort_json.py**
4. Run **generate_pending.py**
5. Review each publication in **pending.json** and move it to either **ignore.json** or **publications.json**. Add the missing `product`, `doi`, and `tags` values for each publication moved to **publications.json**. Use `comment` to record the reason for a publication being ignored. Run **sort_json.py** as required to maintain ordering.
6. Update the Madgwick algorithm citation counts in `citations` in **generate_xml.py** to the [latest values shown in Google Scholar](https://scholar.google.com/citations?user=pVoC0_cAAAAJ)
7. Run **generate_xml.py**

## Tags

- **Activity monitoring**: Detection of discrete activities, or long-term monitoring of human movement.
- **Aerospace**: Drones, aircraft, spacecraft, rockets, satellites, or balloons.
- **Biomechanics**: Biomechanical modelling, or other biomechanics research not covered by other tags.
- **Equine**: Horses or horse riding
- **Ergonomics**: Workplace ergonomics, posture, or loading of the body.
- **Exoskeletons**: Exoskeletons, exosuits, or walking assist devices.
- **Gait**: Walking or running, including gait measures in pedestrian tracking.
- **HCI**: Human-computer interaction: input, gestures, interfaces, AR/VR, or HCI venues.
- **IMU development**: IMU hardware, algorithms, calibration, and other sensor research not covered by other tags.
- **Marine**: Seas, rivers, waterways, or ice, including vessels and underwater vehicles.
- **Medical**: Medical research not covered by other tags: medical technology, physiology, neuroscience, or public health.
- **Mining & industry**: Mining, heavy industry, construction, manufacturing, infrastructure, agriculture, or forestry.
- **Music & arts**: Music, dance, performance, or other arts, including supporting technology and artistic sonification.
- **Navigation**: Positioning, localisation, or tracking of people, vehicles, robots, or devices moving through the world.
- **Parasport**: Sport or exercise for people with disabilities, or wheelchairs.
- **Prosthetics**: Prosthetics, orthotics, or amputees.
- **Rehabilitation**: Therapy, recovery, task assistance, assistive devices (including patient-facing prostheses and exoskeletons), or rehabilitation venues.
- **Robotics**: Robots, drones, autonomous vehicles, powered exoskeletons or prostheses, or teleoperation.
- **Sport**: Sport, athletic performance, exercise, or fitness, including horse riding and parasport.
