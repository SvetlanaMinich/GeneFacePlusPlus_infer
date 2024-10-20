1. Installing CUDA: (must be lower than 12)
sudo apt update
sudo apt install nvidia-cuda-toolkit

check: nvcc --version

2. Clone rep:
git clone https://github.com/yerfor/GeneFacePlusPlus
cd GeneFacePlusPlus

3. Installing Conda from https://docs.anaconda.com/anaconda/install/linux/:
curl -O https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh
bash Anaconda3-2024.06-1-Linux-x86_64.sh   (ENTER, yes, ENTER, yes)

4. Activate venv:
source /root/anaconda3/bin/activate
python3 -V

5. If Python != 3.10:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev

ls -la /usr/bin/python3
sudo rm /usr/bin/python3
sudo ln -s python3.10 /usr/bin/python3
python3 --version

use 3.10 python with python3.10 -V

6. create conda venv with python3.10:
conda create -n geneface python=3.10
conda activate geneface

7. Installing ffmpeg: 
conda install conda-forge::ffmpeg

8. Installing torch for cuda 11.5:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu115

9. Installing dependencies:
sudo apt install gcc-9 g++-9
export CXX=g++-9
export CC=gcc-9
sudo apt-get install cmake libjpeg-dev
pip cache purge
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable" (!!! take much time !!!)

pip install cython
pip install openmim==0.3.9
mim install mmcv==2.1.0

sudo apt-get install libasound2-dev portaudio19-dev
pip install -r docs/prepare_env/requirements.txt -v

(if error with pyworld and dlib:
# Update package lists
sudo apt update

# Install necessary packages for building dlib and pyworld
sudo apt install cmake build-essential libboost-python-dev libboost-thread-dev libboost-system-dev \
                 python3-dev libblas-dev liblapack-dev libatlas-base-dev libopenblas-dev \
                 libboost-all-dev libgtk-3-dev pkg-config libx11-dev

pip install pyworld
pip install dlib
)

bash docs/prepare_env/install_ext.sh 

(resolving errors:
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install python3-dev and so on with gcc==9 and g++==9)

10. Installing zip:
pip install gdown
cd deep_3drecon
rm -r BFM
gdown --folder https://drive.google.com/drive/folders/1o4t5YIw7w4cMUN4bgU9nPf6IyWVG1bEk

11. Installing May dataset:
cd data
mkdir binary
cd binary
mkdir videos
cd videos

gdown --folder https://drive.google.com/drive/folders/1SwZ7uRa5ESzzq_Cd21-Lk5heAZxa9oZO

12. Download checkpoints:
gdown --folder https://drive.google.com/drive/folders/1M6CQH52lG_yZj7oCMaepn3Qsvb-8W2pT
cd checkpoints
sudo apt update
sudo apt install zip
mkdir motion2video_nerf
zip -r motion2video_nerf.zip motion2video_nerf/ (I AM INSTALLING THIS FROM SCRATCH)
rm motion2video_nerf.zip
 
13. START INREFERENCE FROM TERMINAL:
export PYTHONPATH=./
python inference/genefacepp_infer.py --a2m_ckpt=checkpoints/audio2motion_vae --head_ckpt= --torso_ckpt=checkpoints/motion2video_nerf/may_torso --drv_aud=data/raw/val_wavs/KENDALL_JENNER.wav --out_name=may_demo.mp4

14. Run inreference:
- cd GeneFacePlusPlus
- conda activate geneface
export PYTHONPATH=./
python inference/genefacepp_infer.py --a2m_ckpt=checkpoints/audio2motion_vae --head_ckpt= --torso_ckpt=checkpoints/motion2video_nerf/may_torso --drv_aud=data/raw/val_wavs/KENDALL_JENNER.wav --out_name=may_demo.mp4

TODO: Make it work from script