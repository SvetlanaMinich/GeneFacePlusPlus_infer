from inference.genefacepp_infer import GeneFace2Infer
import time

start = time.time()

inp = {
            'a2m_ckpt': 'checkpoints/audio2motion_vae',
            'postnet_ckpt': '',
            'head_ckpt': '',
            'torso_ckpt': 'checkpoints/motion2video_nerf/may_torso',
            'drv_audio_name': 'data/raw/val_wavs/demo_audio.wav',
            'drv_pose': 'nearest',
            'blink_mode': 'none',
            'temperature': 0.2,
            'mouth_amp': 0.4,
            'lle_percent': 0.2,
            'debug': 'store_true',
            'out_name': 'may_demo.mp4',
            'raymarching_end_threshold': 0.05,
            'low_memory_usage': 'store_true',
            }
GeneFace2Infer.example_run(inp)
print('     > Rendering time:', time.time() - start)