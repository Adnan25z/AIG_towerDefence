# Tower Defence Game

## Introduction

This project is a tower defense game developed as part of the AI for Games course. The game integrates various AI techniques to create a dynamic and engaging gameplay experience. Key features include diverse tower types, unique projectiles, and sophisticated enemy pathfinding and decision-making systems. This README provides an overview of the game’s design, AI techniques, and gameplay controls.

## Table of Contents

- [Introduction](#introduction)
- [Gameplay Controls](#gameplay-controls)
- [AI Concepts](#ai-concepts)
  - [Goal Oriented Action Planning](#goal-oriented-action-planning)
  - [Projectile Movement and Shooting Prediction](#projectile-movement-and-shooting-prediction)
  - [Path Searching](#path-searching)
  - [Hierarchical State Machines](#hierarchical-state-machines)
- [Types of Towers and Enemies](#types-of-towers-and-enemies)
  - [Towers](#towers)
  - [Enemies](#enemies)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributors](#contributors)

## Gameplay Controls

The game involves strategically placing towers to prevent creatures from reaching a designated destination. Players start with 1300 credits, which increase with each defeated enemy. Credits are used to buy and upgrade towers.

**Controls:**
- **Space**: Start next level
- **u**: Upgrade tower
- **1, 2, 3**: Select tower to place
- **r**: Find recommended action
- **Right click**: Place or select tower
- **Left click**: Deselect tower
- **Backspace**: Sell selected tower

## AI Concepts

### Goal Oriented Action Planning

The recommendation system utilizes Goal Oriented Action Planning (GOAP) to help players make optimal decisions based on available actions and their costs and values. The system evaluates possible actions, such as purchasing or upgrading towers, to maximize the game’s value within resource constraints.

### Projectile Movement and Shooting Prediction

Projectile prediction is implemented to enhance the accuracy of attacks on moving targets. The system estimates the future position of targets and calculates the optimal projectile trajectory to intersect with that predicted position.

### Path Searching

Enemies use the A* search algorithm for pathfinding, navigating from their spawn points to the goal node. The algorithm considers movement costs and heuristic estimates to find the optimal path.

### Hierarchical State Machines

Towers operate using hierarchical state machines (HSM) to manage different states and sub-states. This allows towers to switch between various behaviors, such as attacking, overdrive, and recharging, based on game conditions.

## Types of Towers and Enemies

### Towers

1. **Blood Moon Tower**: 
   - Normal mode: Shoots predictive bullets.
   - Overdrive mode: Launches bullets in all directions.
   - Special: Can teleport to high enemy activity areas.

2. **Fire Totem Tower**: 
   - Normal mode: Hurls fire projectiles to modify the battlefield.
   - Overdrive mode: Releases multiple fire projectiles simultaneously.

3. **Blue Fire Totem Tower**: 
   - Normal mode: Shoots predictive explosive projectiles.
   - Overdrive mode: Rapidly fires multiple projectiles for explosive damage.

### Enemies

Enemies vary in attributes such as health, speed, credit value, and life value. They navigate the game world using A* search and can adapt their paths to avoid hazards like fire.

## Features

- **AI Techniques**: GOAP, A* pathfinding, predictive projectiles, hierarchical state machines.
- **Gameplay Mechanics**: Tower purchasing, selling, upgrading, and strategic placement.
- **Visual Indicators**: Tower range, state changes, enemy animations, and life indicators.
- **Credit System**: Earn and spend credits to manage resources effectively.

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd tower-defence`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the game: `python main.py`
2. Use the provided controls to start playing and managing your towers.

## Dependencies

- Python 3.x
- Pygame
- Any other dependencies listed in `requirements.txt`

## Contributors

- Adnan Zafar

This README file provides a comprehensive guide to understanding and using the tower defense game, highlighting its AI-driven features and gameplay mechanics. For further details or questions, please refer to the contact information provided in the Contributors section.
