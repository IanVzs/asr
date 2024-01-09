# asr
语音识别

## 安装
安装`modelscope`时会安装依赖的torch,但是是GPU-CUDA版本.
如果没有英伟达显卡cuda应该手动安装适合自己的`torch`, 然后再安装`modelscope`补足其他依赖

- CPU 版本安装: `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`


## ffmpeg pyav 使用说明
```json
{"text": "感谢您收看更多新闻资讯，", "start": 1921170, "end": 1923310, "text_seg": "感 谢 您 收 看 更 多 新 闻 资 讯 ", "ts_list": [[1921210, 1921350], [1921350, 1921510], [1921510, 1921710], [1921710, 1921810], [1921810, 1922050], [1922310, 1922470], [1922470, 1922670], [1922670, 1922830], [1922830, 1922970], [1922970, 1923070], [1923070, 1923310]]}
```
在`asr`识别模型中,输出的时间戳为: `1923310 / 1000` == 1923.310 秒, `1923310 / 1000 / 60` == 32.055166666666665分钟.
而在pyav读取的视频关键帧中获取到的`pts`为显示帧信息, 如果要获取时间需要 `118800000 / 25 / 60 / 60 / 60` == 22分钟
虽然不知道为啥需要除以三个 `60` 但是还是这样算是准的 (25是视频帧率).

```python
ipdb> stream.base_rate
Fraction(25, 1)
ipdb> stream.average_rate
Fraction(25, 1)
ipdb> stream.frames
48785
ipdb> stream.time_base
Fraction(1, 90000)
ipdb> stream.language
'und'
ipdb> stream.duration
175626000
ipdb>
```

基础知识可以参看: [音视频中的PTS和DTS及同步](https://zhuanlan.zhihu.com/p/540405627)
```葵花小课堂
DTS（Decoding Time Stamp）：即解码时间戳，这个时间戳的意义在于告诉播放器该在什么时候解码这一帧的数据。
PTS（Presentation Time Stamp）：即显示时间戳，这个时间戳用来告诉播放器该在什么时候显示这一帧的数据。
```