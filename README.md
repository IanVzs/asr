# asr
语音识别

## 安装
安装`modelscope`时会安装依赖的torch,但是是GPU-CUDA版本.
如果没有英伟达显卡cuda应该手动安装适合自己的`torch`, 然后再安装`modelscope`补足其他依赖

- CPU 版本安装: `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`
