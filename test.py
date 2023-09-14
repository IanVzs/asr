from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

def test_hotword():
    param_dict = dict()
    param_dict['hotword'] = "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/hotword.txt"
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model="damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404",
        param_dict=param_dict)
    
    rec_result = inference_pipeline(audio_in='https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_hotword.wav')
    print(rec_result)

def test_standard():
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch')
    
    rec_result = inference_pipeline(audio_in='https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav')
    print(rec_result)

def test_long():
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
        model_revision="v1.2.4")
    
    rec_result = inference_pipeline(audio_in='https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_vad_punc_example.wav')
    print(rec_result)

if "__main__" == __name__:
    test_standard()
    test_long()
    test_hotword()
