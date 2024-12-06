# Garbage-Classification

This project is focused on classifying garbage into different categories using a YOLOv8 model. The dataset used for training, validation, and testing is provided by Roboflow.

## Dataset

The dataset is organized into three main folders: `train`, `val`, and `test`, each containing subfolders for different classes of garbage:
- cardboard
- glass
- metal
- paper
- plastic
- trash

The dataset configuration is specified in [dataset/data.yaml](dataset/data.yaml).

## Model

The project uses the YOLOv8 model for classification. Pretrained weights are fine-tuned on the provided dataset.

## Files

- `yolov8_fine_tuning.py`: Script to fine-tune the YOLOv8 model on the dataset.
- `Models/`: Directory containing the best models after training.
- `dataset/`: Directory containing the dataset and related files.
  - `data.yaml`: Configuration file for the dataset.
  - `README.dataset.txt`: Information about the dataset.
  - `README.roboflow.txt`: Information about the dataset export from Roboflow.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `LICENSE`: MIT License for the project.

## Usage

To fine-tune the YOLOv8 model on the dataset, run the following command:

```
python yolov8_fine_tuning.py
```