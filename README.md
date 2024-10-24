# SVM-Epilepsy--Machine-Learning-Classifier

## Overview
This project implements a real-time epileptic seizure detection system that utilizes Machine Learning through Support Vector Machines (SVM) classification on electromyography (EMG) and accelerometer (ACC) signal data. By employing wearable technology, it addresses the challenge of continuous patient monitoring through a distributed system architecture. This architecture combines edge computing on mobile devices for data collection with cloud-based resources for signal processing and inference.

For a comprehensive understanding of the system and its implementation, please refer to the following paper:
[Automated Epileptic Seizure Detection System Based on a Wearable Prototype and Cloud Computing to Assist People with Epilepsy](https://link.springer.com/chapter/10.1007/978-3-030-00353-1_18)

## System architecture
![image](https://github.com/user-attachments/assets/897ab42e-4279-4208-bfe4-ec5d15af3c7d)

### Data flow components
1. Mobile app inputs and preprocesses electromyography (EMG) and Accelerometer (ACC) signals comming from the wereable.
2. Features are processed in batch samples and sent, along with GPS coordinates, via a REST API to the cloud server
3. SVM model performs inference.
4. The results trigger the notification system if a high probability of a Tonic-Clonic seizure is detected
5. The medical personnel receives real-time updates in case of a potential seizure, including the GPS coordinates of the patient gathered from their phone.

## Cloud infrastructure
![infraestructura cloud](https://user-images.githubusercontent.com/14321326/34656565-e5900e64-f3e9-11e7-9d5f-8004c59511d0.png)

### Heroku PaaS
- Used to deploy and manage the application in a scalable and cost-effective environment, enabling easy scaling and maintenance.

### Docker Container
- Packages the SVM model, Flask web server, and necessary libraries into a portable container for easy deployment.

### Flask Web Server
- Facilitates communication between the mobile app, SVM model, and api services, allowing for real-time data processing and inference.


## Contribution
Feel free to use. If you have ideas, improvements, or feedback, please feel free to reach out to nicoescobar69@gmail.com. Contributions are welcome!
