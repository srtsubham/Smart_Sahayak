# Smart Sahayak: AI-Driven Printing & Stationery Kiosk

**Project Phase:** Initial Software Prototype (March 2026)
**Seminar Code:** NCS4651
**Developer:** Somya Ranjan Tripathi

---

## 🚀 Overview

Smart Sahayak is a revolutionary self-service kiosk designed to streamline access to printing, document handling, and stationery supplies. This prototype focuses on the backend software architecture and AI pipeline required to manage user interaction and hardware triggers autonomously.

## 🛠️ Core Features

- **Dual-Layer Gateway**: Utilizes frame-differencing for motion detection combined with a 2FA human face verification layer for secure session initialization.
- **Privacy-First Architecture**: Implements a volatile local cache system that executes a mandatory wipe command immediately upon new session detection to ensure data sovereignty.
- **Speaking Interactive AI**: A standalone Python application integrating Speech-to-Text (STT) and Text-to-Speech (TTS) for seamless, hands-free user prompts.
- **Operational Cooldown**: Includes a synchronized 5-second buffer between sessions to ensure stable state transitions and prevent rapid re-triggering.

## 📂 Project Structure

- `src/main.py`: The central orchestrator managing the system lifecycle and cooldown logic.
- `src/gateway.py`: Handles hardware initialization, computer vision for face detection, and the 2FA trigger.
- `src/interaction.py`: Manages the cognitive AI layer, processing voice prompts and user intent.
- `database/`: Local storage for session logs and stationery inventory records.
- `models/`: Repository for lightweight machine learning models and classifiers.
- `doc/`: Project Manifestos, blueprints, and academic documentation.

## ⚙️ Setup & Installation

1.  **Requirement**: Python 3.12 (Stable)
2.  **Environment Setup**:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Execution**:
    ```powershell
    python src/main.py
    ```

---

**Note:** This project adheres to a strict prototype model work and only rules for mission-critical modules, focusing on local processing to ensure maximum security and privacy and backend driven software work only is taken in consideration. Hardware interactions are abstracted through the gateway layer & will be implemented in future version after prototype validation and success.....
