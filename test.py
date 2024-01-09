import json
import argparse
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

def test_hotword(file):
    param_dict = dict()
    param_dict['hotword'] = "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/hotword.txt"
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model="damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404",
        param_dict=param_dict)

    rec_result = inference_pipeline(audio_in=file or 'https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_hotword.wav')
    print(rec_result)

def test_standard(file):
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch')

    rec_result = inference_pipeline(audio_in=file or 'https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav')
    print(rec_result)

def test_long(file):
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
        model_revision="v1.2.4")

    rec_result = inference_pipeline(audio_in= file or 'https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_vad_punc_example.wav')
    with open(f"long_text_result.txt", "a", encoding="utf-8") as f:
        f.write(file + "\n")
        f.write(rec_result["text"])
    
    with open(f"long_text_result_sentences.txt", "a", encoding="utf-8") as f:
        f.write(file + "\n")
        for i in rec_result["sentences"]:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")

if "__main__" == __name__:
    parser = argparse.ArgumentParser("对各个不同特点的语言模型进行测试")
    # 添加--type参数
    parser.add_argument("--type", choices=["long", "stan", "hot"], help="Choose the type of method to execute, stan(standard)")
    # 添加--file参数
    parser.add_argument("--file", help="音频文件路径", type=argparse.FileType("r"))
    # 解析命令行参数
    args = parser.parse_args()

    # # 检查--file参数指定的文件路径是否存在
    # if args.file and not os.path.isfile(args.file):
    #     print("File does not exist!")
    #     exit(1)
    file_path = args.file.name
    args.file.close()
    # 根据--type参数选择执行的方法
    if args.type == "long":
        test_long(file_path)
    elif args.type == "stan":
        test_standard(file_path)
    elif args.type == "hot":
        test_hotword(file_path)
    else:
        print("Invalid type argument!")
